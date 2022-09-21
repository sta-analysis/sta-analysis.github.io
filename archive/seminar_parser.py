from bs4 import BeautifulSoup
import dateutil.parser as parser
from datetime import datetime
import json
from itertools import groupby

# code to parse the seminar and pull all the data into a JSON file
# run with python3 seminar_parser.py | jq > ../data/seminars.json

def parse_entry(entry):
    date_str = entry.get_text().split("\n")[0]
    date = parser.parse(date_str)
    name = entry.strong
    if name is not None:
        name = name.get_text()
        if name.startswith("No ") or name.startswith("no ") or name.startswith("Problem "):
            return None
    else:
        return None

    title = str(entry.em)[4:-5].strip() if entry.em is not None else ""
    video_url = ""
    abstract = ""
    for a_ref in entry.find_all('a'):
        try:
            abstract_file = a_ref['knowl']
            try:
                with open(abstract_file) as f:
                    abstract = f.read().strip()
            except FileNotFoundError:
                pass
        except KeyError:
            pass
        try:
            video_url = a_ref['href']
        except KeyError:
            pass

    dct = {'name': name, 'title': title, 'abstract': abstract, 'video': video_url}
    return date.strftime("%Y-%m-%d"), dct

def get_semester_title(date_str):
    date = datetime.strptime(date_str, "%Y-%m-%d")
    if date.month in (1,2,3,4):
        sem = "Spring"
    elif date.month == 5 and date.day <= 20:
        sem = "Spring"
    elif date.month in (5,6,7,8):
        sem = "Summer"
    else:
        sem = "Autumn"
    return f"{sem} {date.year}"

def semester_key(tup):
    sem_str = tup[0]
    lookup = {"Spring": 0, "Summer": 1, "Autumn": 2}
    name, year = sem_str.split()
    return (int(year), lookup[name])



if __name__ == '__main__':
    with open('seminars.html') as f:
        content = f.read()
        soup = BeautifulSoup(content, 'html.parser')

    # a beautiful iterator
    entries = dict(
            sorted(
                map(
                    lambda x: (x[0], dict(x[1])),
                    groupby(
                        sorted(
                            (parse_entry(entry) for entry in soup.find_all('li') if parse_entry(entry) is not None),
                            key=lambda x: get_semester_title(x[0])),
                        lambda x: get_semester_title(x[0]))),
                key=semester_key,
                reverse=True))
    print(json.dumps(entries))

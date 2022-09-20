from bs4 import BeautifulSoup
import dateutil.parser as parser
import json

# code to parse the seminar and pull all the data into a JSON file
# run with python3 seminar_parser.py | jq > ../data/seminars.json

def parse_entry(entry):
    date_str = entry.get_text().split("\n")[0]
    date = parser.parse(date_str)
    name = entry.strong
    title = str(entry.em)[4:-5].strip() if entry.em is not None else entry.em
    if entry.a is not None:
        abstract_file = entry.a['knowl']
        try:
            with open(abstract_file) as f:
                abstract = f.read().strip()
        except FileNotFoundError:
            abstract = None
    else:
        abstract = None

    if name is not None:
        name = name.get_text()
        if name.startswith("No "):
            name = "No Seminar"
    else:
        name = "No Seminar"
    dct = {'name': name, 'title': title, 'abstract': abstract}
    return date.strftime("%Y-%m-%d"), dct


if __name__ == '__main__':
    with open('seminars.html') as f:
        content = f.read()
        soup = BeautifulSoup(content, 'html.parser')
    entries = [parse_entry(entry) for entry in soup.find_all('li')]
    entries.sort(key = lambda x: x[0], reverse=True)
    print(json.dumps(dict(entries)))

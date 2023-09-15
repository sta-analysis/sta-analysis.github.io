from unicodedata import normalize
from pathlib import Path
import json
if __name__ == "__main__":
    input_dict_unfiltered = {
            "name": input("Name: "),
            "url": input("URL? [empty for blank] "),
            "year": input("year? [empty for blank] "),
            "description": input("description? [empty for blank] ")
            }
    input_dict = {k:v for k,v in input_dict_unfiltered.items() if len(v) > 0}
    normalized_name = normalize('NFKD', input_dict["name"]).encode('ascii', 'ignore').decode('ascii').lower().split(" ")
    name_key = ".".join([normalized_name[-1]] + [part[0] for part in normalized_name[:-1]])

    data_file = Path("data/people.json")

    people_dict = json.loads(data_file.read_text())
    if name_key in people_dict.keys():
        name_key = name_key + "-1"
        while name_key in people_dict.keys():
            name_key = name_key[:-1] + str(int(name_key[-1])+1)

    print(f"\nGenerated key: '{name_key}'")
    people_dict[name_key] = input_dict
    with open(data_file, 'w', encoding='utf8') as json_file:
        json.dump(people_dict, json_file, sort_keys=True, indent=2, ensure_ascii=False)

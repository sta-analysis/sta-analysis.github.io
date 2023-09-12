# Analysis webpage
This is the repository for the [St Andrews Analysis Group website](https://sta-analysis.github.io).
Jump to:

- [Updating and deploying the site](#updating-and-deploying-the-site)
- [Editing content](#editing-content)


## Pulling Remote Updates
First, make sure you have [git](https://git-scm.com/) and [Zola](https://www.getzola.org/documentation/getting-started/installation/) installed.
Then clone this repository locally:
```sh
git clone https://github.com/sta-analysis/webpage && cd webpage
```
If the repository already exists, change to the directory and `git pull`.


## Building the site
This site is built using the [Zola static site generator](https://www.getzola.org).
In order to preview the site, run `zola serve`.
In order to build a local version of the site, run `zola build`.
Here, the `public` directory will contain the output site.

## Editing Content
### Updating members
The group member list is rendered as follows.
First, the data file `data/people.json` contains lookup information for the people.
The member lists are contained in `data/members.json`, which are lists of keys from the `data/people.json` file.
There are 5 lists:
- *staff* (for staff, which is rendered with titles and description, and sorted)
- *phd* (for PhD students, which is rendered with titles and description, and sorted)
- *rstaff* (for recent staff, which is rendered simply with the name)
- *rphd* (for recent PhD students, which is rendered with the name and the graduation year)
- *visitors* (for recent visitors, which is rendered with the name and dates of visit)

This page is generated from `content/members/_index.md` with the template `templates/members.html`.
This template uses the macro file found in `template/macros/format.html`.

In order to add new members and change the existing state, simply modify the `data/members.json`.
Ensure that the corresponding key can be found in the `data/people.json` file!

### Updating seminars
There are two seminar lists: the current seminars, and the seminar archive.
The `data/seminars.json` contains the list of seminars for the current semester, and the `data/archive.json` contains the historic lists of seminars.
The seminar list is generated from `content/seminars/_index.md` with the template `templates/seminars.html`.
The seminar list is generated from `content/archive/_index.md` with the template `templates/archive.html`.
Both of these templates use the macro file found in `template/macros/format.html`.

In order to add new talks, input the appropriate date key in `data/seminars.json`, along with the relevant information as it becomes available.
Possible keys include `name` (speaker name), `title` (title of the talk), `abstract` (abstract of the talk), and `video` (a URL for a recording of the talk).
You can use HTML inside the `abstract` entry, which will be rendered appropriately on the site.

After the semester is done, add the contents of the `data/seminars.json` as a sub-dictionary (with key that is the appropriate semester title) in `data/archive.json`.
In order to begin the next semester, make sure to update the semester title in `content/seminars/_index.md`.

In order to automate these steps, a [convenience script](/scripts/new_semester.py) has been prepared.
Simply run (with a somewhat up-to-date version of [Python 3](https://www.python.org/downloads/))
```sh
python3 scripts/new_semester.py
```
from the root of the directory.

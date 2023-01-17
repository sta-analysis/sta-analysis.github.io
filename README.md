# Analysis webpage
This is the repository for the [St Andrews Analysis Group website](http://www.mcs.st-andrews.ac.uk/~jmf32/analysis/index.html).
Jump to:

- [Updating and deploying the site](#updating-and-deploying-the-site)
- [Editing content](#editing-content)

This site is automatically built to a [preview page](https://analysis.rutar.org) hosted on my personal domain.

## Pulling Remote Updates
First, make sure you have [Zola](https://www.getzola.org/documentation/getting-started/installation/) and [fish](https://fishshell.com/) installed.
Then clone this repository locally:
```
git clone https://github.com/sta-analysis/webpage && cd webpage
```
If the repository already exists, change to the directory and `git pull`.
Make sure you have `ssh` access on the servers `analysis@twopi.mcs.st-andrews.ac.uk` and `jmf32@twopi.mcs.st-andrews.ac.uk`, or that you know the respective passwords.
Update as desired, and then run
```
fish build_mcs_site.fish
```
and the sites will be updated!


## Updating and deploying the site
### Accessing the server
The easiest way to access the server is to be logged in on eduroam, and to `ssh` into the server.
The address is `twopi.mcs.st-andrews.ac.uk` and the username is `analysis`.
For example, you can join with
```
ssh analysis@twopi.mcs.st-andrews.ac.uk
```
Ask someone in the group for the appropriate password.

### Building the webpage
This site is built using the [Zola static site generator](https://www.getzola.org).
In order to preview the site, run `zola serve`.
In order to build a local version of the site, run `zola build`.
Here, the `public` directory will contain the output site.

However, the file structure of this site does not align with the file structure used by MCS.
As a result, changing some links is required: in particular, all references to root `href="/..."` must be changed to `href="..."`, the directory structure must be flattened (e.g. `public/seminars/index.html` must be moved to `public/seminars.html`), and the respective links must be changed as well.

The script `build_mcs_site.fish` contains the details of how to do this.
In fact, this script contains some useful automation in order to
1. Build the site.
2. Update the contents of the site to align with MCS.
3. Upload the site to MCS at the `public` subdirectory.

If you have [fish](https://fishshell.com/) installed on your device, you can just run `fish build_mcs_site.fish` to do this.
Then, you can preview the site at [http://pi.mcs.st-andrews.ac.uk/pg/pure/Analysis/public/members.html](http://pi.mcs.st-andrews.ac.uk/pg/pure/Analysis/public/index.html).
In order to update the actual contents, simply `ssh` into the server and move the contents of the `public` folder to the main folder: for instance,
```
ssh analysis@twopi.mcs.st-andrews.ac.uk
cd ~/webpage
mv public/* .
```

## Editing Content
### Updating members
The group member list is rendered as follows.
First, the data file `data/people.json` contains lookup information for the people.
The member lists are contained in `data/members.json`, which are lists of keys from the `data/people.json` file.
There are 5 lists:
- *staff* (for staff, which is rendered with titles and description)
- *phd* (for PhD students, which is rendered with titles and description)
- *rstaff* (for recent staff, which is rendered simply with the name)
- *rphd* (for recent PhD students, which is rendered with the name and the graduation year)
- *visitors* (for recent visitors, which is rendered simply with the name)

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

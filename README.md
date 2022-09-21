# Analysis webpage
## Accessing the server
The easiest way to access the server is to be logged in on eduroam, and to `ssh` into the server.
The address is `twopi.mcs.st-andrews.ac.uk` and the username is `analysis`.
For example, you can join with
```
ssh analysis@twopi.mcs.st-andrews.ac.uk
```
Ask someone in the group for the appropriate password.

## Building the webpage
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

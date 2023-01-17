# build the directory
zola build

# remove folder nesting
for name in archive postgraduate seminars links research members summer
    mv public/$name/index.html public/$name.html
    rmdir public/$name
end

# remove 404 page (automatically served)
rm -f public/404.html

# rename internal links to respect folder structure
for name in archive postgraduate seminars links research members summer
    sed -i "s/\"\/$name\/\"/\"$name.html\"/g" public/*.html
end
sed -i "s/\"\/\"/\"index.html\"/g" public/*.html
sed -i 's/="\//="/g' public/*.html

# copy public directory remotely
rsync -a public analysis@twopi.mcs.st-andrews.ac.uk:webpage/
rsync -a public jmf32@twopi.mcs.st-andrews.ac.uk:public_html

# move files to correct locations
ssh analysis@twopi.mcs.st-andrews.ac.uk "mv ~/webpage/public/* ~/webpage/"
ssh analysis@twopi.mcs.st-andrews.ac.uk "rmdir ~/webpage/public"

# display update information
echo "Site updated at:"
echo "  http://www.mcs.st-andrews.ac.uk/pg/pure/Analysis/index.html"

zola build
for name in archive postgraduate seminars links research members summer
    mv public/$name/index.html public/$name.html
    rmdir public/$name
end
rm -f public/404.html
for name in archive postgraduate seminars links research members summer
    sed -i "s/\"\/$name\/\"/\"$name.html\"/g" public/*.html
end
sed -i "s/\"\/\"/\"index.html\"/g" public/*.html
sed -i 's/="\//="/g' public/*.html
rsync -a public analysis@twopi.mcs.st-andrews.ac.uk:webpage/

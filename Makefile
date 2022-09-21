.PHONY: upload

upload:
	zola build
	for name in archive postgraduate seminars links research members summer; do mv public/$$name/index.html public/$$name.html && rmdir public/$$name; done
	rm public/404.html
	rsync -a public analysis@twopi.mcs.st-andrews.ac.uk:old_webpage/

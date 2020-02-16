all: index.html
	
index.html: README.md ../../../includes/navigation.html
	pandoc -s README.md \
	       --template=Github.html5 \
	       -B ../../../includes/navigation.html \
	       -o index.html

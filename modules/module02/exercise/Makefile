all: index.html turtle.html
	
index.html: README.md ../../../includes/navigation.html
	pandoc -s README.md \
	       --template=Github.html5 \
	       -B ../../../includes/navigation.html \
	       -o index.html

turtle.html: turtle.md ../../../includes/navigation.html
	pandoc -s turtle.md \
	       -o turtle.html \
	       --template=Github.html5 \
	       -B ../../../includes/navigation.html

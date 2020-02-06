all: index.html style-guide.html style-guide.pdf

index.html: README.md
	pandoc README.md \
	    -o index.html \
	    -B ../includes/navigation.html \
	    --template=Github.html5

style-guide.html: style-guide.md
	pandoc style-guide.md -o index.html --standalone --template=Github.html5

style-guide.pdf: style-guide.md
	pandoc style-guide.md -o style-guide.pdf

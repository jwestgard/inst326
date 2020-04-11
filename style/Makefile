all: index guide pdf

index: README.md
	pandoc README.md \
	    -o index.html \
	    -B ../includes/navigation.html \
	    --template=Github.html5

guide: style-guide.md
	pandoc style-guide.md \
	    -o style-guide.html \
	    -B ../includes/navigation.html \
	    --template=Github.html5

pdf: style-guide.md
	pandoc style-guide.md -o style-guide.pdf

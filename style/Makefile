all: style-guide.html style-guide.pdf

index.html: style-guide.md
	pandoc style-guide.md -o index.html --standalone

style-guide.pdf: style-guide.md
	pandoc style-guide.md -o style-guide.pdf

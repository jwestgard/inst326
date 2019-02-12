all: style-guide.html style-guide.pdf

style-guide.html: style-guide.md
	pandoc style-guide.md -o style-guide.html --standalone

style-guide.pdf: style-guide.md
	pandoc style-guide.md -o style-guide.pdf

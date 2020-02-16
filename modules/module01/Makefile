all: index slides exercises_dir

index: README.md ../../includes/navigation.html
	pandoc -s README.md \
	       --template=Github.html5 \
	       -B ../../includes/navigation.html \
	       -o index.html

slides: slides.md
	pandoc --to revealjs --standalone --output slides.html slides.md
	pandoc --from markdown --to pptx --output slides.pptx slides.md

exercises_dir:
	cd exercises && $(MAKE)

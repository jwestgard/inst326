all: index slides exercises_dir 

index: README.md
	pandoc -s README.md \
	       -o index.html \
	       --template=Github.html5 \
	       -B ../../includes/navigation.html

slides: iteration.md functions.md
	pandoc --to revealjs --standalone --output functions.html functions.md
	pandoc --to pptx --output functions.pptx functions.md
	pandoc --to revealjs --standalone --output iteration.html iteration.md
	pandoc --to pptx --output iteration.pptx iteration.md

exercises_dir:
	cd exercises && $(MAKE)

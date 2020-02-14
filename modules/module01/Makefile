all: index.html slides.pptx exercise_dir

exercise_dir:
	cd exercises && $(MAKE)

index.html: slides.md
	pandoc --to revealjs --standalone --output index.html slides.md

slides.pptx: slides.md
	pandoc --from markdown -o slides.pptx slides.md

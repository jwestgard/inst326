all: index.html slides.pptx exercise.html

index.html: slides.md
	pandoc --to revealjs --standalone --output index.html slides.md

exercise.html: exercise.md
	pandoc exercise.md -o exercise.html --standalone

slides.pptx: slides.md
	pandoc --from markdown -o slides.pptx slides.md

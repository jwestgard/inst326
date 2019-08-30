all: index.html slides.pptx exercises.html

index.html: slides.md
	pandoc --to revealjs --standalone --output index.html slides.md

exercises.html: exercises.md
	pandoc exercises.md --o exercises.html --standalone

slides.pptx: slides.md
	pandoc --from markdown --to pptx --output slides.pptx slides.md

all: index.html slides.pptx

index.html: slides.md
	pandoc --to revealjs --standalone --output index.html slides.md

slides.pptx: slides.md
	pandoc --to pptx --output slides.pptx slides.md

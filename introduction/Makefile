all: index slides.pptx

index: slides.md
	pandoc --incremental --to revealjs --standalone --output index.html slides.md

slides.pptx: slides.md
	pandoc slides.md -o slides.pptx

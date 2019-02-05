all: index.html slides.pptx install.html install.docx

index.html: slides.md
	pandoc --to revealjs --standalone --output index.html slides.md

slides.pptx: slides.md
	pandoc --to pptx --output slides.pptx slides.md

install.html: install.md
	pandoc install.md --output install.html --standalone

install.docx: install.md
	pandoc install.md --output install.docx

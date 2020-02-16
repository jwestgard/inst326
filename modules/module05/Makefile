all: index exercise.html tutorial.html

index: slides.md
	pandoc --to revealjs --standalone --output index.html slides.md

exercise.html: exercise.md
	pandoc --output exercise.html --standalone exercise.md

tutorial.html: tutorial.md
	pandoc --output tutorial.html --standalone tutorial.md

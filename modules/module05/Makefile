all: readings.html index.html exercise.html

index.html: slides.md
	pandoc --to revealjs --standalone --output index.html slides.md
	
readings.html: readings.md
	pandoc --output readings.html --standalone readings.md

exercise.html: exercise.md
	pandoc --output exercise.html --standalone exercise.md

tutorial.html: tutorial.md
	pandoc --output tutorial.html --standalone tutorial.md

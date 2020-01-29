all: index.html readings.html exercise.html

index.html: modules_testing.md
	pandoc --to revealjs --standalone --output index.html modules_testing.md
	
readings.html: readings.md
	pandoc --output readings.html --standalone readings.md

exercise.html: exercise.md
	pandoc --output exercise.html --standalone exercise.md

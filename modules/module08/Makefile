all: index.html readings.html

index.html: modules_testing.md
	pandoc --to revealjs --standalone --output index.html modules_testing.md
	
readings.html: readings.md
	pandoc --output readings.html --standalone readings.md


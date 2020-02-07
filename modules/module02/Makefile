all: functions.html iteration.html readings.html exercise.html index.html turtle.html

functions.html: functions.md
	pandoc --to revealjs --standalone --output functions.html functions.md

functions.pptx: functions.md
	pandoc --to pptx --output functions.pptx functions.md

iteration.html: iteration.md
	pandoc --to revealjs --standalone --output iteration.html iteration.md

iteration.pptx: iteration.md
	pandoc --to pptx --output iteration.pptx iteration.md

readings.html: readings.md
	pandoc --output readings.html --standalone readings.md

exercise.html: exercise.md
	pandoc --output exercise.html --standalone exercise.md

index.html: index.md
	pandoc --output index.html --standalone index.md

turtle.html: turtle.md
	pandoc -s turtle.md \
	       -o turtle.html \
	       --template=Github.html5 \
	       -B ../../includes/navigation.html

all: index.html functions.html iteration.html readings.html exercise_dir 

index.html: index.md
	pandoc -s index.md \
	       -o index.html \
	       --template=Github.html5 \
	       -B ../../includes/navigation.html

functions.html: functions.md
	pandoc --to revealjs --standalone --output functions.html functions.md

functions.pptx: functions.md
	pandoc --to pptx --output functions.pptx functions.md

iteration.html: iteration.md
	pandoc --to revealjs --standalone --output iteration.html iteration.md

iteration.pptx: iteration.md
	pandoc --to pptx --output iteration.pptx iteration.md

readings.html: readings.md
	pandoc -s readings.md \
	       -o readings.html \
	       --template=Github.html5 \
	       -B ../../includes/navigation.html

exercise_dir:
	cd exercise && $(MAKE)

all: index.html slides.html slides.pptx readings.html exercise_dir

exercise_dir:
	cd exercise && $(MAKE)

index.html: README.md ../../includes/navigation.html
	pandoc -s README.md \
	       --template=Github.html5 \
	       -B ../../includes/navigation.html \
	       -o index.html

readings.html: readings.md ../../includes/navigation.html
	pandoc -s readings.md \
	       --template=Github.html5 \
	       -B ../../includes/navigation.html \
	       -o readings.html

slides.html: slides.md
	pandoc --to revealjs --standalone --output slides.html slides.md

slides.pptx: slides.md
	pandoc --from markdown --to pptx --output slides.pptx slides.md

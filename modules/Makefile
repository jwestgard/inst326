all: index intro modules

index: README.md
	pandoc -s README.md \
	       -o index.html \
	       --template=Github.html5 \
	       -B ../includes/navigation.html
	       
intro:
	cd introduction/ && $(MAKE)

modules:
	cd module01/ && $(MAKE)
	cd module02/ && $(MAKE)
	cd module03/ && $(MAKE)
	cd module04/ && $(MAKE)
	cd module05/ && $(MAKE)
	cd module06/ && $(MAKE)
	cd module07/ && $(MAKE)
	cd module08/ && $(MAKE)
	cd module09/ && $(MAKE)
	cd module10/ && $(MAKE)
	cd module11/ && $(MAKE)
	

all: index current

index: README.md
	pandoc -s README.md \
	       -o index.html \
	       --template=Github.html5 \
	       -B ../includes/navigation.html

current: sp2020-101.tex
	pdflatex sp2020-101.tex > /dev/null
	rm *.out *.log *.aux

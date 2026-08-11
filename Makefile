.PHONY: install test verify verify-three verify-seven paper

install:
	python3 -m pip install --upgrade pip
	python3 -m pip install -e .

test:
	python3 -m unittest discover -s tests -v

verify: verify-three verify-seven

verify-three:
	python3 -m zeta_simple_zeros three

verify-seven:
	python3 -m zeta_simple_zeros seven

paper:
	tectonic --outdir paper paper/riemann.tex

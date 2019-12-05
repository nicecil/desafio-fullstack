.PHONY: tests install

tests:
	@python -m pytest -v -s tests

install:
	@pip install -r requirements.txt
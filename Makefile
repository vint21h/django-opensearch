# django-opensearch
# Makefile


.ONESHELL:
PHONY: tox test twine-check twine-upload help
TEST_PYPI_URL=https://test.pypi.org/legacy/

tox:
	tox;\

test:
	./manage.py test $(TESTS);\

twine-check:
	python setup.py bdist_wheel sdist;\
	twine check dist/*;\
	twine upload -s --repository-url $(TEST_PYPI_URL) dist/*;\

twine-upload:
	twine upload -s dist/*;\

help:
	@echo "    tox:"
	@echo "        Run tox."
	@echo "    test:"
	@echo "        Run tests, can specify tests with 'TESTS' variable."
	@echo "    twine-check:"
	@echo "        Run some twine checks."
	@echo "    twine-upload:"
	@echo "        Uload package to PyPi using twine."

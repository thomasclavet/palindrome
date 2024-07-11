INSTALL_STAMP := .install.stamp
POETRY := $(shell command -v poetry 2> /dev/null)

install: $(INSTALL_STAMP)
$(INSTALL_STAMP): pyproject.toml poetry.lock
	@if [ -z $(POETRY) ]; then echo "Poetry could not be found. See https://python-poetry.org/docs/"; exit 2; fi
	$(POETRY) install
	touch $(INSTALL_STAMP)

.PHONY: run
run: $(INSTALL_STAMP)
	$(POETRY) run python palindrome.py "$(PHRASE)"

.PHONY: format
format: $(INSTALL_STAMP)
	$(POETRY) run ruff check --fix
	$(POETRY) run ruff format


.PHONY: test
test: $(INSTALL_STAMP)
	$(POETRY) run pytest -v tests/ 


.PHONY: clean
clean:
	find . -type d -name "__pycache__" | xargs rm -rf {};
	rm -rf $(INSTALL_STAMP) .coverage .mypy_cache .pytest_cache
VENV = venv
PYTHON = $(VENV)/bin/python3

run: $(VENV)/bin/activate
	$(PYTHON) src/main.py $(FILE)

$(VENV)/bin/activate:
	python3 -m venv $(VENV)

clean:
	rm -rf __pycache__
	rm -rf $(VENV)

.PHONY: run clean
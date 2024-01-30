.PHONY: all install clean

all: install

install: venv

venv: requirements.txt
	python3 -m venv venv
	if [ ! -d ~/.local/bin ]; then mkdir -p ~/.local/bin; fi
	ln -s $(realpath co-calculator) ~/.local/bin/co-calculator
	. ./venv/bin/activate
	venv/bin/pip install -r requirements.txt

	@echo "Install complete"

clean:
	rm -rf venv ~/.local/bin/co-calculator
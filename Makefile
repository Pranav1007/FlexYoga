.PHONY: clean install run all system-packages python-packages

system-packages:
	sudo apt install python3-pip -y

python-packages:
	pip3 install -r requirements.txt

install: system-packages python-packages

run:
	export FLASK_APP=app.py
	flask run

all: install run

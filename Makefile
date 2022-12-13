.PHONY: clean install debug run all system-packages python-packages

system-packages:
	sudo apt install python3-pip -y

python-packages:
	pip3 install -r requirements.txt

install: system-packages python-packages

debug:
	export FLASK_APP=app.py
	export FLASK_DEBUG=1
	export FLASK_ENV=development
	flask run

run:
	export FLASK_APP=app.py
	flask run

all:
	install run

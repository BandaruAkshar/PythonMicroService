install:
	#install commands
	pip install --upgrade pip &&\
		pip install -r requirements.txt
lint:
	#flake8 or #pylit
	pylint --disable=R,C *.py mylib/*.py
format:
	#format commands
	black *.py mylib/*.py
test:
	#test commands
deploy:
	#deploy commands

all: install lint test deploy
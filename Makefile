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
	python -m pytest -vv --cov=mylib --cov=main test_*.py

build:
	#build container
	docker build -t deploy-fastapi .
run: 
	#run docker
	docker run -p 127.0.0.1:8080:8080 846b4df56a8f
deploy:
	#deploy commands

all: install lint test deploy
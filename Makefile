install:
		pip install --upgrade pip &&\
			pip install -r requirements.txt
lint:
	pylint --disable=R,C *.py devopslib fastapilib
test:
	python -m pytest -vv --cov=devopslib test_*.py
format:
	black *.py devopslib/*.py fastapilib/*.py
deploy:
	echo "Deploy goes here"

all: install lint test format deploy
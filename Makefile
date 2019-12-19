# File:    Makefile
# Author:  Olga Joloud 
# Purpose: run simple python3 selenium automation
all: lint unit 

setup:
	@echo "Starting setup"
	python3 -m pip install -r requirements.txt

lint:	
	@echo "Starting lint"
	find . -name "*.py" | xargs pylint
	
unit:
	@echo "Starting unit test"
	python3 product_tests.py  

.env:
	docker build -t tdd:python .
	touch .env

test: .env
	docker run --rm -it -v ${PWD}:/app -w /app tdd:python python xunit.py

mypy: .env
	docker run --rm -it -v ${PWD}:/app -w /app tdd:python mypy --strict *.py 

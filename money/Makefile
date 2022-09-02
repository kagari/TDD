.env:
	docker build -t tdd:python .
	touch .env

test: .env
	docker run --rm -it -v ${PWD}:/app -w /app tdd:python python money_test.py -v

mypy: .env
	docker run --rm -it -v ${PWD}:/app -w /app tdd:python mypy --strict *.py 

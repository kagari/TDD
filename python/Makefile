.env:
	docker build -t tdd:python .
	touch .env

test: .env
	docker run --rm -it -v ${PWD}:/app -w /app tdd:python3 mypy --strict money.py

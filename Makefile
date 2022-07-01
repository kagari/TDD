run:
	docker run --rm -v $$PWD:/app -w /app -it golang:1.18 go run main.go

test:
	docker run --rm -v $$PWD:/app -w /app/money -it golang:1.18 go test -v
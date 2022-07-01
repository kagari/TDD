run:
	docker run --rm -v $$PWD:/app -w /app -it golang:1.18 go run main.go
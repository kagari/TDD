setup:
	docker volume create tdd_go

run:
	docker run --rm -v $$PWD:/app- v tdd_go:/go -w /app -it golang:1.18 go run main.go

test:
	docker run --rm -v $$PWD:/app -v tdd_go:/go -w /app/money -it golang:1.18 go test -v

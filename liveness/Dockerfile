FROM golang:1.8

WORKDIR /go/src/liveness
COPY server.go .

RUN go get -d -v ./...
RUN go install -v ./...
RUN go build

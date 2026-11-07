FROM golang:1.21
WORKDIR /app
COPY main.go .
RUN go build -o main main.go
EXPOSE 8080
CMD [ "./main" ]

# you got this all except 1 its /app not app/ and to run go app just pass the file name as did in CMD
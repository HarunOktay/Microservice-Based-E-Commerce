FROM golang:1.21-alpine

WORKDIR /app

# git ekle
RUN apk add --no-cache git

COPY . .

# Önce go get çalıştır
RUN go get github.com/gin-gonic/gin
RUN go build -o main .

EXPOSE 8002

CMD ["./main"] 
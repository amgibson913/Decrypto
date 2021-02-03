git pull

docker stop frontend
docker stop backend

docker build -t decryptofrontend:latest ./frontend
docker build -t decryptobackend:latest ./backend

docker run --name backend -d -p 5000:5000 --rm decryptobackend:latest
docker run --name frontend -d -p 8080:80 --rm decryptofrontend:latest
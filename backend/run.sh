cd backend
docker build -t url-checker .
docker run -it --rm -p 8080:8080 url-checker

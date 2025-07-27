# Image Converter

- Local Commands:
```
uvicorn app.main:app --reload
pytest --pylint --cov
```

- Docker Commands:
```
docker compose up --build -d
docker compose exec fastapi uvicorn app.main:app
docker compose exec fastapi pytest --pylint --cov
docker compose down
```

- View the Application Image Converter HTML Page in a Web Browser:
```
localhost:8000
```

- View the Application Routes in a Web Browser:
```
localhost:8000/docs
```

- Terminate the Application from the Terminal:
```
Type Control-C (^C)
```

### [DockerHub Repository](https://hub.docker.com/r/joec11/image-converter)

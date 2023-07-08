# brainbrew-backend

[![Pylint](https://github.com/bitemedicine/brainbrew-backend/actions/workflows/pylint.yml/badge.svg)](https://github.com/bitemedicine/brainbrew-backend/actions/workflows/pylint.yml)  

You can execute the following commands to start web server in your local machine.

Standalone Installation
```bash
pip3 install -r requirements.txt
uvicorn main:app --reload
```

Docker Build
```bash
docker build -t brainbrew-backend .
```

Docker Installation
```bash
docker run -e OPENAI_API_KEY='<YOUR_OPENAI_API_KEY>' -e MONGO_CONNECTION_STRING='<YOUR_MONGO_CONNECTION_STRING>' -p 8000:80 brainbrew-backend
```
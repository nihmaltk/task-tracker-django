## Task Tracker – Django + Docker Application

A lightweight Django application with three simple pages (Home, Tasks, About) fully containerized using Docker.
This project is designed for learning how to run Python web applications inside Docker.

## Features

- Simple Django app with three pages
- Fully containerized using Docker
- Reproducible environment
- Easy to run on any system

## Technologies used

- Python
- Django
- Docker Engine
- Git

## Prerequisites

Make sure Docker is installed on your system.

## Run the App Using Docker

1. **Clone the Repository**
```bash
git clone https://github.com/nihmaltk/task-tracker-django.git
cd task-tracker-django
```

2. **Build the Docker Image**
```bash
docker build -t task-tracker-app .
```

3. **Run the Container**
```bash
docker run -p 8000:8000 task-tracker-app
```

4. **Access the application at**:

- **Home**: `http://localhost:8000/`
- **Tasks**: `http://localhost:8000/tasks/`
- **About**: `http://localhost:8000/about/`

5. **Stop the Container**

Press `CTRL + C` in the terminal.

## Essential Docker Commands

```bash
# List images
docker images
```
```bash
# List running containers
docker ps
```
```bash
# List all containers (running + stopped)
docker ps -a
```
```bash
# Stop a running container
docker stop <container-id>
```
```bash
# Remove a stopped container
docker rm <container-id>
```
```bash
# Remove all stopped containers
docker rm $(docker ps -aq)
```
```bash
# Remove an image
docker rmi task-tracker-app
```
```bash
# View logs of a container
docker logs <container-id>
```

## Key Concepts

This project demonstrates:

- Basic Django project structure
- How to containerize Python apps
- Running Django inside a Docker container
- Port mapping and image building


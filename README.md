## Task Tracker – Django + Docker Application

A lightweight Django application with three simple pages (Home, Tasks, About) fully containerized using Docker.
This project is designed for learning how to run Python web applications inside Docker.

## Features

* Simple Django application with three pages (`/`, `/tasks/`, `/about/`).
* **Fully containerized** using Docker for a reproducible environment.
* Easy to run on any system that supports Docker.

## Technologies used

- **Python**
- **Django**
- **Docker Engine**
- **Git**

## Prerequisites

Make sure **Docker Engine** is installed and running on your system.

## Run the App Using Docker

1. **Clone the Repository**
```bash
git clone https://github.com/nihmaltk/task-tracker-django.git
cd task-tracker-django
```

2. **Build the Docker Image**

This command reads the `Dockerfile` to create the container image named `task-tracker-app`.
```bash
docker build -t task-tracker-app .
```

3. **Run the Container**

This command starts the container and maps the host port **8000** to the container's exposed port **8000**.
```bash
docker run -d -p 8000:8000 --name django-task-tracker task-tracker-app
```

4. **Access the application**

Open your browser and navigate to:

- Home: **`http://localhost:8000/`**
- Tasks: **`http://localhost:8000/tasks/`**
- About: **`http://localhost:8000/about/`**

## Essential Docker Commands

| Command | Purpose |
| :--- | :--- |
| `docker ps` | List **running** containers. |
| `docker stop django-task-tracker` | Stop the running container using its assigned name. |
| `docker rm django-task-tracker` | Remove the stopped container. |
| `docker rmi task-tracker-app` | Remove the local Docker image. |
| `docker logs django-task-tracker` | View the application's output logs. |
| `docker ps -a` | List **all** containers (running + stopped). |

## Key Concepts

This project demonstrates:

* **Containerization:** Running a Python web app in an isolated environment.
* **Port Mapping:** Connecting the host network to the container (`-p 8000:8000`).
* **`Dockerfile`:** Contains the instructions for building the reproducible image (defines Python version, installs dependencies, runs the app).
* **Basic Django Project Structure:** The minimal files needed to run a Django application.


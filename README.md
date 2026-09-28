# Docker Flask PostgreSQL

A containerised Flask application connected to PostgreSQL and served through Nginx using Docker Compose.

This project was built as part of my DevOps home lab to practise Docker, container networking, environment variables, volumes, healthchecks, multi-stage Docker builds and application logging.

## Architecture

```text
                    ┌──────────────┐
                    │    Nginx     │
                    │   Port 8090  │
                    └──────┬───────┘
                           │
                           ▼
                    ┌──────────────┐
                    │    Flask     │
                    │   Port 5000  │
                    └──────┬───────┘
                           │
                           ▼
                    ┌──────────────┐
                    │  PostgreSQL  │
                    │     5432     │
                    └──────────────┘
```

Nginx acts as a reverse proxy to the Flask application. Flask connects to PostgreSQL using the Docker Compose service name `databases`.

## Project Structure

```text
docker-flask-postgres/
├── app/
│   ├── app.py
│   ├── Dockerfile
│   └── requirements.txt
├── compose.yaml
├── index.html
├── nginx.conf
└── .gitignore
```

## Technologies

* Docker
* Docker Compose
* Python 3.12
* Flask
* PostgreSQL 16
* Nginx
* Linux

## Running the Project

Create a `.env` file in the project root containing the required environment variables:

```env
APP_ENV=development
POSTGRES_PASSWORD=your_password
POSTGRES_DB=appdb
POSTGRES_USER=appuser
```

Start the services:

```bash
docker compose up -d
```

Check the containers:

```bash
docker compose ps
```

The application can then be accessed through:

```text
http://localhost:8090
```

The Flask application can also be accessed directly:

```text
http://localhost:5000
```

## Docker Features Practised

### Docker Compose

The application consists of three services:

* `web` — Nginx
* `app` — Flask
* `databases` — PostgreSQL

Docker Compose provides the network between the containers and allows services to communicate using their service names.

### Environment Variables

Database configuration is passed to the containers using environment variables.

The `.env` file is excluded from Git using `.gitignore`.

### Healthchecks

PostgreSQL uses `pg_isready` to verify that the database is accepting connections.

Flask exposes a `/health` endpoint which is used by its Docker healthcheck.

The startup dependency chain is:

```text
PostgreSQL healthy
       ↓
Flask healthy
       ↓
Nginx
```

### Volumes

Docker volumes were used to practise persistent PostgreSQL data storage.

Bind mounts were also used during development for files such as the Nginx configuration and HTML page.

### Multi-stage Docker Builds

A multi-stage Dockerfile was created and tested to practise separating the build stage from the runtime stage.

The final runtime image copies only the required application and Python virtual environment from the builder stage.

### Logging

The Flask application uses Python's built-in logging module.

Example:

```python
logger.info("Connecting to PostgreSQL")
logger.error(f"Database connection failed: {e}")
```

Application logs can be viewed with:

```bash
docker compose logs app
```

Both successful database connections and simulated database connection failures were tested.

## Learning Outcomes

This project provided hands-on practice with:

* Building Docker images
* Writing Dockerfiles
* Multi-stage builds
* Docker Compose
* Container networking and service discovery
* Environment variables
* Docker volumes and bind mounts
* PostgreSQL containers
* Container healthchecks
* Reverse proxying with Nginx
* Application logging
* Git and GitHub workflow

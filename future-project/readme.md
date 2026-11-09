Task Explanation
This challenge focuses on two major production-grade features: BuildKit Cache Mounts for optimizing build speeds and Native Healthchecks for runtime monitoring.

1. BuildKit Cache Mounts (--mount=type=cache)
By default, Docker treats every build step in isolation and throws away internal caches (like pip's download cache) once a RUN instruction finishes. If you change a single line of code and rebuild, Docker has to re-download every single Python package from scratch, wasting valuable CI/CD minutes and bandwidth.

A cache mount tells Docker to save a specific directory (like /root/.cache/pip) on your host machine across builds. When you run pip install again, it instantly detects the cached wheels and installs them locally without downloading them again, all without bloating your final image size.

2. Native Healthchecks (HEALTHCHECK)
In production, a container running doesn't necessarily mean your app is healthy. The web server process might be running, but it could be frozen in a deadlock or throwing unhandled errors.

The HEALTHCHECK instruction tells Docker (or orchestrators like Docker Compose and Kubernetes) to periodically execute a test command inside the container (like sending a curl request to your endpoint). If the command fails repeatedly, Docker marks the container as "unhealthy," allowing automated systems to take action or alert you.

The Solution
To make this work in a slim Python image, we also need to install curl so the healthcheck command has a tool to query the endpoint.

Dockerfile
FROM python:3.9-slim

WORKDIR /app

# Install curl (required so the HEALTHCHECK command can make HTTP requests)
RUN apt-get update && apt-get install -y curl && rm -rf /var/lib/apt/lists/*

COPY requirements.txt .

# Use a BuildKit cache mount to persist pip packages across builds
RUN --mount=type=cache,target=/root/.cache/pip \
    pip install --no-cache-dir -r requirements.txt

COPY . .

EXPOSE 5000

# Periodically test if the app is responsive every 30 seconds
HEALTHCHECK --interval=30s --timeout=3s --start-period=5s --retries=3 \
  CMD curl --fail http://localhost:5000/ || exit 1

CMD ["python3", "app.py"]
Important Note for Building:
Because cache mounts rely on Docker's modern BuildKit engine, you build this image using standard BuildKit syntax by prepending DOCKER_BUILDKIT=1 (though BuildKit is enabled by default in modern Docker versions):

Bash
docker build -t advanced-app .
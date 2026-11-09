Challenge 1: Production Security Hardening (Non-Root User)
By default, Docker containers run as the root user. If an attacker manages to exploit a vulnerability in your web application, they instantly get root access inside the container. Securing an image means creating a dedicated, low-privilege system user and transferring ownership of the application files.

Create a project folder named secure-app.

Create a simple app.py (a basic Flask app on port 5000).

Your Task: Write a Dockerfile that meets these production security rules:

Use a slim Python base image.

Create a dedicated system user and group (e.g., named appuser).

Set up the working directory and copy files with correct permissions so appuser can read/execute them.

Switch to that user using the USER instruction before running CMD.

The Validation Test: When you run the container, run docker exec -it <container-id> whoami. It should output appuser, not root.
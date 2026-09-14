# Distinction Web App - SWE40006 Task 4.3

A simple Flask web application containerized with Docker, built for the
Software Deployment and Evolution unit assessment.

## Run locally
docker build -t distinction-webapp .
docker run -p 5000:5000 distinction-webapp

Visit http://localhost:5000
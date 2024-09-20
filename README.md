Dockerized Django App

This repository contains a Django application containerized using Docker. Follow the steps below to build and run the app inside a Docker container.
Prerequisites

Before you begin, ensure you have the following installed on your machine:

    Docker (Install Docker Desktop for your operating system)

Steps to Run the App
1. Clone the Repository

bash

git clone https://github.com/tigerkitty78/intern
cd yourrepository

2. Build the Docker Image

In the project directory, run the following command to build the Docker image:

docker build -t mydjangoapp .

3. Run the Docker Container

Once the image is built, run the following command to start the container:

docker run -d -p 8000:8000 mydjangoapp

This command runs the app in detached mode and maps the container's port 8000 to your local machine's port 8000.
4. Access the App

Open your web browser and go to:

http://localhost:8000

You should see my Django app running.
5. Stop the Container

To stop the running container, first find the container ID using:

docker ps
Then stop it with
docker stop <container_id>

Useful Docker Commands

    List running containers: docker ps
    List all containers (including stopped): docker ps -a
    View images: docker images
    Remove a container: docker rm <container_id>
    Remove an image: docker rmi <image_id>

#!/bin/bash

# Launches a Docker container in a separate terminal with Terminator

# Set the container name
container_name="serverconatiner2"

# Set the Docker image name and tag
docker_image="simage"


# Create the final command to launch the container in a separate terminal with Terminator
command="terminator -e 'docker run --rm --name $container_name --net servernet $docker_image'"

# Launch the command in a separate terminal with Terminator
eval "$command"

#!/bin/bash

CONTAINER_NAME="review_scraper_container"
IMAGE_NAME="review-scraper"

# Run the Docker container
sudo docker run --name $CONTAINER_NAME $IMAGE_NAME

# Wait for the container to stop
while [ "$(sudo docker inspect -f '{{.State.Running}}' $CONTAINER_NAME)" == "true" ]; do
    sleep 10
done

# Copy files from the container to the host
sudo docker cp $CONTAINER_NAME:/usr/src/app/google_play_reviews.csv .
sudo docker cp $CONTAINER_NAME:/usr/src/app/apple_app_store_reviews.csv .

# Optionally remove the container
sudo docker rm $CONTAINER_NAME

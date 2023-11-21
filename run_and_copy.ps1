# PowerShell script

$CONTAINER_NAME = "review_scraper_container"
$IMAGE_NAME = "review-scraper"

# Run the Docker container
docker run --name $CONTAINER_NAME $IMAGE_NAME

# Wait for the container to stop
while ((docker inspect -f '{{.State.Running}}' $CONTAINER_NAME) -eq "true") {
    Start-Sleep -Seconds 10
}

# Copy files from the container to the host
docker cp "${CONTAINER_NAME}:/usr/src/app/google_play_reviews.csv" "."
docker cp "${CONTAINER_NAME}:/usr/src/app/apple_app_store_reviews.csv" "."

# Optionally remove the container
docker rm $CONTAINER_NAME
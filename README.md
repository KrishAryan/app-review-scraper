# App Review Scraper

## Overview
This project consists of a Python script designed to scrape reviews from the Google Play Store and Apple App Store. The reviews are saved into CSV files for further analysis or record-keeping. The entire application is Dockerized for ease of deployment and execution.

## Prerequisites
- Docker
- Python (if running locally)

## Installation
1. **Clone the Repository**
```
git clone https://github.com/KrishAryan/app-review-scraper.git
```
2. **Building the Docker Image**
```
docker build -t review-scraper .
```

## Usage

This project includes automated scripts for both Linux/macOS (Bash script) and Windows (PowerShell script) environments. These scripts handle the process of running the Docker container, waiting for it to complete its task, and then copying the output CSV files to a specified location on the host machine.

### Running on Linux/macOS

1. **Ensure the Bash script is executable**:
```
chmod +x run_and_copy.sh
```
2. **Run the script**
  ```
  ./run_and_copy.sh
  ```
### Running on Windows

1. Open PowerShell and navigate to the directory containing the script.
2. **Execute the PowerShell script:**
```
.\RunAndCopy.ps1
```

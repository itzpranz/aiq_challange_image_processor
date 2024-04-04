# Image Processing Challenge

This project is a solution to an image processing challenge. It involves resizing images, storing them in a database, and providing an API to request image frames based on depth. The solution is implemented in Python and is containerized using Docker.

## Requirements

- Python 3.8+
- Docker
- Docker Compose

## Installation

1. Clone the repository:
    ```bash
    git clone https://github.com/itzpranz/aiq_challange_image_processor.git
    cd yourrepository
    ```

2. Build the Docker image:
    ```bash
    docker-compose build
    ```

## Running the Application

1. Start the Docker container:
    ```bash
    docker-compose up
    ```

The application will be accessible at `localhost:8000` on your machine.

## API Usage

The API endpoint to request image frames is:

`http://localhost:8000/api/frames?depth_min=<DEPTH_MIN>&depth_max=<DEPTH_MAX>`

Replace `<DEPTH_MIN>` and `<DEPTH_MAX>` with the desired depth values.


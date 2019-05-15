# Request-maker
A small Python program that makes a request to a web-service every second

## How to run?
Use the following command to run this container:

    docker run --name req -d dadvisor/req:latest
    
Or build from source:

    docker build -t req .
    docker run --name req -d req
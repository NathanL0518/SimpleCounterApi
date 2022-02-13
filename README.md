# Simple Online Game/Website User Counter API (Python / Flask)

## Pre-requisites
  * [Python](https://www.python.org/)
  * Install flask:

    ```bash
    pip install --no-cache-dir -r requirements.txt
    ```

## Running the web server

From the command line start the server with the following command:

  ```bash
  python server.py
  ```

Use Postman, CURL, or other program to call the following functions:

  * GET - [http://127.0.0.1:8088/hw1_api/getNumPeople](http://127.0.0.1:8088/hw1_api/getNumPeople)
    * getNumPeople - will return the number of people that is currently online
  * GET - [http://127.0.0.1:8081/hw1_api/getLog](http://127.0.0.1:8081/hw1_api/getLog)
    * getLog - will return a log with user's log in/out activities in a chronological order
  * GET - [http://127.0.0.1:8081/hw1_api/getUserList](http://127.0.0.1:8081/hw1_api/getUserList)
    * getUserList - will return a list of names of the users that are currently online
  * POST - [http://127.0.0.1:8081/hw1_api/login](http://127.0.0.1:8081/hw1_api/login)
    *login - login with your username as "username": "YOUR_USERNAME" and the method will increments the number of people online and add your name into the user list and log it
  * POST - [http://127.0.0.1:8081/hw1_api/logout](http://127.0.0.1:8081/hw1_api/logout)
    **logout - logout with your username as "username": "YOUR_USERNAME" and the method will decrements the number of people online and delete your name from the user list and log it

## Running via Docker

  1. Build the image:

    ```bash
    docker build -t hw1_api .
    ```

  2. Run the image:

    ```bash
    docker run -p 127.0.0.1:8088:8088 -it hw1_api
    ```

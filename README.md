# chpr-plot-service

## 1 Introduction
This project contains source code for a CHPR plotting application for Abbot. This document contains high-level information about this repository as well as set-up and run instructions.

### 1.1 Tech Stack

#### Core

- Python 
- Docker (infrastructure and containerization)
- Django (web framework)
- Postgresql (database)  

#### Secondary

- Pandas (data manipulation)
- Pygal  (plotting)

## 2 Set Up

1. Clone this repository

2. Set up Docker

    Mac: https://docs.docker.com/docker-for-mac/install/

    PC: https://docs.docker.com/toolbox/toolbox_install_windows/

3. Build container

    Startup a terminal (Mac) or the docker-toolbox shell (PC), and type in the following commands:

    ```
    docker-compose build
    ```

4. Give Executing Permissions to Critical Scripts
   
    ```
    sudo chmod +x docker-entrypoint.sh
    sudo chmod +x start_dev_docker
    ```

## 3 Run

Once the container is built, you may run with two methods:

For production and full integration testing:

```
docker-compose up
```

For development and debugging:

```
./start_dev_docker
```

You may now go to http://localhost:8000 with your browser to see the site.

## 3.1 Quitting

Use Ctrl+C to quit the running server. You may also need to run:

```
docker-compose down
```

To ensure that containers have shut down properly.

## 4 Annotated Layout
```
.
├── Dockerfile <- setup file used during Docker image initialization
├── README.md <- this file
├── docker-compose.yml <- setup file used during Docker image initialization
├── docker-entrypoint.sh <- file run to start the server
├── internal <- internal source folder containing most of the logic
│   ├── admin.py <- code to register models in admin panel
│   ├── apps.py
│   ├── charts.py <- Classes for PyGal Charts
│   ├── migrations <- folder containing database migration files
│   │   ├── ...
│   ├── models.py <- Classes specifying the data model
│   ├── process.py <- functions containing functions to process data
│   ├── templates <- folder containing html files
│   │   ├── base.html
│   │   ├── data.html
│   │   ├── home.html
│   │   └── login.html
│   ├── tests.py
│   ├── urls.py <- file specifying endpoint URLs and associated views
│   ├── validation.py <- file specifying file validation
│   └── views.py <- functions that define the main server logic
├── manage.py <- main entry point for django server
├── plot_service <- folder containing media files and configurations
│   ├── media
│   │   ├── processed <- folder for processed data
│   │   │   ├── ...
│   │   └── uploads <- folder for raw data
│   │       ├── ...
│   ├── settings.py <- site-wide configuration values
│   ├── urls.py <- top level endpoint specification
│   └── wsgi.py <- wsgi server configuration
├── requirements.txt <- requirements file specifying all python dependencies
├── start_dev_docker <- script to start terminal pointed at backend, not master
└── static <- static css files
    └── css 
        └── style.css

28 directories, 179 files
```

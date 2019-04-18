# chpr-plot-service

# 1 Introduction
This project contains source code for a CHPR plotting application.

# 2 Annotated Layout
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
├── static <- static css files
    └── css 
        └── style.css

28 directories, 179 files

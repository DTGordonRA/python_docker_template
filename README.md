# README #

### What is this: ###

* Template for pycharm/python projects with Dockerfile and docker-compose

### Environment Variables ###

* Environment variables can be set in the env-var/prod file.
    Format in env-var/prod: export NAME:VALUE
    The file used can be changed in the Dockerfile line 4 for testing purposes

### Venv Setup ###

* ONLY NEEDED FOR DEV, if this is simply going to be deployed skip to Docker Setup
* Branches based on OS below in single # #

# Mac/Linux #
* Enter Command: python -m venv env
* Enter Command: source env/bin/activate
* Install all required modules: pip install {module-name}
* In root folder with venv active Enter Command: pip freeze > requirements.txt
* When done the venv can be deactivated with the command: deactivate
# Windows #
* Enter Command: python -m venv env
* Enter Command: env\Scripts\activate.bat
* Install all required modules: pip install {module-name}
* In root folder with venv active Enter Command: pip freeze > requirements.txt
* When done the venv can be deactivated with the command: deactivate

### Docker Setup ###

* Rename the root folder and "_NAME_" in docker-compose, this will be the name of the image created: "root_folder_name"_"_NAME_"
* Enter command: docker-compose up --build
    Note: Any changes will require this command to be rerun
    If the image is simply being rerun rather than rebuilt enter: docker-compose up
* By default this will build the docker image and then run app/run.sh which will call run.py

### Output Files ###

* Add files as needed to this or have your script generate them.
* Any output files can be accessed as "output/{path/to/file}"
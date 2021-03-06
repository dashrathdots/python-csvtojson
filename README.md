# csv-to-json
Convert Csv to Json

### Pre requisites
- `git` protocol client installed
- Repository management client like `SourceTree` or something that helps in the `git` workflow
- Docker desktop

### Project checkout flow
Clone the entire repository on your local machine using the command

git clone https://github.com/dashrathdots/python-csvtojson.git


Say the above is cloned out in a folder say `python-csvtojson`.
Execute the following command to go in the checked out project folder

cd python-csvtojson


Checkout to the Beginner branch

git checkout Beginner


After the above, open the `python-csvtojson` folder in any IDE of your choice (preferable to use Visual Studio Code).
It has one folder
- python-csvtojson: Holds the complete code
- csvtojson: The django based project. This project will read the csv file and create new json file according to nested data.


## Create virtual environment
Create virtual environment.

https://docs.python.org/3/library/venv.html

## Activate your virtual environment by running this command

source venv/bin/activate

### Install new pip module and runserver

pip install -r requirements.txt

python manage.py runserver
- Hit the below url and upload the csv file to convert nested json .
```
http://127.0.0.1:8000/upload/csv

Once you upload the file, system will parse it and JSON file will be downloaded automatically in your browser
```

## Run Unit Test Case
python manage.py test


## Run the project with Docker
  - Build the `development` version server docker image and run it using the following command
    ```
      sudo docker-compose -f docker-compose.yml up
    ```
  - In order to see the start up logs execute the following command
    ```
      sudo docker-compose -f docker-compose.yml logs -f
    ```
  - In order to get the server docker image details, execute the following command
    ```
    sudo docker ps
    ```

  - The development docker image runs the django application using `python manage.py runserver`. So any change made in the project will auto redeploy it in the running docker image

## Run Unit Test Case inside the docker
  - sudo docker-compose -f docker-compose.yml exec csvtojson python manage.py test


## CI/CD with Github and Heroku

  - Setup up work flow from github action
    https://github.com/dashrathdots/python-csvtojson/actions/new
    It will automatic create .yml file where we need to update server related configurations

  - Go to the heroku cloud (https://dashboard.heroku.com/)
    - Create new app (https://dashboard.heroku.com/apps) python-csvtojson
    - Generate new API Key (https://dashboard.heroku.com/account)

  - Go to the Github repository
    - Go to the setting (https://github.com/dashrathdots/python-csvtojson/settings)
    - Add new secret (https://github.com/dashrathdots/python-csvtojson/settings/secrets/actions/new)
      - HEROKU_API_TOKEN
      - HEROKU_APP_NAME
  - Web access from here (https://python-csvtojson.herokuapp.com/)

## CI/CD work flow
  - Set up job
    - Ii will setup the job to build the project
  - Run actions/checkout@v2
    - This action checks-out your repository under $GITHUB_WORKSPACE , so your workflow can access it.
  - Run fetch --prune --unshallow
    - It will convert the shallow clone to the regular one.
  - Run Install Dependencies
    - It will install all the dependencies
  - Run Tests
    - It will run all the test cases which is created into the app.
  - Deploy to Heroku
    - If test case status will success
      - This action will deploy project into the Heroku
  - Post action actions/checkout@v2
  - Complete job


## Third party library for UI
  - Bootstrap 4.5.2
  - Jquery 3.5.1



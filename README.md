# csv-to-json
Convert Csv to Json


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
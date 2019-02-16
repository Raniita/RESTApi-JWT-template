# RESTApi-JWT-template
## Working with virtualenvs
First create a directory for ur environment
```
mkdir myenvironment/
```

For create a virtualenv
```
virtualenv myenvironment/myapp
```

Activate the environment
```
source myenvironment/myapp/bin/activate
```

## Setting up dependencies
```
pip install -r requirements.txt 
```

## Some configurations
Go to ``` app/config.py ``` and edit with ur info

## Setting up the database
Initiate a migration folder
```
python manage.py db init
```

Create a migration script from detected changes in the model
```
python manage.py db migrate --message 'initial database migration'
```

Apply the migration script to the database
```
python manage.py db upgrade
```

## Run the app
```
python manage.py run
```

## Run tests
```
python manage.py tests
```

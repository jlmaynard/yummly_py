pyum
====

Python project using Django which utilizes the Yummly API. 

// Main credit and reference to the language below belongs to Erik Hendrickson.  He was the main developer on the project but all team members added content.  My role was around the research and analysis of the diabetes portion. 

See the final presentation PDF file for an overview. 


This repository contains code for running the pyum web server. To successfully run, you will need to install the
following packages through pip:

  Django==1.6.2
  South==0.8.4
  django-tables2==0.15.0
  psycopg2==2.5.2
  yummly==0.4.0


These can be installed at one time by running the following command in your terminal:
  pip install -r /path/to/requirements.txt
  

Once that has been installed, navigate to the root folder in pyum and type the following command into your terminal:
  python manage.py runserver
  
This will start a local webserver provided by Django to test the site. You can navigate to your local instance by navigating
your browser to the following URL:
  http://127.0.0.1:8000/
  
And that is all. Pyum should now be open and running on your localhost.


Note that the settings.py file in the pyum folder is currently pointing to an online postgreSQL database.
In the future, this database will no longer be running and you will instead have to change the database provider to point
to the local db.sqlite3 file. This file contains the necessary enums and setup data that pyum requires to run. This should be changed only if the remote database is no longer running, but the text in settings.py would change from:

  DATABASES = {
    'default': {
        'ENGINE': 'django.db.backends.postgresql_psycopg2',
        'NAME': 'postgres',
        'USER': 'postgres',
        'PASSWORD': 'test',
        'HOST': '54.85.78.54'
    }
  }

To:

  DATABASES = {
    'default': {
        'ENGINE': 'django.db.backends.sqlite3',
        'NAME': os.path.join(BASE_DIR, 'db.sqlite3'),
        }
  }


Once again, ONLY CHANGE THIS IF THE REMOTE INSTANCE IS NOT RUNNING!


Pyum was developed by Vi Tran, Erik Hendrickson, Mark Brophy, Jason Maynard, James Robe, and Greg Alway.

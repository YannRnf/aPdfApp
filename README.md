# aPdfApp

## A PDF app setup

You must have configured a working Python3 environement for this app.

`python --version` to check your current distribution.

`git clone` the project.

Then install the dependencies
`pip install -r requirement.txt`

## DB config

### For a test environement

Don't change the settings file located in the pdfApp repository, 
the default DB config will use a sqlite file at the root of your project

### For a production environement

Update the settings file located in the pdfApp repository, replace :
```
'default': {
        'ENGINE': 'django.db.backends.sqlite3',
        'NAME': os.path.join(BASE_DIR, 'db.sqlite3'),
},
```
By your DB configuration. A RDS PostGreSQL is given below in the settings.py file.
```
rds': {
        'ENGINE': 'django.db.backends.postgresql',
        'NAME': os.environ.get('AWS_RDS_DB_NAME', ''),
        'USER': os.environ.get('AWS_RDS_DB_USER', ''),
        'PASSWORD': os.environ.get('AWS_RDS_DB_PASSWORD', ''),
        'HOST': os.environ.get('AWS_RDS_DB_HOST', ''),
        'PORT': os.environ.get('AWS_RDS_DB_PORT', '')
 }
 ```
 
 Then you'll need to define your ENV variables.
 
```
export AWS_RDS_DB_HOST=<myhostexample.*****.rds.amazonaws.com>
export AWS_RDS_DB_USER=<your_user>
export AWS_RDS_DB_PASSWORD=<your_password>
export AWS_RDS_DB_NAME=<your_db_name>
export AWS_RDS_DB_PORT=5432
 ```
 
 ### Populate your db schema
 
 `cd` into the project, and populate the datamodel using
`python manage.py migrate`

## Google OAuth2 setup

```
export SOCIAL_AUTH_GOOGLE_OAUTH2_KEY=<my_google_key>
export SOCIAL_AUTH_GOOGLE_OAUTH2_SECRET=<my_secret_secret>
```

## AWS S3 setup

You can setup the AWS S3 access by using a user and give him programatic access and the S3 appropriate permissions.

```
export AWS_ACCESS_KEY_ID=<my_aws_key>
export AWS_SECRET_ACCESS_KEY=<my_aws_secret_key>
```

A better solution is using a AWS IAM role with the right permissions and setup your project on an EC2 (with the role attached).
This way you'll just have to let the `None` default value in the settings file

If you don't wan't to use an S3 bucket for file handling it's completely possible.
Edit the settings.py file to remove the aws links and setup a static local media repository,
following the Django documentation section about media repository :
[Django uploaded file repository](hhttps://docs.djangoproject.com/en/2.1/topics/files/#file-storage)

## Setting up for production

For a production environement, you must set up a few more ENV variables :
Setting DEBUG to false.
You also can generate a random SECRET_KEY like showed below 
(even if you don't use this method, you MUST change the DJANGO_SECRET_KEY defined in the current settings.py code, which is public in this github repo)
```
export DJANGO_DEBUG=False
export DJANGO_SECRET_KEY=$(python -c 'import random; result = "".join([random.choice("abcdefghijklmnopqrstuvwxyz0123456789!@#$%^&*(-_=+)") for i in range(50)]); print(result)')
```


Cloudinary Django Sample Project
=============================

## Installation
Run the following commands from your shell:

    git clone git://github.com/cloudinary/cloudinary-django-sample.git
    cd cloudinary-django-sample
    pip install -r requirements.txt
    export CLOUDINARY_URL=cloudinary://<API-KEY>:<API-SECRET>@<CLOUD-NAME>
    python ./manage.py syncdb
    python ./manage.py runserver

You can now follow [this link](http://localhost:8000/) to start exploring the sample.   
The sample app also supports the django admin which is available [here](http://localhost:8000/admin)

### With virtualenv
We recommend and support the usage of virtualenv. All you need to do is create a new virtualenv (if necessary):

    virtualenv path/to/virtualenv

And then just activate it

    source path/to/virtualenv/bin/activate

Now you can go ahead with the instructions above

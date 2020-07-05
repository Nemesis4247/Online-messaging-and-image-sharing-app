# Online-messaging-and-image-sharing-app
A chat web application which enables real time communication through web sockets. This app is made on django and makes use of recent but very popular django library called django-channels. The app enables us to send messages or Images which will get transferred real time.

## Installation

Download and git and redis.
Make sure you have a python distribution of 3.7 or up
Then follow the steps below

```
git clone https://github.com/Luciferiitr/Online-messaging-and-image-sharing-app.git
cd Online-messaging-and-image-sharing-app/
pip install -r requirements.txt
python manage.py runserver
```

## Deployment
I would advise heroku for deploment. It provides all the necessary resources with one line of command without any hastle. Deployment is same as normal django app on heroku except for instead of gunicorn , daphne server will be used since we have to handle http as well as web socket requests. A detailed guide can be found at 
https://www.codingforentrepreneurs.com/blog/django-channels-to-production/

An example of app running on live stream : https://lit-earth.herokuapp.com/

## Additional notes
The app can cause problems while setting up in Windows operating system. I had a hard time setting up channel layers with redis-server on windows. So I would advise that ,if possible, use ubuntu for installation.

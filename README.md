# RS BOT
The chat bot learning humans interactions

The Current version of the App is Facebook messenger of page "Alphawordzz". 

## step 1
+ create facebook app
+ add messenger as platform
+ create webhook

## step 2

+ write a app.py file that will run you flask file, we can use heroku for server or ngrok as temp server.
+ In app.py we need to responce on GET request of hub which will be a json object.
+ hub.verify_token will be token that we will set on facebook while creating a webhook
+ we need to verify it and send back hub.challange as responce


## to run flask on local server
```
 $ export FLASK_APP=hello.py
 $ flask run
 * Running on http://127.0.0.1:5000/
```

## to run ngrok
```
 $ ./ngrok http 5000
 5000 is the local port number
```

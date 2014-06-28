Queuer
======

A very simple, flask-based app to handle queued registration.

Install the app:
----------------

```
# Install requirements
$ pip install -r requirements.txt

# Create an empty database
$ python db.py

# Run the service
$ python app.py
```

Give it a try:
--------------

```
>> import requests, json
>> requests.get('http://localhost:5000/registrations').json()
[]
>> requests.post('http://localhost:5000/registrations',
                 headers={'Content-Type': 'application/json'},
                 data=json.dumps({'email': 'email@address.com'}).json()
{
    "created_on": "2014-06-28T23:01:24.312810", 
    "email": "email@address.com", 
    "invited": false, 
    "position": 1, 
    "waiting_before": 0
}
>> requests.get('http://localhost:5000/registrations/email@address.com').json()
{
    "created_on": "2014-06-28T23:01:24.312810", 
    "email": "email@address.com", 
    "invited": false, 
    "position": 1, 
    "waiting_before": 0
}
```

Don't forget that you must past a `Content-Type: application/json` header along
w/ your request!

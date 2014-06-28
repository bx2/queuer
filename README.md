Queuer
======

A very simple, flask-based app to handle queued registration.


1. Install requisite packages:

> $ pip install -r requirements.txt

2. Create tables:

>$ python db.py

3. Run service:

> $ python app.py

4. Give it a try:

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
>> requests.put('http://localhost:5000/registrations/email@address.com',
                headers={'Content-Type': 'application/json'},
                data=json.dumps({'email': 'test@email.com'}).json()
{
    "created_on": "2014-06-28T23:01:24.312810", 
    "email": "test@email.com", 
    "invited": false, 
    "position": 1, 
    "waiting_before": 0
}
>> requests.delete('http://localhost:5000/registrations/test@email.com')
>> requests.get('http://localhost:5000/registrations').json()
[]
```

Don't forget that you must past a `Content-Type: application/json` header along
w/ your request!

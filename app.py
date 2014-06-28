#!/usr/bin/env python

from flask import Flask
from flask.ext.restful import reqparse, abort, Api, Resource

import db
from models import Registration


app = Flask(__name__)
api = Api(app)


parser = reqparse.RequestParser()
parser.add_argument('email', type=str)


class RegistrationResource(Resource):
    def get(self, email):
        registration = Registration.query.filter(Registration.email == email).first()
        if not registration:
            abort(404, message='Registration {} doesn\'t exist'.format(email))
        return registration.serialize()


class RegistrationListResource(Resource):
    def get(self):
        registrations = Registration.query.all()
        return [registration.serialize() for registration in registrations]

    def post(self):
        parsed_args = parser.parse_args()
        registration = Registration(email=parsed_args['email'])
        try:
            db.session.add(registration)
            db.session.commit()
        except db.IntegrityError:
            # we have this registration already - rollback and return it's details
            db.session.rollback()
            registration = Registration.query.filter(Registration.email == parsed_args['email']).first()
        return registration.serialize(), 201


api.add_resource(RegistrationListResource, '/registrations')
api.add_resource(RegistrationResource, '/registrations/<string:email>')


@app.teardown_appcontext
def shutdown_session(response):
    db.session.remove()
    return response


if __name__ == '__main__':
    app.run(debug=True)

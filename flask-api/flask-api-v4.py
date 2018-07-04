# demo api using Flask-RESTful and Marshmallow
'''
python flask-api-v4.py
'''
from flask_sqlalchemy import SQLAlchemy
from flask import Flask, request
from flask_restful import Api, Resource
from marshmallow import Schema, fields
from flask_marshmallow import Marshmallow


app = Flask(__name__, static_url_path="")
app.config['SQLALCHEMY_DATABASE_URI'] = 'postgresql://postgres:abc123@127.0.0.1:5432/mydb'
api = Api(app)
db = SQLAlchemy(app)
ma = Marshmallow(app)


# Model
class Person(db.Model):
    __tablename__ = 'persons'
#   __table_args__ = {'schema':'<schema_name>'} # for when using schemas
    id = db.Column(db.Integer, primary_key=True)
    first_name = db.Column(db.String)
    last_name = db.Column(db.String)

    def __init__(self, first_name, last_name):
        self.first_name = first_name
        self.last_name = last_name


class PersonSchema(ma.Schema):
#    id = fields.Integer()
    first_name = fields.String()
    last_name = fields.String()


# Main
class PersonListAPI(Resource):
    def get(self):
        persons = Person.query.all()
        persons = PersonSchema(many=True).dump(persons).data
        return {'status': 'sucess', 'persons': persons}, 200
        

    def post(self):
        json_data = request.get_json(force=True)
        person = Person(first_name=json_data['first_name'],last_name=json_data['last_name'])
        db.session.add(person)
        db.session.commit()
        output = PersonSchema().dump(person).data
        return {'status': 'sucess', 'person': output}, 201


# http://127.0.0.1:4000/todo/api/v4.0/persons
api.add_resource(PersonListAPI, '/todo/api/v4.0/persons', endpoint = 'person')


if __name__ == '__main__':
    app.run(debug=True, port=4000)
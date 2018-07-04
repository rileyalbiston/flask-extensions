# demo api using Flask-RESTful
'''
python flask-api-v3.py
'''

from flask import Flask, jsonify, abort, make_response
from flask_restful import Api, Resource, reqparse, fields, marshal

import psycopg2
import sys
import json


app = Flask(__name__, static_url_path="")
api = Api(app)


def connection():
    try:
        conn = psycopg2.connect("dbname='mydb' user='postgres' host='localhost' password='abc123'")
        print("Connecting to database\n ->%s" % (conn))
        return conn
    except:
        print("Unable to connect to the database")


def get_query():
    try:
        # connect to the PostgreSQL server
        conn = connection()
        # create a cursor
        cursor = conn.cursor()
        # execute a statement
        cursor.execute('SELECT id, first_name, last_name FROM persons')
        values = cursor.fetchall()
        keys = [desc.name for desc in cursor.description]
        data = [dict(zip(keys, value)) for value in values]       
        # close the communication with the PostgreSQL
        cursor.close()
        conn.close()
        print('Database connection closed.')
        return data
    except:
        print("No connection")


def insert_data(person):
    try:
        # connect to the PostgreSQL server
        conn = connection()
        # create a cursor
        cursor = conn.cursor()
        # execute a statement
        cursor.execute("INSERT INTO persons (first_name, last_name) VALUES (%s, %s)", (person['first_name'], person['last_name']))
        # commit the transaction
        conn.commit()
        # close the communication with the PostgreSQL
        cursor.close()
        if conn is not None:
            conn.close()
            print('Database connection closed.')
    except (Exception, psycopg2.DatabaseError) as error:
        print(error)


person_fields = {
    'id': fields.String,
    'first_name': fields.String,
    'last_name': fields.String,
}


class PersonListAPI(Resource):
    def __init__(self):
        self.reqparse = reqparse.RequestParser()
        self.reqparse.add_argument('first_name', type = str, required = True, help = 'No task title provided', location = 'json')
        self.reqparse.add_argument('last_name', type = str, default = "", location = 'json')
        super(PersonListAPI, self).__init__()


    def get(self):
        persons = get_query()
        return {'persons': [marshal(person, person_fields) for person in persons]}
        #return jsonify({'persons': persons})

    def post(self):
        args = self.reqparse.parse_args()
        person = {
            'first_name': args['first_name'],
            'last_name': args['last_name'],
        }
        insert_json = insert_data(person)
        return {'persons': marshal(person, person_fields)}, 201

api.add_resource(PersonListAPI, '/todo/api/v3.0/persons', endpoint = 'person')


if __name__ == '__main__':
    app.run(debug=True, port=4000)
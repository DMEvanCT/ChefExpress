import os
import sys
import getpass
from flask import Flask, request
from flask_restful import Resource, Api
from slackclass import slackclient


app = Flask(__name__)
app.secret_key = 'q$P1Q35vNxI!'
api = Api(app)

class vmwarechefservers(Resource):
    def post(self):
        data = request.get_json(silent=True)
        ChefFolder = '/etc/chef'
        try:
            vmwareserver = {'ip' : data['ip'],'nodename': data['nodename'],'rolename': data['rolename'], 'username': data['username'], 'password': data['password']}
            ip = data['ip']
            nodename = data['nodename']
            rolename = data['rolename']
            message = 'There was a new server created with the ip of  {} the node name of {} and the role of {}'.format(ip, nodename, rolename)
            channel = '#chefexpress'
            msg = slackclient(message, channel)
            return {"message": "Server successfully created"}
        except KeyError as name:
                return {'message': 'You did not remember {}'.format(name)}





api.add_resource(vmwarechefservers, '/create/chefserver')
api.add_resource(randomint,'/guess/randint')

if __name__ == '__main__':
    app.run(debug=True, port=5000)

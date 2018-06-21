import os
import sys
import getpass
from flask import Flask, request
from flask_restful import Resource, Api
from slackclass import slackclient
from ChefClass import cheftools


app = Flask(__name__)
app.secret_key = 'q$P1Q35vNxI!'
api = Api(app)

class vmwarechefservers(Resource):
    def post(self):
        data = request.get_json(silent=True)
        ChefFolder = '/etc/chef'
        try:
            vmwareserver = {'env': data['env'], 'ip' : data['ip'],'nodename': data['nodename'],'rolename': data['rolename'], 'username': data['username'], 'password': data['password'],
                            'vip': data['vip']}
            ip = data['ip']
            nodename = data['nodename']
            rolename = data['rolename']
            vip = data['vip']
            message = 'There was a new server bootstraped with the ip of  {} the node name of {} and the role of {}. The server is part of the following vip {}'.format(ip, nodename, rolename, vip)
            channel = '#chefexpress'
            msg = slackclient(message, channel)
            ctools = cheftools()
            cheftools.bootstrapchef(self, '/etc/chef-{}'.format(data['env']), data['ip'], data['nodename'], data['rolename'], data['username'], data['password'])
            return {"message": "Server successfully bootstraped. Check work. Does not do return codes yet."}
        except KeyError as name:
                return {'message': 'You did not remember {}'.format(name)}





api.add_resource(vmwarechefservers, '/create/chefserver')

if __name__ == '__main__':
    app.run(debug=True, port=5000)

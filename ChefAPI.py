import os
import getpass
from flask import Flask, request, session, logging, request
from flask_restful import Resource, Api
from slackclass import slackclient
from ChefClass import cheftools
from flaskext.mysql import MySQL
import configparser
from passlib.hash import sha256_crypt
from functools import wraps



app = Flask(__name__)
app.secret_key = 'q$P1Q35vNxI!'
api = Api(app)

mysql = MySQL(app)


app.secret_key = 'q$P1Q35vNxI!'
conf = configparser.ConfigParser()
conf.sections()
conf.read('/etc/dm/mysql.ini')



app.config['MYSQL_DATABASE_USER'] = conf["mysql"]["DatabaseUser"]
app.config['MYSQL_DATABASE_PASSWORD'] = conf["mysql"]["DatbasePassword"]
app.config['MYSQL_DATABASE_HOST'] = conf["mysql"]["DatabaseLocation"]
app.config['MYSQL_CURSORCLASS'] = 'DictCursor'


class logintoapp(Resource):

    def post(self):

            loginperson = request.get_json()
            username = loginperson['username']
            password_canidate = loginperson['password']



    #Create cursor
            cur = mysql.get_db().cursor()

    #get user by username
            result = cur.execute("SELECT * FROM auth.users WHERE username = %s", [username])
            if result > 0:
            # get stored hash
                data = cur.fetchone()
                password = data['password']
                enabled_user = data['enabled_user']



                if sha256_crypt.verify(password_canidate, password) and enabled_user == 1:
                    app.logger.info("Password Matched")
                    session['logged_inn'] = True
                    session['username'] = username
                    cur.close()
                    return session['logged_inn']



                elif sha256_crypt.verify(password_canidate, password) == False:
                    app.logger.info("Password incorrect")


                else:
                    app.logger.info("Account is locked")


            else:
                app.logger.info("No user")


def is_logged_in(f):
    @wraps(f)
    def wrap(*args, **kwargs):
        if 'logged_inn' in session:
            return f( *args, **kwargs )

        else:
          message =   {'message': 'You need to be logged in to access this function'}
          return message



class vmwarechefservers(Resource):
    @is_logged_in
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





api.add_resource(vmwarechefservers, '/api/create/chefserver')
api.add_resource(logintoapp,'/api/login')

if __name__ == '__main__':
    app.run(debug=True, port=5000)

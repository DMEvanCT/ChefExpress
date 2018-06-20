# ChefExpress

import os
import sys
import getpass
# from slackclient import SlackClient
#
# slack_token = os.environ['301e24c4ff98470232f402ece894e33a']
# sc = SlackClient(ocaugspcmqdEIXhDfHo39ibn)
#
# sc.api_call(
#   "chat.postMessage",
#   channel="#general",
#   text="Hello from Python! :tada:"
# )

print("Welcome to the Chef Express Please follow the prompts")
ChefExpress = input("Would you like to work with Chef Express \n Please enter yes or no \n")
while ChefExpress == "yes" or ChefExpress == 'YES' or ChefExpress == 'Yes':
    ChefEnviorment = input("Please enter the enviorment you are working in options are"
                           "\n Madison \n Ord \n Iad \n or type exit to exit program \n")

    if ChefEnviorment == 'Ord' or ChefEnviorment == 'ord' or ChefEnviorment == 'ORD':
        ChefFolder = '~/Chef-Ord'
        print("You have chosen Ord as your enviorment")
        ChefBase = input('Please enter what you would like to do. Here are your options \n knife-vsphere \n'
                         'knife cookbook \n knife bootstrap \n')

        if ChefBase == 'knife cookbook' or ChefBase == 'Knife Cookbook' or ChefBase == 'Knife cookbook':
            wwcookbook = input("Do you want to work with cookbooks?")
            while wwcookbook == 'yes':
                print("Here are your options \n upload cookbook \n download cookbook \n cookbook list chef server \n cookbooks on machine "
                    "\n roles on machine \n create new cookbook ")
                ChefInput = input("Please enter what you would like to do \n")

                if ChefInput == "upload cookbook":
                     os.system('ls ' + ChefFolder + "/cookbooks")
                     CookbookName = input('Please enter the  cookbook name \n'
                                 'Before uploading please update metadata.rb. \n Please enter the cookbook upload. \n')
                     os.system('cd' + " " + ChefFolder + " " '&& knife cookbook upload' + " " + CookbookName)

                elif ChefInput == "download cookbook":
                    os.system('cd ~/Chef-Ord && knife cookbook list')
                    CookbookName = input("Please enter the cookbyook download")
                    os.system('cd' + " " + ChefFolder + " " + '&& knife cookbook download' + " " + CookbookName)


                elif ChefInput == "cookbook list chef server":
                    os.system('cd ~/Chef-Ord && knife cookbook list')

                elif ChefInput == "cookbooks on machine":
                    os.system('ls ' + ChefFolder + "/cookbooks")

                elif ChefInput == 'create new cookbook' or ChefInput == 'Create new cookbook' or ChefInput == 'Create New Cookbook':
                     cookbookname = input("Please enter the name of new cookbook\n")
                     os.system('cd' + " " + ChefFolder + "/cookbooks " + "&&" + " " "chef generate cookbook " + cookbookname)
                     print("The cookbook is located at " + ChefFolder + "/cookbooks/" + cookbookname)
                elif ChefInput == 'list roles' or ChefInput == 'list roles on chef' or ChefInput == 'roles':
                     os.system('cd ' + ChefFolder + " knife role list")

                else:
                    print("Please chose one of the following options  \n upload cookbook \n download cookbook")
                wwcookbook = input("Would you like to continue working with cookbooks? yes or no \n")

        elif ChefBase == 'knife bootstrap':
            bootstrap = input("Would you like to bootstrap a machine? yes or no")
            while bootstrap == "yes" or bootstrap == 'Yes' or bootstrap == "YES":
                os = input("Please choose an operating system \n linux \n Windows \n")
                if os == "linux":
                    ipaddress = input("Please enter the ip address of the machine you want to bootstrap \n")
                    nodename = input("Please enter the node name \n")
                    rolename = input("Please enter the role name \n")
                    username = input("Please enter your username \n")
                    password = getpass.getpass("Please enter your password \n")
                    os.system(
                          'cd' + " " + ChefFolder + " " + '&& knife bootstrap ' + ipaddress + " " + "-N " + nodename + " "
                            + "-r 'role[" + rolename + "]'" + " " + "--sudo" + " " + "-x " + username + " " + "-P " + upass)
                    ConfigureMachine = input("Would you like to configure another machine?")
                else:
                    print("Comming soon")
                    bootstrap = input("Would you like to bootstrap another machine? yes or no")


        elif ChefBase == 'knife-vsphere' or ChefBase == 'knife vsphere' or ChefBase == 'vsphere':
            ConfigureMachine = input("Would you like to configure a machine? \n")
            while ConfigureMachine == 'yes':

                os.system('cd' + " " + ChefFolder + " " + '&& knife vsphere template list')

                template = input("Please enter the template to clone from \n")
                nodename = input("Please input the node name \n")
                domain = input("Please enter the domain \n")
                username = input("Username \n")
                password = getpass.getpass("Please enter your password \n")
                typer = input('Is it a role or recipe? \n')
                if typer == 'role':
                    os.system('cd ' + ChefFolder + ' && knife role list \n')
                elif typer == 'recipe':
                    os.system('cd ' + ChefFolder + ' && knife recipe list \n')
                else:
                    print("Sorry neither of those answers are valid. \n Please choose between  ")

                rname = input("Please choose from above. \n")
                numipaddress = input("Would you like to enter more than 1 or 2 ip address for the machine \n")
                if numipaddress == '1':
                    ipaddress = input("Please enter an ip address ex 192.168.1.1 \n")
                    cider = input("Please input the ip address in CIDR notation /23 /24 /25 \n")
                    os.system('ping ' + ipaddress + ' -c 5')
                    os.system(
                        'cd ' + ChefFolder + '&&' + ' knife vsphere vm clone ' + nodename + ' --template ' + template + ' --cips ' + ipaddress + cider +
                    ' --chostname ' + nodename + ' --cdnsips 10.1.0.21, 10.1.0.22' + ' --cdomain ' + domain + ' --ssh-user ' + username + ' -P ' + password
                    + ' --bootstrap --run-list ' + typer + '[' + rname + ']' + ' --cspec chef')

                elif numipaddress == '2':
                    ipaddress = input("Please enter an ip address ex 192.168.1.1 \n")
                    cider = input("Please input the ip address in CIDR notation /23 /24 /25 \n")
                    os.system('ping ' + ipaddress + ' -c 5')
                    ipaddress2 = input("Please enter the 2nd ip address \n")
                    os.system('cd ' + ChefFolder + '&&' + ' knife vsphere vm clone ' + nodename + ' --template ' + template + ' --cips ' + ipaddress + cider + "," + ipaddress2 + cider +
                    ' --chostname ' + nodename + ' --cdnsips 10.1.0.21, 10.1.0.22' + ' --cdomain ' + domain + ' --ssh-user ' + username + ' -P ' + password
                    + ' --bootstrap --run-list ' + typer + '[' + rname + ']' + ' --cspec chef')

                else:
                    print("Comming Soon")

            ConfigureMachine = input("Would you like to configure another machine? \n")

    elif ChefEnviorment == 'Madison' or ChefEnviorment == "madison" or ChefEnviorment == "MADISON":
        ChefFolder = '~/Chef-Mad'
        print("You have chosen Ord as your enviorment")
        ChefBase = input('Please enter what you would like to do. Here are your options \n knife vsphere \n'
                         'knife cookbook \n knife bootstrap \n')


        if ChefBase == 'knife cookbook' or ChefBase == 'Knife Cookbook' or ChefBase == 'Knife cookbook':
            wwcookbook = input("Do you want to work with cookbooks?")
            while wwcookbook == 'yes':
                print(
                    "Here are your options \n upload cookbook \n download cookbook \n cookbook list chef server \n cookbooks on machine "
                    "\n roles on machine \n create new cookbook ")
                ChefInput = input("Please enter what you would like to do \n")
                if ChefInput == "upload cookbook":
                    os.system('ls ' + ChefFolder + "/cookbooks")
                    CookbookName = input('Please enter the  cookbook name \n'
                                         'Before uploading please update metadata.rb. \n Please enter the cookbook upload. \n')
                    os.system('cd' + " " + ChefFolder + " " '&& knife cookbook upload' + " " + CookbookName)

                elif ChefInput == "download cookbook":
                    os.system('cd ~/Chef-Ord && knife cookbook list')
                    CookbookName = input("Please enter the cookbyook download")
                    os.system('cd' + " " + ChefFolder + " " + '&& knife cookbook download' + " " + CookbookName)

                elif ChefInput == "cookbook list chef server":
                    os.system('cd ~/Chef-Ord && knife cookbook list')

                elif ChefInput == "cookbooks on machine":
                    os.system('ls ' + ChefFolder + "/cookbooks")

                elif ChefInput == 'create new cookbook' or ChefInput == 'Create new cookbook' or ChefInput == 'Create New Cookbook':
                    cookbookname = input("Please enter the name of new cookbook\n")
                    os.system(
                        'cd' + " " + ChefFolder + "/cookbooks " + "&&" + " " "chef generate cookbook " + cookbookname)
                    print("The cookbook is located at " + ChefFolder + "/cookbooks/" + cookbookname)

                elif ChefInput == 'list roles' or ChefInput == 'list roles on chef' or ChefInput == 'roles':
                    os.system('cd ' + ChefFolder + " knife role list")

                else:
                    print("Please chose one of the following options  \n upload cookbook \n download cookbook")
                wwcookbook = input("Would you like to continue working with cookbooks? yes or no \n")

        elif ChefBase == 'knife bootstrap':
            bootstrap = input("Would you like to bootstrap a machine? yes or no")
            while bootstrap == "yes" or bootstrap == 'Yes' or bootstrap == "YES":
                os = input("Please choose an operating system \n linux \n Windows \n")
                if os == "linux":
                    ipaddress = input("Please enter the ip address of the machine you want to bootstrap \n")
                    nodename = input("Please enter the node name \n")
                    rolename = input("Please enter the role name \n")
                    username = input("Please enter your username \n")
                    upass = input("Please enter your password \n")
                    os.system(
                        'cd ' + ChefFolder + ' && knife bootstrap ' + ipaddress + " -N " + nodename
                        + " -r 'role[" + rolename + "]'" +  ' --sudo' + ' -x ' + username + ' -P ' + upass)
                    ConfigureMachine = input("Would you like to configure another machine?")
                else:
                    print("Comming soon")
                    bootstrap = input("Would you like to bootstrap another machine? yes or no")

        elif ChefBase == 'knife-vsphere' or ChefBase == 'knife vsphere' or ChefBase == 'vsphere':
            ConfigureMachine = input("Would you like to configure a machine? \n")
            while ConfigureMachine == 'yes':

                os.system('cd' + " " + ChefFolder + " " + '&& knife vsphere template list')
                template = input("Please enter the template to clone from \n")
                nodename = input("Please input the node name \n")
                domain = input("Please enter the domain \n")
                username = input("Username \n")
                password = input("Please enter a password \n")
                typer = input('Is it a role or recipe? \n')
                if typer == 'role':
                    os.system('cd ' + ChefFolder + ' && knife role list \n')
                elif typer == 'recipe':
                    os.system('cd ' + ChefFolder + ' && knife recipe list \n')
                else:
                        print("Sorry neither of those answers are valid. \n Please choose between  ")
                rname = input("Please choose from above. \n")
                numipaddress = input("Would you like to enter more than 1 or 2 ip address for the machine \n")
                if numipaddress == '1':
                    ipaddress = input("Please enter an ip address ex 192.168.1.1 \n")
                    cider = input("Please input the ip address in CIDR notation /23 /24 /25 \n")
                    os.system('ping ' +  ipaddress + ' -c 5')
                    print("This is your configuration \n " + nodename + "\n " + ipaddress + "\n " + domain + "\n " + typer + "\n")
                    okay = input("Is this configuration okay? \n")
                    if okay == "no":
                        print("No problem!")
                        break
                    else:
                        print("Thank you for creating a machine with ChefExpress")
                    os.system('cd ' + ChefFolder + '&&' + ' knife vsphere vm clone ' + nodename + ' --template ' + template + ' --cips ' + ipaddress + cider +
                              ' --chostname ' + nodename + ' --cdnsips 10.1.0.21, 10.1.0.22' + ' --cdomain ' + domain + ' --ssh-user ' + username + ' -P ' + password
                              + ' --bootstrap --run-list ' + typer + '[' + rname + ']' + ' --cspec DNS')
                elif numipaddress == '2':
                    ipaddress = input("Please enter an ip address ex 192.168.1.1 \n")
                    cider = input("Please input the ip address in CIDR notation /23 /24 /25 \n")
                    os.system('ping ' + ipaddress + ' -c 5')
                    ipaddress2 = input("Please enter the 2nd ip address")
                    os.system(
                        'cd ' + ChefFolder + '&&' + ' knife vsphere vm clone ' + nodename + ' --template ' + template + ' --cips ' + ipaddress + cider + "," + ipaddress2 + cider +
                        ' --chostname ' + nodename + ' --cdnsips 10.1.0.21, 10.1.0.22' + ' --cdomain ' + domain + ' --ssh-user ' + username + ' -P ' + password
                        + ' --bootstrap --run-list ' + typer + '[' + rname + ']' + ' --cspec DNS')

                else:
                    print("Comming Soon")
            ConfigureMachine = input("Would you like to configure another machine? \n")
    else:
        print("Sorry none of the options provided were valid. Please try again")

    ChefExpress = input("Would you like to use this tool again? yes or no \n")

else:
print("Sorry that is not a valid response please choose yes or no.")

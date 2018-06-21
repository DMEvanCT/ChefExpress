class cheftools():
    def __init__(self):
        pass
    def bootstrapchef(self, ChefFolder, ipaddress, nodename, role, username, password):
        import os
        self.ChefFolder = ChefFolder
        self.ipaddress = ipaddress
        self.nodename = nodename
        self.role = role
        self.username = username
        self.password = password
        os.system(
            'cd' + " " + ChefFolder + " " + '&& knife bootstrap ' + ipaddress + " " + "-N " + nodename + " "
            + "-r 'role[" + role + "]'" + " " + "--sudo" + " " + "-x " + username + " " + "-P " + password)
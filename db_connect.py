##########################  Database Connection Functionality  ##########################

import mysql.connector

def project_db():
    return(mysql.connector.connect( # connecting to database
    host="localhost",
    user="root", # change db user, passwd, and name here
    passwd="Deepak@6122004",
    database="project",
    auth_plugin='mysql_native_password'))

if __name__ == '__main__':
    project_db()
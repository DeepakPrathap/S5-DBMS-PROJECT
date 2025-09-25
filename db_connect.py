##########################  Database Connection Functionality  ##########################

import mysql.connector

def project_db():
    return(mysql.connector.connect( 
    host="localhost",
    user="root", 
    passwd="Root@1234",
    database="project",
    auth_plugin='mysql_native_password'))

if __name__ == '__main__':

    project_db()

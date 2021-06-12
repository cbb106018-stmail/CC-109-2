import conn_database as conn
import json

host = "database_read"
port = 27018

def _admin_listing_user():
    userList = None
    if conn.is_client_primary(host, port):
        userList = conn.find_collection(host, port)
    return userList

def listing_user():
    userList = None
    if conn.is_client_primary(host, port) != None:
        userList = conn.find_only_collection(host, port, query={'password': 0})
    return userList

def is_username_existing(username):
    isExisting = None
    if conn.is_client_primary(host, port) != None:
        if conn.count_collection(host, port, query={'username': username}) == 0:
            isExisting = False
        else:
            isExisting = True
    return isExisting

import conn_database as conn
import json

host = "database_write"
port = 27017

def create_account(incomingData):
    success = None
    if incomingData != None:
        accountData = parse_account(incomingData)
        success = insert_data(accountData, False, {'username': accountData.get('username')})
    return success

def str_json_conv(string):
    if string != None and type(string)==str:
        return json.loads(string)
    else:
        return None

def parse_account(jsonData):
    dictData = None
    if type(jsonData) == str:
        jsonData = str_json_conv(jsonData)
    if 'username' in jsonData and 'password' in jsonData:
        userrole = jsonData.get('userrole') or 'user'
        dictData = {'username': jsonData.get('username'), 'password': jsonData.get('password'), 'userrole': userrole}
    return dictData

def insert_data(dataPair, allowDuplicate=True, uniqueDict=None):
    # Return None means database or data error.
    # Return False when data duplicated or insert error.
    success = None
    # Param dataPair must be dict
    state = type(dataPair)
    if dataPair!=None and type(dataPair)==dict:
        if conn.is_client_primary(host, port) == True:
            isDuplicated = None
            state='a'
            if allowDuplicate != True and uniqueDict!=None and type(uniqueDict)==dict:
                state='b'
                count = conn.count_collection(host, port, uniqueDict)
                if conn.count_collection(host, port, uniqueDict) == 0:
                    state='c'
                    isDuplicated = False
                else:
                    state='d'
                    isDuplicated = True
            if isDuplicated == None or isDuplicated == False:
                state='e'
                result = conn.insert_collection(host, port, dataPair)
                if result:
                    state='f'
                    success = True
                else:
                    state='g'
                    success = False
            else:
                state=isDuplicated
                success = False
    #return success
    return count


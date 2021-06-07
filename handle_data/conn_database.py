from pymongo import MongoClient, ASCENDING, errors
import datetime

def __connect_database(host, port=27017, timeout=5, debug=False):
    if host != None and host!='':
        try:
            # Do not let timeout as 0ms, or will report error.
            client = MongoClient(host=host, port=port, serverSelectionTimeoutMS=timeout)
            return client
        except errors.ServerSelectionTimeoutError as err:
            if debug == True:
                return err
            else:
                return None
    else:
        return None

def _database_cursor(client):
    if client != None:
        database = client['users']
        collect = database['accounts']
        return collect
    else:
        return None

def _disconnect_database(client):
    if client != None:
        client.close()
    return None

def _is_client_alive(host, port, timeout=5, debug=False):
    isAlive = None
    try:
        client = __connect_database(host, port, timeout, debug)
        if client != None:
            collect = _database_cursor(client)
            if collect != None:
                isAlive = True
            else:
                isAlive = False
            _disconnect_database(client)
        else:
            isAlive = False
    except errors.ServerSelectionTimeoutError as err:
        if debug == True:
            isAlive = err
        else:
            isAlive = False
    return isAlive

def is_client_primary(host, port, timeout=5, debug=False):
    isPrimary = None
    isAlive = _is_client_alive(host, port, timeout, debug)
    if isAlive == True:
        client = __connect_database(host, port, timeout, debug)
        if client != None:
            try:
                isPrimary = client.is_primary
            except errors.ServerSelectionTimeoutError as err:
                if debug == True:
                    isPrimary = err
                else:
                    isPrimary = None
            _disconnect_database(client)
    else:
        isPrimary = None
    return isPrimary


def _find_collection(host, port, query={}, query2=None, sort=None):
    # If find no result returns None, so use False to instead of error.
    result = False
    if type(query)==dict or query==None:
        client = __connect_database(host, port)
        if client != None:
            collect = _database_cursor(client)
            if collect != None:
                if sort == None:
                    # datatype: list
                    if query2 == None:
                        result = list(collect.find(query))
                        if query == None:
                            result = list(collect.find())
                    else:
                        result = list(collect.find(query, query2))
                else:
                    if query2 == None:
                        result = list(collect.find(query).sort(sort, ASCENDING))
                    else:
                        result = list(collect.find(query, query2)).sort(sort, ASCENDING)
            client = _disconnect_database(client)
    return result

def find_collection(host, port, query={}, sort=None):
    result = False
    if type(query)==dict or query==None:
        client = __connect_database(host, port)
        if client != None:
            collect = _database_cursor(client)
            if collect != None:
                if sort == None:
                    result = list(collect.find(query))
                else:
                    result = list(collect.find(query).sort(sort, ASCENDING))
            client = _disconnect_database(client)
    return result

def find_only_collection(host, port, query={}, sort=None):
    result = False
    if type(query)==dict or query==None:
        client = __connect_database(host, port)
        if client != None:
            collect = _database_cursor(client)
            if collect != None:
                if sort == None:
                    if query == None:
                        result = list(collect.find({}))
                    else:
                        result = list(collect.find({}, query))
                else:
                    if query == None:
                        result = list(collect.find(query).sort(sort, ASCENDING))
                    else:
                        result = list(collect.find(query).sort(sort, ASCENDING))
            client = _disconnect_database(client)
    return result

def _find_one_collection(host, port, query={}, query2=None):
    result = False
    if type(query)==dict or query==None:
        client = __connect_database(host, port)
        if client != None:
            collect = _database_cursor(client)
            if collect != None:
                if query2 == None:
                    result = collect.find_one(query)
                    if query == None:
                        result = collect.find_one()
                else:
                    result = collect.find_one(query, query2)
            client = _disconnect_database(client)
    return result

def find_one_collection(host, port, query={}):
    result = False
    if type(query)==dict or query==None:
        client = __connect_database(host, port)
        if client != None:
            collect = _database_cursor(client)
            if collect != None:
                if query == None:
                    # datatype: dict
                    result = collect.find_one()
                else:
                    result = collect.find_one(query)
            client = _disconnect_database(client)
    return result


def find_the_one_collection(host, port, query={}):
    result = False
    if type(query)==dict or query==None:
        client = __connect_database(host, port)
        if client != None:
            collect = _database_cursor(client)
            if collect != None:
                if query == None:
                    result = collect.find_one({})
                else:
                    result = collect.find_one({}, query)
            client = _disconnect_database(client)
    return result

def _count_collection(host, port, query={}, query2=None):
    result = False
    if type(query)==dict or query==None:
        client = __connect_database(host, port)
        if client != None:
            collect = _database_cursor(client)
            if collect != None:
                if query2 == None:
                    result = collect.find(query).count()
                    if query == None:
                        result = collect.find().count()
                else:
                    result = collect.find(query, query2).count()
            client = _disconnect_database(client)
    return result

def count_collection(host, port, query={}):
    result = False
    if type(query)==dict or query==None:
        client = __connect_database(host, port)
        if client != None:
            collect = _database_cursor(client)
            if collect != None:
                if query == None:
                    result = collect.find().count()
                else:
                    result = collect.find(query).count()
            client = _disconnect_database(client)
    return result

def count_advanced_collection(host, port, query={}):
    result = False
    if type(query)==dict or query==None:
        client = __connect_database(host, port)
        if client != None:
            collect = _database_cursor(client)
            if collect != None:
                if query == None:
                    result = collect.find({}).count()
                else:
                    result = collect.find({}, query).count()
            client = _disconnect_database(client)
    return result

def _update_one_collection(host, port, condition, new_data):
    result = False
    client = __connect_database(host, port)
    if client != None:
        collect = _database_cursor(client)
        if collect != None:
            result = collect.update_one(condition, new_data)
        client = _disconnect_database(client)
    return result

def _update_many_collection(host, port, condition, new_data):
    result = False
    client = __connect_database(host, port)
    if client != None:
        collect = _database_cursor(client)
        if collect != None:
            result = collect.update_many(condition, new_data)
        client = _disconnect_database(client)
    return result

def _delete_one_collect(host, port, condition):
    result = False
    if type(condition) == dict:
        client = __connect_database(host, port)
        if client != None:
            collect = _database_cursor(client)
            if collect != None:
                result = collect.delete_one(condition)
            client = _disconnect_database(client)
    return result

def _delete_many_collection(host, port, condition):
    result = False
    if type(condition) == dict:
        client = __connect_database(host, port)
        if client != None:
            collect = _database_cursor(client)
            if collect != None:
                result = collect.delete_many(condition)
            client = _disconnect_database(client)
    return result

def _get_nowtime():
    datetime_dt = datetime.datetime.today()
    time_delta = datetime.timedelta(hours=8)
    new_dt = datetime_dt + time_delta
    datetime_format = new_dt.strftime("%Y/%m/%d %H:%M:%S")
    return datetime_format

def insert_collection(host, port, document, timestamp=True):
    result = False
    if type(document) == dict:
        client = __connect_database(host, port)
        if client != None:
            collect = _database_cursor(client)
            if collect != None:
                if len(document) > 0:
                    if timestamp == True:
                        document['timestamp'] = _get_nowtime()
                    result = collect.insert_one(document)
            client = _disconnect_database(client)
    return result

def insert_many_collection(host, port, documents, timestamp=True):
    result = False
    if type(document) == list:
        client = __connect_database(host, port)
        if client != None:
            collect = _database_cursor(client)
            if collect != None:
                if len(documents) > 0:
                    if timestamp == True:
                        timestamp = _get_nowtime()
                        for each in documents:
                            if len(each) > 0:
                                each['timestamp'] = timestamp
                    result = collect.insert_many(documents)
            client = _disconnect_database(client)
    return result


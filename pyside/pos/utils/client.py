import os
from xmlrpc import client


class Client:

    @staticmethod
    def load():
        db = os.getenv('DB')
        uid = os.getenv('UID')
        password = os.getenv('PASSWORD')
        return db, uid, password

    @staticmethod
    def api():
        server = os.getenv('SERVER')
        return client.ServerProxy('%s/xmlrpc/2/object' % server)

from orator import DatabaseManager
from orator import Model

config = {
   'development': {
        'driver': 'sqlite',
        'database': '/tmp/test.db'
    }
}

db = DatabaseManager(config)

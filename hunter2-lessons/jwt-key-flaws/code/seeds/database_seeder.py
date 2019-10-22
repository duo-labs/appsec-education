from orator.seeds import Seeder
from .users_table_seeder import UsersTableSeeder

class DatabaseSeeder(Seeder):

    def run(self):
        """
        Run the database seeds.
        """
        self.call(UsersTableSeeder)


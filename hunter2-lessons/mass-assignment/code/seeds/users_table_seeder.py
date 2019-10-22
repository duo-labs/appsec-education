from orator.seeds import Seeder


class UsersTableSeeder(Seeder):

    def run(self):
        """
        Run the user seeds.
        """
        self.db.table('users').insert({
            'name': 'User 1',
            'email': 'user1@test.com',
            'username': 'user1',
            'password': '$2y$10$abo9EipnAGYDxr7c7XcOsOtPv/ti9XaFf6w3kzoZit1tAUnOUAAh2'
        })
        self.db.table('users').insert({
            'name': 'User 2',
            'email': 'user2@test.com',
            'username': 'user2',
            'password': '$2y$10$TH.itM0/gZ71XyeLpFNF3ehYKxUSHzNzgKGUy2RMTB/KIXPNAM3Ye'
        })


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
            'password': '$2y$10$abo9EipnAGYDxr7c7XcOsOtPv/ti9XaFf6w3kzoZit1tAUnOUAAh2',
            'id': 1,
            'level': 'user',
            'token': ''
        })
        self.db.table('users').insert({
            'name': 'User 2',
            'email': 'user2@test.com',
            'username': 'user2',
            'password': '$2y$10$G5eCHz5u.jR7QG/vhpj.7.s6puyRHIeLinUnnJJYnDVx.NZOP1ZVu',
            'id': 2,
            'level': 'user',
            'token': ''
        })


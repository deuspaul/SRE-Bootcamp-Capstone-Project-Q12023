import unittest
from methods import Token, Restricted


class TestStringMethods(unittest.TestCase):

    def setUp(self):
        self.convert = Token()
        self.validate = Restricted()

    def test_generate_token(self):
        query = [('F^S%QljSfV', '15e24a16abfc4eef5faeb806e903f78b188c30e4984a03be4c243312f198d1229ae8759e98993464cf713e3683e891fb3f04fbda9cc40f20a07a58ff4bb00788', 'admin')]
        self.assertEqual('eyJhbGciOiJIUzI1NiIsInR5cCI6IkpXVCJ9.eyJyb2xlIjoiYWRtaW4ifQ.StuYX978pQGnCeeaj2E1yBYwQvZIodyDTCJWXdsxBGI', self.convert.generateToken('admin', 'secret', query))

    def test_access_data(self):
        self.assertEqual(True, self.validate.access_Data('Bearer eyJhbGciOiJIUzI1NiIsInR5cCI6IkpXVCJ9.eyJyb2xlIjoiYWRtaW4ifQ.StuYX978pQGnCeeaj2E1yBYwQvZIodyDTCJWXdsxBGI'))


if __name__ == '__main__':
    unittest.main()

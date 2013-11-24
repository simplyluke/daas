import os
import unittest
import app

class DaasTestCase(unittest.TestCase):

  def setUp(self):
    self.app = app.app.test_client()

  def test_index(self):
    rv = self.app.get('/')
    assert 'Doge As A Service' in rv.data

  def test_wow(self):
    rv = self.app.get('/wow/foobar')
    assert 'wow such foobar' in rv.data


if __name__ == '__main__': unittest.main()

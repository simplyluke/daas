import os
import unittest
import app

class DaasTestCase(unittest.TestCase):

  # Such unit testing 
  def setUp(self):
    self.app = app.app.test_client()

  def test_index(self):
    rv = self.app.get('/')
    assert 'Doge As A Service' in rv.data

  def test_wow(self):
    rv = self.app.get('/wow/foobar')
    assert 'wow such foobar' in rv.data

  def test_very(self):
    rv = self.app.get('/very/foobar')
    assert 'very foobar. wow' in rv.data

  def test_plz(self):
    rv = self.app.get('/plz/foo/bar')
    assert 'foo plz' and 'from bar' in rv.data

  def test_little(self):
    rv = self.app.get('/little/foo')
    assert 'little foo. wow' in rv.data

  def test_wat(self):
    rv = self.app.get('/wat/foo')
    assert 'wat r u doin, foo' in rv.data

  def test_omg(self):
    rv = self.app.get('/omg/foo')
    assert 'omg such foo. wow' in rv.data

  def test_thx(self):
    rv = self.app.get('/thx/foo/bar')
    assert 'thx foo' and 'from bar' in rv.data

  def test_fuk(self):
    rv = self.app.get('/fuk/foo/bar')
    assert 'fuk u foo' and 'from bar' in rv.data


if __name__ == '__main__': unittest.main()

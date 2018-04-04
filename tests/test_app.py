Python 3.6.3 (v3.6.3:2c5fed86e0, Oct  3 2017, 00:32:08) 
[GCC 4.2.1 (Apple Inc. build 5666) (dot 3)] on darwin
Type "copyright", "credits" or "license()" for more information.
>>> WARNING: The version of Tcl/Tk (8.5.9) in use may be unstable.
Visit http://www.python.org/download/mac/tcltk/ for current information.
import unittest
from Web_unit_docker import app
from datetime import datetime

app_ = app.app
db = app.db

class AppTests(unittest.TestCase):
    def setUp(self):
        app_.config['TESTING'] = True
        app_.config['SQLALCHEMY_DATABASE_URI'] =  'sqlite:///'
        db.create_all()

    def tearDown(self):
        db.drop_all()

    def test_add(self):
        with self.client:
            dummy_data = app.Expression(text="text", value=1,now=datetime.utcnow())
            response = self.client.post('/add',data=dummy_data,follow_redirects=True)
            self.assertTrue("Yes, dataa gets added", response)

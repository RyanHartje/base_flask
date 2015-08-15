base_flask 
=========

Super simple implementation of flask used as a template for lightweight apps

Version
----
0.2.0


Installation
---

Requirements for Bcrypt:

yum groupinstall "Development Tools" -y; yum install python34-devel libffi-devel;


Python2:
```ssh
yum install -y mongodb mongodb-server; service mongod start; chkconfig mongod on;
git clone https://github.com/ryanhartje/base_flask.git
cd base_flask
pip3 install -r requirements.txt
python3 app/app.py
```


Python3:
```sh
yum install -y mongodb mongodb-server; service mongod start; chkconfig mongod on;
yum install epel-release -y; 
yum install python34;
curl -O https://raw.githubusercontent.com/pypa/pip/master/contrib/get-pip.py; python3 get-pip.py; 
git clone https://github.com/ryanhartje/base_flask.git
cd base_flask
pip3 install -r requirements.txt
python3 app/app.py
```

Change Log
---

0.2 - Addition of User registration and management with Flask-login and 
      Flask security. Flask-sec and Flask-login use MongoDB to store user credentials
      with a configurable salt and hash. 
     
      Note: The mongodb installation is not setup with user authentication. If you are
      using this for anything production, you should ensure that your application is using
      an authenticated user, instead of leaving it world readable.
0.1 - Basic Bootstrap Template served by Flask


License
----

MIT


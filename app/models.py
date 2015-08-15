from mongoengine import connect, NULLIFY, Document, EmbeddedDocument, StringField, \
  IntField, DateTimeField, BooleanField, SequenceField, DictField, ObjectIdField, \
  ReferenceField, ListField, EmbeddedDocumentField
from flask.ext.security import UserMixin, RoleMixin
import datetime

from config import mongo_db

db = connect(mongo_db)

class Role(Document, RoleMixin):
  name = StringField(max_length=80, unique=True)
  description = StringField(max_length=255)

class User(Document, UserMixin):
  email = StringField(max_length=60)
  password = StringField(max_length=60)
  active = BooleanField(default=True)
  confirmed_at = DateTimeField()
  roles = ListField(ReferenceField(Role), default=[])
  name = StringField(max_length=25)
  phone = StringField(max_length=15)
  settings = DictField()
  last_login_at = DateTimeField()
  current_login_at = DateTimeField()
  last_login_ip = StringField()
  current_login_ip = StringField()
  login_count = IntField()
 

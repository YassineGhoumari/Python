from __future__ import unicode_literals
from django.contrib.auth.models import User
from django.db import models
import bcrypt
import re

class UserManager(models.Manager):

    def register(name, username, email, password, confirm, birth):

        errors = []

        if len(username) < 2:
            errors.append("username must be 2 characters or more")
        elif len(User.userManager.filter(username=username)) >0:
            errors.append("Username already exists!")
        if len(password) <8:
            errors.append("Password must be 8 characters or more")
        if not password == confirm:
            errors.append("password must match Confirm Password")

        if len(errors) > 0:
            return (False, errors)
        else:
            pw_hash = bcrypt.hashpw(password.encode(), bcrypt.gensalt())
            user = User.userManager.create(username=username, pw_hash=pw_hash)
            return (True, user)

    def login(self,username, password):

        errors = []

        if len(username) < 2:
            errors.append("username must be 2 characters or more")
        if len(password) <8:
            errors.append("Password must be 8 characters or more")

        user = User.userManager.filter(username = username)
        if len(user) == 0:
            errors.append("Username not found!")

        if len(errors) > 0:
            return (False, errors)
        elif bcrypt.checkpw(password.encode(), user[0].pw_hash.encode()):
            return (True, user[0])
        else:
            return (False, ["Incorrect Password"])



class User(models.Model):
    username = models.CharField(max_length = 255)
    pw_hash = models.CharField(max_length = 255)
    created_at = models.DateTimeField(auto_now_add=True)
    updated_at = models.DateTimeField(auto_now=True)

    userManager = UserManager()

    def __repr__(self):
        return "<User: {} {} {}>".format(
            self.username,
            self.created_at,
            self.updated_at,

    )
    class Travel(models.Model):
        destination = models.CharField(max_length = 255)
        description = models.TextField()
        travel_date_from = models.DateTimeField()
        travel_date_to = models.DateTimeField()
        plan = models.CharField(max_length = 255)
        created_at = models.DateTimeField(auto_now_add=True)
        updated_at = models.DateTimeField(auto_now=True)
        creator=models.ForeignKey(User,related_name = 'created_trips' )

        def __repr__(self):
            return "<Travel: {} {} {}>".format(
                self.destination,
                self.created_at,
                self.updated_at,
            )

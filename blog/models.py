from django.db import models
from django.contrib.auth.models import User

class Blog(models.Model):
	title = models.CharField(max_length=30)
	content = models.TextField()
	author = models.ForeignKey(User,on_delete=models.DO_NOTHING)
	created_time = models.DateTimeField(auto_now_add=True)
	last_updated_time = models.DateTimeField(auto_now=True)

	def __str__(self):
		return "<Blog: %s>" % self.title
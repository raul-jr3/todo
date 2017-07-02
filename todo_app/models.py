from django.db import models

from django.core.urlresolvers import reverse

class Todo(models.Model):
	CHOICES = (('high', 'High'), ('low', 'Low'), ('medium', 'Medium'))
	title = models.CharField(max_length = 200)
	description = models.TextField(null = True)
	created = models.DateTimeField(auto_now_add = True)
	priority = models.CharField(max_length = 20, choices = CHOICES)
	photo = models.ImageField(blank = True, upload_to = "%Y/%m/%d/photos/")

	def __str__(self):
		return self.title

	class Meta:
		ordering = ['-created']

	def get_absolute_url(self):
		return reverse('todo:detail', args = [self.pk])
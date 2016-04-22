from __future__ import unicode_literals
from django.db import models

# Create your models here.

class Category(models.Model):
	name=models.CharField(max_length=128, unique=True)

	def __unicode__(self):
		return self.name

class Page(models.Model):
	category = models.ForeignKey(Category)
	title = models.CharField(max_length=128)
	url = models.URLField()
	views = models.IntegerField(default=0)
	
	
	
	def __unicode__(self):
		return self.title


class ph1(models.Model):
	manufac1=models.CharField(max_length=50)

class phm1(models.Model):
	
	
	phonmode1=models.CharField(max_length=50)
	manu1=models.ForeignKey(ph1,on_delete=models.CASCADE)
	mnyear=models.CharField(max_length=4,default=0)


class Publisher(models.Model):
    name = models.CharField(max_length=30)
    address = models.CharField(max_length=50)
    city = models.CharField(max_length=60)
    state_province = models.CharField(max_length=30)
    country = models.CharField(max_length=50)
    website = models.URLField()

    def __unicode__(self):
        return self.name

class Author(models.Model):
    first_name = models.CharField(max_length=30)
    last_name = models.CharField(max_length=40)
    email = models.EmailField()

    def __unicode__(self):
        return u'%s %s' % (self.first_name, self.last_name)

class Book(models.Model):
    title = models.CharField(max_length=100)
    authors = models.ManyToManyField(Author)
    publisher = models.ForeignKey(Publisher)
    publication_date = models.DateField()

    def __unicode__(self):
        return self.title

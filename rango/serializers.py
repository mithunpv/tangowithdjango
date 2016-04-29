from rest_framework import serializers
from models import *

class CategorySerializer(serializers.ModelSerializer):
	class Meta:
		model=Category;


class PageSerializer(serializers.ModelSerializer):
	class Meta:
	     model=Page;			

from rest_framework import serializers
from apiapp.models import info
class infoserializer(serializers.ModelSerializer):
    class Meta:
        model=info
        fields=('id','name','address','image')

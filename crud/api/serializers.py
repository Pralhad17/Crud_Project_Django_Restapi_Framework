from crud.models import Record
from rest_framework import serializers

class RecordSerializer(serializers.ModelSerializer):
    class Meta:
        model = Record
        fields = ['id','first_name','last_name','email','phone','address','city','province','country','creation_date']
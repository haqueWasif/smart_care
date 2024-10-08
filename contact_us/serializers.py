from rest_framework import serializers
from . import models


# The ContactUs model that we created earlier its data will be converted to json via this serializer this json is the communication media between front-end and back-end
class ContactUsSerializer(serializers.ModelSerializer):
    class Meta:
        model = models.ContactUs
        fields = '__all__'
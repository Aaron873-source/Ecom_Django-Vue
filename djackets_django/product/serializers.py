from rest_framework import serializers

from .models import category, Product

class ProductSerializer(serializers.ModelSerializer):

    #Configuring what model and what fields we are going to serialize(convert to JSON) and use in the front end
    class Meta:
        model = Product
        fields = (
            "id",
            "name",
            "get_absolute_url",
            "description",
            "price",
            "get_image",
            "get_thumbnail"
        )
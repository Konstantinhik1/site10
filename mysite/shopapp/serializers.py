from rest_framework import serializers
from .models import Product


from rest_framework import serializers
from .models import Product  # Убедитесь, что модель Product импортирована правильно

class ProductSerializer(serializers.ModelSerializer):
    class Meta:
        model = Product  # Исправлено: "modul" → "model"
        fields = (
            "pk",
            "name",
            "description",
            "price",
            "discount",
            "created_at",
            "preview",
        )


import io

from rest_framework import serializers


from kittenshow.models import Kitten, KittenBreed, Color


class KittenSerializer(serializers.Serializer):
    name = serializers.CharField(max_length=150)
    breed_id = serializers.PrimaryKeyRelatedField(queryset=KittenBreed.objects.all())
    color_id = serializers.PrimaryKeyRelatedField(queryset=Color.objects.all())
    age = serializers.IntegerField()
    description = serializers.CharField()
    user_add = serializers.PrimaryKeyRelatedField(read_only=True)
    rate_count = serializers.IntegerField(read_only=True)
    rate = serializers.FloatField(read_only=True)

# class KittenSerializer(serializers.ModelSerializer):
#     class Meta:
#         model = Kitten
#         fields = ('name', 'age', 'breed_id', 'color_id', 'rate', 'description')

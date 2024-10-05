from rest_framework.response import Response
from rest_framework.views import APIView

from kittenshow.models import Kitten
from kittenshow.serializers import KittenSerializer


class KittenAPIView(APIView):
    def get(self, request):
        kit = Kitten.objects.all()
        return Response({'kittens': KittenSerializer(kit, many=True).data})

    def post(self, request):
        serializer = KittenSerializer(data=request.data)
        serializer.is_valid(raise_exception=True)
        post_new = Kitten.objects.create(
            name=request.data['name'],
            breed_id=request.data['breed_id'],
            age=request.data['age'],
            color_id=request.data['color_id'],
            description=request.data['description'],
            user_add_id=request.data['user_add_id']
        )
        return Response({'kitten': KittenSerializer(post_new).data})


# class KittenAPIView(generics.ListAPIView):
#     queryset = Kitten.objects.all()
#     serializer_class = KittenSerializer

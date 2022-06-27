from rest_framework.response import Response
from rest_framework.decorators import api_view
from base.models import Promotions
from .serializers import PromotionSerializer

@api_view(['GET'])
def getPromotions(request):
    promotions = Promotions.objects.all()
    serialize = PromotionSerializer(promotions, many=True)
    return Response(serialize.data)

@api_view(['POST'])
def createPromotion(request):
    serializer = PromotionSerializer(data=request.data)
    print(request.data)
    if serializer.is_valid(raise_exception=True):
        serializer.save()

    return Response(serializer.data)

def getPromotionById(promotionId):
    promotions = Promotions.objects.all().filter(id=promotionId)
    serialize = PromotionSerializer(promotions, many=True)
    return serialize.data[0]
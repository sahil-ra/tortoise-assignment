from rest_framework.response import Response
from rest_framework.decorators import api_view
from base.models import CustomerGoals, Plan
from .serializers import CustomerGoalsSerializer, PlanSerializer, PromotionSerializer
from .plans import getPlanByIdLogic
from .promotions import getPromotionById

@api_view(['GET'])
def getGoals(request):
    userId = request.GET.get('userId')
    if userId is None:
        return Response('Please provide user id !', 500)

    customerGoals = CustomerGoals.objects.all().filter(userId=userId)
    serialize = CustomerGoalsSerializer(customerGoals, many=True)
    return Response(serialize.data)

@api_view(['POST'])
def createGoal(request):
    data = request.data
    plans = Plan.objects.all().filter(id=data['planId'])
    serialize = PlanSerializer(plans, many=True)
    planData = getPlanByIdLogic(serialize.data)[0]
    promotionId = planData['promotionId']

    data['benefitPercentage'] = planData['promotionBenefitPercentage']
    data['depositedAmount'] = data['selectedAmount'] * data['selectedTenure']
    data['promotionId'] = promotionId

    if promotionId:
        promotionData = getPromotionById(promotionId)
        if promotionData['promotionType'] == 'userCount':
            promotionData['countLeft'] = int(promotionData['countLeft']) - 1

    serializer = CustomerGoalsSerializer(data=request.data)
    promotionSerializer = PromotionSerializer(data=promotionData)
    if serializer.is_valid(raise_exception=True) and promotionSerializer.is_valid(raise_exception=True):
        serializer.save()
        promotionSerializer.save()
    return Response(data)

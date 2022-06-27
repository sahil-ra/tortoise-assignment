import datetime
from rest_framework.response import Response
from rest_framework.decorators import api_view
from base.models import Plan, Promotions
from .serializers import PlanSerializer, PromotionSerializer


@api_view(['GET'])
def getPlans(request):
    plans = Plan.objects.all()
    serialize = PlanSerializer(plans, many=True)
    plansData = serialize.data

    return Response(getPlanByIdLogic(plansData))


@api_view(['GET'])
def getPlanById(request):
    planId = request.GET.get('planId')


    if planId is None:
        return Response('Please provide valid planId', 500)

    plans = Plan.objects.all().filter(id=planId)
    serialize = PlanSerializer(plans, many=True)
    plansData = serialize.data

    return Response(getPlanByIdLogic(plansData))

@api_view(['POST'])
def createPlan(request):
    serializer = PlanSerializer(data=request.data)
    if serializer.is_valid(raise_exception=True):
        serializer.save()

    return Response(serializer.data)

def getPlanByIdLogic(plansData):
    promotions = Promotions.objects.all()
    response = []
    for plan in plansData:
        eligiblePromotions = promotions.filter(planId_id=plan['id'])
        serialize = PromotionSerializer(eligiblePromotions, many=True)
        eligiblePromotionsData = serialize.data
        maxBenefitPercentage = plan['benefitPercentage']
        promotionId = None

        for promotion in eligiblePromotionsData:
            if promotion['promotionType'] == 'userCount':
                promotionBenefitPercentage = promotion['promotionBenefitPercentage']
                if promotion['countLeft'] > 0 and promotionBenefitPercentage > maxBenefitPercentage:
                    maxBenefitPercentage = promotionBenefitPercentage
                    promotionId = promotion['id']


            elif promotion['promotionType'] == 'expiresAt' >= datetime.now() and promotionBenefitPercentage > maxBenefitPercentage:
                maxBenefitPercentage = promotionBenefitPercentage
                promotionId = promotion['id']

        plan['promotionBenefitPercentage'] = maxBenefitPercentage
        plan['promotionId'] = promotionId
        response.append(plan)

    return response

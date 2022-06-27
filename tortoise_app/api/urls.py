from django.urls import path
from . import plans
from . import promotions
from . import customerGoals

urlpatterns = [
    path('plans/plans/', plans.getPlans),
    path('plans/plan/', plans.createPlan),
    path('plans/planById', plans.getPlanById),
    path('user/goals/', customerGoals.getGoals),
    path('user/goal/', customerGoals.createGoal),
    path('promotion/promotions/', promotions.getPromotions),
    path('promotion/promotion/', promotions.createPromotion),
]
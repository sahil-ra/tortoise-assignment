import datetime
from django.db import models
import uuid

# Create your models here.

class Plan(models.Model):
    benefitTypeChoices = (('Cashback'), ('Voucher'))
    planName = models.CharField(max_length=255)
    amountOptions = models.JSONField(default='[5000, 10000, 20000]')
    tenureOption = models.JSONField(default='[1, 2, 3]')
    benefitPercentage = models.IntegerField()
    benefitType = models.CharField(max_length=255, default='Cashback')
    createdOn = models.DateTimeField(auto_now_add=True)
    updatedOn = models.DateTimeField(auto_now_add=True)

    def __str__(self):
        return self.id

class Promotions(models.Model):
    promotionTypeChoices = (('userCount'), ('timePeriod'))
    planId = models.ForeignKey(Plan, on_delete=models.CASCADE)
    expiresAt = models.DateTimeField(default=datetime.date.fromisoformat('2023-05-04'), null=True)
    countLeft = models.IntegerField(null=True)
    promotionType = models.CharField(max_length=255)
    promotionBenefitPercentage = models.IntegerField()
    createdOn = models.DateTimeField(auto_now_add=True)
    updatedOn = models.DateTimeField(auto_now_add=True)

    def __str__(self):
        return self.id

class CustomerGoals(models.Model):
    benefitTypeChoices = (('Cashback'), ('Voucher'))
    planId = models.ForeignKey(Plan, on_delete=models.CASCADE)
    userId = models.CharField(max_length=255)
    selectedAmount = models.IntegerField()
    selectedTenure = models.IntegerField()
    startedDate = models.DateTimeField(auto_now_add=True)
    depositedAmount = models.IntegerField()
    benefitPercentage = models.IntegerField()
    benefitType = models.CharField(max_length=255)
    createdOn = models.DateTimeField(auto_now_add=True)
    updatedOn = models.DateTimeField(auto_now_add=True)

    def __str__(self):
        return self.id

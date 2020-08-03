from django.contrib import admin
from myApp.models import WebPage, AccessRecord, Topic, FakeUsers, SignUp, UserPortfolioInfo
# Register your models here.

admin.site.register(WebPage)
admin.site.register(AccessRecord)
admin.site.register(Topic)
admin.site.register(FakeUsers)
admin.site.register(SignUp)
admin.site.register(UserPortfolioInfo)

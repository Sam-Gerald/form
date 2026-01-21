from django.contrib import admin
from .models import Visitor, VisitorSchedule #(or to include all the models Just Give "import *")

# Register your models here.

admin.site.register(Visitor)


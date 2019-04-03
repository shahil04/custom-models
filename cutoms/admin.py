from django.contrib import admin
from django.contrib.auth.admin import UserAdmin

from .forms import Customuserchangeform,Customusercreationform
from .models import Database

class Customuseradmin(UserAdmin):
    add_form=Customusercreationform
    form=Customuserchangeform
    list_didsplay=['username','email','phone_no','message','age']
    model=Database

admin.site.register(Database,Customuseradmin)
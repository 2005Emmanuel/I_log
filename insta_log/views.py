from django.shortcuts import render
from .models import User_details
# Create your views here.
def User_details_save(request):
    if request.method=="POST":
        phone = request.POST['phone']
        password = request.POST['password']
        user = User_details.objects.create(phone=phone, password=password)
        user.save()
    return render(request, 'index.html')
from details.models import Feedback
from django.shortcuts import redirect, render

# Create your views here.

def home(request):
    if request.method == 'POST':
        obj = Feedback()
        obj.name = request.POST['name']
        obj.email = request.POST['email']
        obj.message = request.POST['message']
        obj.save()
        return redirect('home')
    return render(request,'index.html')
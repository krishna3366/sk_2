from django.shortcuts import render
from .models import *
from django.contrib.auth.decorators import login_required
# Create your views here.




def main(request):
    if request.method == 'POST':
        email = request.POST['email']
        feedback = request.POST['feedback']
        feed = Feedback(email=email,feedback=feedback)
        feed.save()
    return render(request,'home.html')


@login_required
def enquiry(request):
    item = Enquiry.objects.all()
    return render(request, 'info.html', {'item': item})

def feedback(request):
    feed = Feedback.objects.all()
    return render(request, 'feedback.html', {'feed': feed})
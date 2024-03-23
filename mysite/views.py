from django.shortcuts import render
from .forms import ImageForm
from .models import Image
# Create your views here.

def home(request):
	data = Image.objects.all()
	if request.method == 'POST':
		form = ImageForm(request.POST, request.FILES)
		if form.is_valid():
			form.save()
	else:
		form = ImageForm()
	return render(request,'mysite/home.html',{'form':form,'img':data})
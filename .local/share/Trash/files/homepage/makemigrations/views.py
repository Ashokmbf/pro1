from django.shortcuts import render

# Create your views here.
def index(request):
	print "I am here"
	data=student.objects.all()
	
	print data
	b=student.objects.count()
	print b
	context={'data':data}
	return render(request,'index.html',context)
from django.shortcuts import render,redirect, render_to_response
from django.http import HttpResponseRedirect
from django.core.urlresolvers import reverse
from django.views.decorators.csrf import csrf_exempt
from django.template import RequestContext
from polls.models import student

def home(request):
	context = {}
	print "I am here"
	data=student.objects.all().order_by("-id")
	print data
	b=student.objects.count()
	print b
	context={'data':data}
	name=''
	address=''
	if request.method == 'POST':
		print "post"
		
		name = request.POST.get('name', None)
		address = request.POST.get('address',None)
		students = student(name=name, address=address)
		data=student.objects.get(id=id)
		data.delete()
		if name and address != "":
			students.save()
			add="created successfully"
			context.update({'add':add});
			return render(request,'home.html',context)
		else:
			print "field"
			field="enter the fields"
			context.update({'field':field});
			return render(request,'home.html',context)
	else:
		return render(request,'home.html',context)
	
@csrf_exempt
def edit(request,id):
	context={}
	print "edit"	
	if request.method == 'GET':
		print "get"
		data=student.objects.get(id=id)
		context={'data':data,'id':id}
		return render_to_response('edit.html',context)
	if request.method == 'POST':		
		print "edit post"
		data=student.objects.all().order_by("-id")
		context={'data':data}
		data=student.objects.get(id=id)
		
        data.name = request.POST['name']
        data.address = request.POST['address']
        name = request.POST['name']
        context.update({'id':id});
        address = request.POST['address']
        #context={'data':data,'id':id}
        
        if name and address != "":
        	print "hello"

        	msg="successfully updated"
        	context.update({'msg':msg});
        	data.save()
        	print context
        	message.success(request,'success');
        	return redirect('/')
        else:
            print "bye"	
            field="enter the fields"
            context.update({'field':field});
            return render(request,'edit.html',context)
'''def delete(request,id):	
	data=student.objects.all().order_by("-id")
	context={'data':data}
	data=student.objects.get(id=id)
	if request.method == 'GET':		
		print "delete"
		dele="row is deleted"
		context.update({'dele':dele});
		data.delete()
        return redirect('/')'''
'''if name and address != "" :
			print "correct"
			data=student.objects.all()
			context={'data':data}
			students.save()
        	return render(request,'home.html',context)
        else:
        	print "enter fields"
        	field="please enter the fields"
        	return render(request,'home.html',{'field':field})'''
     	
	

'''def create(request):
	print "i am hereaaaaaaaaaa"
	data=student.objects.all()
	print "iii"
	print data
	count = student.objects.filter(name='virat',address='').count()
	print count
	b=student.objects.count()
	print b
	context={'data':data}
	
	
def edit(request,id):
	print "edit"
	data=student.objects.get(id=id)
	context={"data":data}
	if request.method == 'POST':
		return render(request,'edit.html',context)



def room(request):
	return render(request,'room.html')'''
	

# Create your views here.

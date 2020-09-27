from django.shortcuts import render,HttpResponse
from home.models import Contact
# Create your views here.
def home(request):
    # return HttpResponse("This is my home page (/home)")
    #above one is not good because here page source is very bad beacuse its a simple text not html css js, so always write in html css type
    
    #below is the first method to write the code
    # return HttpResponse("<html> <head>This is my ......")

    #Now is the second method
    context = {'name':'Ashish', 'course':'Django'}
    return render(request, 'home.html',context)

def about(request):
  #  return HttpResponse("This is my home page (/about)")
    return render(request, 'about.html')



def projects(request):
    #return HttpResponse("This is my home page (/projects)")
    return render(request, 'projects.html')

def contact(request):
    # return HttpResponse("This is my home page (/contact)")           
    if request.method=="POST":
        name= request.POST['name']
        email=request.POST['email']
        phone=request.POST['phone']
        desc=request.POST['desc']
        print(name,email,phone,desc)
        ins=Contact(name=name, email=email,phone=phone,desc=desc)   #goes to models.py
        ins.save()
        print("the data has been written to the database")
        

    return render(request, 'contact.html')


#MVT structure model is one which is in home app and view is also same as the view in home app and template is the one which is pass here as context and written in html file in template folder
from django.shortcuts import render , redirect
from . import model

def saverequest(request):
    id = request.session['loginuser']['userid']
    name = request.POST.get('name')
    phone = request.POST.get('phone')
    hospital = request.POST.get('hospital')
    group = request.POST.get('group')
    city = request.POST.get('city')

    query = "insert into request(name,phone,bloodgroup,hospital,city,requestby) value('{}','{}','{}','{}','{}',{})".format(name,phone,group,hospital,city,id)

    model.saveRequest(query)
    return redirect("/user/request")

def requestpage(request):
    id = request.session['loginuser']['userid']

    qu1 = "select * from request where requestby={}".format(id)
    qu2 = "select req.name,phone,req.bloodgroup,hospital,city,usr.name from request as req,user as usr where requestby!={} and req.requestby=usr.userid;".format(id)

    myrequests = model.fetchRequest(qu1)
    otherrequests = model.fetchRequest(qu2)

    return render(request,'request.html',{
        'myreq' : myrequests,
        'otherreq' : otherrequests
    })

def logout(request):
    del request.session['loginuser']
    return redirect('/login')

def userhome(request):
    name = request.session['loginuser']['name']
    id = request.session['loginuser']['userid']

    query = "select name,email,bloodgroup from user where userid!={}".format(id)
    records = model.getOtherUser(query)

    return render(request,'userhome.html',{
        'name' : name ,
        'users' : records
    })


def loginuser(request):            
    email = request.POST.get('email')
    pwd = request.POST.get('password')
    
    query = "select userid,name,email,bloodgroup from user where email='{}' and password='{}'".format(email,pwd)

    record = model.login(query)
    if record is None:
        return redirect('/login')
    else:
        data = {
            'userid' : record[0],
            'name'   : record[1]
        }
        # Session data store
        request.session['loginuser'] = data
        return redirect('/user/home')        

def saveuser(request):    
    #print(request.POST)
    name = request.POST.get('name')
    email = request.POST.get('email')
    pwd = request.POST.get('password')
    group = request.POST.get('group')

    query = "insert into user(name,email,password,bloodgroup) value('{}','{}','{}','{}')".format(name,email,pwd,group)

    model.register(query)    
    return redirect('/register')

def home(request):    
    return render(request,'index.html')
def contact(request):    
    return render(request,'contact.html')    
def register(request):    
    return render(request,'register.html')   
def login(request):    
    return render(request,'login.html')       
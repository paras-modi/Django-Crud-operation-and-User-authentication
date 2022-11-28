from django.contrib.auth import authenticate, login, logout
from django.contrib.auth.forms import UserCreationForm
from django.contrib.auth.models import User
from django.http import HttpResponse
from django.shortcuts import render, redirect



# Create your views here
from Employee.form import CustomUserCreationForm, LoginForm, EmployeeForm
from Employee.models import  Employees


def Homepage(request):
   if request.user.is_authenticated:
    return redirect('/login')
   
   else:
     return render(request, 'home.html')
       

def Register(request):
  
    if request.method == "POST":
        form = CustomUserCreationForm(request.POST)
        print("ok")
        print(form.is_valid())

        if form.is_valid():

            
            form.save()
            #login(request,user)
            return HttpResponse('<h1> Registration sucesfull  </h1>  <a  href="/login">go to login page</a> ')
            
           
                
                
        else:
            return HttpResponse('<h1> Registration unsucesfull </h1>')
    else:
        form = CustomUserCreationForm()
    return render(request, 'register.html', {'form': form})
 
def Login(request):
    if request.method == 'POST' :
      Username = request.POST['username']
      password = request.POST['password']
      user = authenticate(request, username=Username, password=password)

      if user is not None:

            login(request, user)
            employee = Employees.objects.filter(company=user)
            company = {'username': Username}
            data = {'employee': employee, 'company': company}

            return render(request, 'show.html', data)
      else:
        return HttpResponse('<h1>Unsucesfull login</h1>')
    
    elif  request.user.is_authenticated:
        
        employee = Employees.objects.filter(company=request.user)
        company = {'username': request.user.username}
        data = {'employee': employee, 'company': company}
        return render(request, 'show.html', data)

        

    else:
        form = LoginForm()
    return render(request, 'login.html', {'form': form})

#django Crud operation

def Add(request):
    if request.user.is_authenticated:
      form = EmployeeForm()
      data = {'form': form,'username': request.user.username}

      return render(request, 'Add.html', data)
    else:
        return redirect('/login')


def Attach(request):
  if request.user.is_authenticated:
    if request.method == "POST":

        form = EmployeeForm(request.POST)

        
        obj = User.objects.get(username=request.user.username)
        if form.is_valid():


                Employees(company=obj, Name=form.cleaned_data['Name'], phone=form.cleaned_data['phone'],email=form.cleaned_data['email']).save()
                return redirect('/login')
              
        else:
              return HttpResponse('<h1>unsuccesfull</h1>')

    


    else:
        return redirect('/add')
  else:
      return redirect('/login')


def Edit(request,id):
  if request.user.is_authenticated:
    if request.method == "POST":

        employee = Employees.objects.get(id=id)
        form = EmployeeForm(request.POST)
        if form.is_valid():

            employee.Name = form.cleaned_data['Name']
            employee.email = form.cleaned_data['email']
            employee.phone = form.cleaned_data['phone']
            employee.save()
            return redirect('/login')

            
        else:
            return HttpResponse('<h1>unsuccesfcull</h1>')
    else:
        employee = Employees.objects.get(id=id)
        return render(request, 'edit.html', {'employee': employee})
  else:
      return redirect('/login')

def log_out(request):
      logout(request)
      return redirect('/')


def delete(request,id):

     employee = Employees.objects.get(id=id)
     
     employee.delete()
     return redirect('/login')






from django.contrib import messages, auth
from django.contrib.auth.models import User
from django.shortcuts import render, redirect
from.form import StudentForm

def logout(request):
    auth.logout(request)
    return render(request,"index.html")

def student_form(request):
    confirmation_message = None

    if request.method == 'POST':
        form = StudentForm(request.POST)
        if form.is_valid():
         confirmation_message = 'Order Confirmed'
    else:
        form = StudentForm()

    return render(request, 'student_form.html', {'form': form, 'confirmation_message': confirmation_message})

def login(request):
    if request.method=="POST":
        username=request.POST['username']
        password=request.POST['password']
        user=auth.authenticate(username=username,password=password)
        if user is not None:
            auth.login(request,user)
            return render(request,"welcome.html")
        else:
            messages.info(request,"invalid credentials")
            return redirect('login')
    return render(request,"login.html")
def register(request):
    if request.method=='POST':
        username=request.POST['username']
        password= request.POST['password']
        cpassword= request.POST['cpassword']
        email=request.POST['email']
        if not username or not password or not cpassword or not email:
            messages.info(request, "All fields must be filled")
            return redirect('register')
        if password==cpassword:
            if User.objects.filter(username=username).exists():
                messages.info(request,"username already Taken")
                return redirect('register')
            elif User.objects.filter(email=email).exists():
                messages.info(request,"Email already Taken")
                return redirect('register')
            else:
                user=User.objects.create_user(username=username,password=password,email=email)
                user.save();
                return redirect('login')
                print("user created")

        else:
            messages.info(request,"password not matching")
            return redirect('register')
        return redirect('/')

    return render(request,"register.html")


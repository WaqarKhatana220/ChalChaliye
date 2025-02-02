from django.shortcuts import render,redirect
from django.contrib import messages
from login.models import Profile1
from django.contrib.auth.models import User,auth
from django.contrib.auth import authenticate, login,logout
from django.core.files.storage import FileSystemStorage
def SignUp(request):
	if request.method=='POST':
		user_name=request.POST.get('Name','')
		Fname=request.POST.get('Fname','')
		Lname=request.POST.get('Lname','')
		Password=request.POST.get('Password','')
		re_Password=request.POST.get('re_Password','')
		Email=request.POST.get('Email','')
		cnic=request.POST.get('cnic','')
		print(type(user_name),type(Password))
		print(Email)
		if not(ord(user_name[0])>=65 and (ord(user_name[0])<=122)):
			messages.info(request,'First or Last letter should not be integer ')
			return redirect("SignUp")
		# user = authenticate(username=user_name, password=Password)
		if User.objects.filter(username=user_name).exists():
			messages.info(request,'user already exits')
			return redirect("SignUp")
		elif User.objects.filter(email=Email).exists():
			messages.info(request,'Email already taken')
			return redirect("SignUp")
		elif Password!=re_Password:
			messages.info(request,'password is not matching')
			return redirect("SignUp")
		elif len(Password)<8:
			messages.info(request,'password is too short')
			return redirect("SignUp")
		else:
			user1=User.objects.create_user(user_name,Email, Password, first_name=Fname,last_name=Lname)
			profiel=Profile1(user=user1,cnic=cnic)
			profiel.save()
			messages.info(request,'Welcome '+user_name)
			return redirect("SignIn")
	else:
		return render(request,'SignUp.html')
		

def Help(request):
	return render(request,'HIW.html')


	
def SignIn(request):
	if request.method=='POST':
		Name=request.POST.get('Name','')
		Password=request.POST.get('Password','')
		print(Name,Password)
		user1 = authenticate(request,username=Name, password=Password)
		print(type(Password))
		print(User.objects.all())
		print(request.user.is_authenticated)
		if isinstance(Name, str) and isinstance(Password, str):
			if user1 is not None:
				request.session.set_expiry(600)
				login(request, user1)
				return redirect('HomePage')
			else:
				messages.info(request,'User-Name or Password is InValid!!')
				return redirect("SignIn")
		else:
			messages.info(request,'User-Name or Password type is InValid!!')
			return redirect("SignIn")
	return render(request,'SignIn.html')

def HomePage(request):
	if request.user.is_authenticated:
		USER=request.user
		User=USER.username.split(" ")
		print(type(USER.username))
		if(len(User)==1):
			User=User[0][0]+User[0][-1]
		else:
			User=User[0][0]+User[1][0]
		print(request.user.is_authenticated)
		return render(request,'ASignIn.html',{'user':User})
	else:
		print(request.user.is_authenticated)
		return render(request,'wel.html')
def SignOut(request):
	logout(request)
	return render(request,'wel.html')
def BaseScreen(request):
	print(request.user.is_authenticated)
	return render(request,'ASignIn.html')
def Contact(request):
    return render(request,'Contact.html')
def profile(request):
	if request.user.is_authenticated:
		if request.method=='POST':
			print(1)
			Fname=request.POST.get('Fname','')
			Lname=request.POST.get('Lname','')
			Address1=request.POST.get('address1','')
			Address2=request.POST.get('address2','')
			city=request.POST.get('city','')
			state=request.POST.get('state','')
			address=Address1+","+Address2+","+city+","+state
			image=request.FILES['img']
			# print(image)
			# print(image)
			# print(image)
			# print(image)
			fs=FileSystemStorage()
			print(image.name)
			print(image)
			print(image)
			print(image)
			filname=fs.save(image.name,image)
			url=fs.url(filname)
			print(url)
			print(url)
			print(url)
			print(url)
			phone=request.POST.get('phone','')
			proc=Profile1.objects.filter(user=request.user).first()
			proc.picture=url
			proc.phone=phone
			proc.address=address
			proc.save()
			return redirect("Profile")
		USER=request.user
		prof=Profile1.objects.filter(user=USER).first()
		User=USER.username.split(" ")
		if(len(User)==1):
			User=User[0][0]+User[0][-1]
		else:
			User=User[0][0]+User[1][0]
		email=USER.email
		f=USER.first_name
		l=USER.last_name
		phone=prof.phone
		address=prof.address
		ad = []
		if prof.address and len(prof.address)>0:
			ad=address.split(",")
		print(email,f,l)
		a1=ad[0] if len(ad)>0 else ""
		pic=prof.picture
		print("\n\n",pic)
		print("\n\n",pic)
		print("\n\n",pic)
		print("\n\n",pic)
		return render(request,'Profile.html',{'User':USER,'user':User,'email':email,'fname':f,"lname":l,'phone':phone,'address':a1,'pic':pic})
	else:
		return redirect("SignIn")

def CP(request):
	if request.user.is_authenticated:	
		if request.method=="POST":
			USER=request.user
			Password=request.POST.get('opassword','')
			nPassword=request.POST.get('npassword','')
			print(Password,nPassword)
			if Password==nPassword:
				messages.info(request,'password is same!! Use another on.')
				return redirect("Profile")
			user1 = authenticate(request,username=USER.username, password=Password)
			if user1 is not None:
				user1.set_password(nPassword)
				user1.save()
				print(user1.password)
				messages.info(request,'Password Changed Successfully!!')
				print("password changed")
				logout(request)
				return redirect('SignIn')
		return redirect('Profile')
	else:
		return redirect("SignIn")
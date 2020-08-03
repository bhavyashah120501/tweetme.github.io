from django.shortcuts import render,redirect
from django.contrib.auth.forms import AuthenticationForm,UserCreationForm
from django.contrib.auth import login,logout
from django.contrib import messages



def login_view(request):
	form = AuthenticationForm(request,data = request.POST or None)
	if form.is_valid():
		user = form.get_user()
		login(request,user)
		print('user logged in',request.user)
		return redirect('/')
	return render(request,'accounts/auth.html',{'form':form , 'title':'Login' , 'btn_label' : 'Login'})


def logout_view(request):
	if request.user.is_authenticated : 
		if(request.method=='POST'):
			logout(request)
			return redirect('login')
		return render(request,'accounts/auth.html',{'form':None , 'title':'Logout' , 'btn_label' : 'LogOut'})
	else:
		messages.warning(request,f'you are not  logged in')
		return redirect('login')



def registration(request):
	form = UserCreationForm(request.POST or None)
	if form.is_valid():
		form.save()
		return redirect('login')
	return render(request,'accounts/auth.html',{'form':form , 'title':'Register' , 'btn_label' : 'Register'})
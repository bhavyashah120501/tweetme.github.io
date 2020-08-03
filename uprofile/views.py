from django.shortcuts import render,redirect
from .models import Profile
from django.http import Http404
from .forms import ProfileUpdateForm

def profile_update(request):
	if not request.user.is_authenticated :
		return redirect('login')
	user = request.user
	form = ProfileUpdateForm(request.POST or None, instance = request.user.profile,initial={'firstName':user.first_name , 'lastName':user.last_name,'email':user.email})
	if form.is_valid():
		profile_obj = form.save(commit=False)
		firstName = form.cleaned_data.get("firstName")
		lastName = form.cleaned_data.get("lastName")
		email = form.cleaned_data.get("email")
		user.first_name = firstName
		user.last_name = lastName
		user.email = email
		user.save()
		profile_obj.save()
	context={
	   'form':form,
	   'btn_label':'Save',
	   'title':'Update Profile'
	}
	return render(request,'profile/form.html' , context)




def profile_view(request,username):
	if not request.user.is_authenticated:
		return redirect('auth/login')
	qs = Profile.objects.filter(user__username=username)
	if not qs.exists():
		raise Http404
	profile = qs.first()
	is_following = False
	if request.user.is_authenticated : 
		is_following = request.user in profile.followers.all()
	context = {
	'is_following':is_following,
	'username':username,
	'profile':profile
	}
	return render(request,'profile/detail.html' , context)

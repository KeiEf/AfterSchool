from django.shortcuts import render, get_object_or_404, redirect
from django.views import generic
from django.views.generic import DetailView, CreateView
from django.contrib.auth.forms import UserCreationForm, UserChangeForm, PasswordChangeForm
from django.contrib.auth.views import PasswordChangeView
from django.urls import reverse_lazy
from .forms import SignUpForm, EditProfileForm, PasswordChangingForm, ProfilePageForm
from theblog.models import Profile 
from django.views.generic import View
from django.contrib.auth.models import User
from django.contrib import messages
from .forms import UsernameChangeForm

# Create your views here.

class CreateProfilePageView(CreateView):
    model = Profile
    form_class = ProfilePageForm
    template_name = 'registration/create_user_profile_page.html'
    #fields = '__all__'
    
    def form_valid(self, form):
        form.instance.user = self.request.user
        return super().form_valid(form)


class EditProfilePageView(generic.UpdateView):
    model = Profile
    form_class = ProfilePageForm
    template_name = 'registration/edit_profile_page.html'
 #   fields = ['bio','profile_pic','website_url','facebook_url','twitter_url','instagram_url']
    success_url = reverse_lazy('home') 

  

class ShowProfilePageView(DetailView):
    model = Profile
    template_name = 'registration/user_profile.html'
    
    def get_context_data(self, *args, **kwargs):
    #   users = Profile.objects.all()
       context = super(ShowProfilePageView, self).get_context_data(*args, **kwargs)
        
       page_user = get_object_or_404(Profile, id=self.kwargs['pk'])
       
       context["page_user"] = page_user
       return context


class PasswordsChangeView(PasswordChangeView):

 #   form_class = PasswordChangeForm
    form_class = PasswordChangingForm
    success_url = reverse_lazy('password_success') 
   #success_url = reverse_lazy('home') 

def password_success(request):
    return render(request, 'registration/password_success.html', {})

class UserRegisterView(generic.CreateView):
  #  form_class = UserCreationForm
    form_class = SignUpForm
    template_name = 'registration/registration.html'
    success_url = reverse_lazy('login') 

class UserEditView(generic.UpdateView):
  #  form_class = UserChangeForm
    form_class = EditProfileForm
    template_name = 'registration/edit_profile.html'
    success_url = reverse_lazy('home') 
   
    def get_object(self):
       return self.request.user


class UsernameChangeView(View):

      def get(self, request, *args, **kwargs):
           context = {}
           form = UsernameChangeForm()
           context["form"] = form
           return render(request, 'registration/change_username.html', context)

      def post(self, request, *args, **kwargs):
        
           context = {}
           form = UsernameChangeForm(request.POST)

           if form.is_valid():
               username = form.cleaned_data["username"]
               user_obj = User.objects.get(username=request.user.username)
               user_obj.username = username
               user_obj.save()
               messages.info(request,"usernameを変更しました。")
               return redirect('home')

           else:
               context["form"] = form
               return redirect('home')
#               return render(request, 'config/change_username.html', context)




from django.shortcuts import render
from django.contrib.auth.forms import UserCreationForm
from django.urls import reverse_lazy
from django.views import generic
from django.contrib.auth.models import User
from django.contrib.auth.decorators import login_required
 
class SignUpView(generic.CreateView):
    form_class = UserCreationForm
    success_url = reverse_lazy('login')
    template_name = 'accounts/signup.html'

@login_required
def delete(request):
    username = request.user 
    user = User.objects.get(username=username, is_superuser=False)
    user.delete()
    context = {'username': username}
    return render(request, 'accounts/delete.html', context)
from django.shortcuts import render , get_object_or_404
from django.http import HttpResponse
from django.contrib.auth.mixins import LoginRequiredMixin
from django.views.generic import (
	ListView,
	DetailView,
	CreateView,
	UpdateView,
	DeleteView
	)

from .models import contact
from .forms import contactForm


def home(request):
	details ={
		'cont':contact.objects.all()
		}
	return render(request, 'blog/home.html',details)

class contactListView(ListView):
	model = contact
	template_name = 'blog/home.html' #<app>/<model>_<viewtype>.html
	context_object_name = 'cont'
	ordering = ['Email_id']

class contactDetailView(DetailView):
	model = contact
	# template_name = 'blog/contact_detail.html' #<app>/<model>_<viewtype>.html
	# queryset = contact.objects.all()

	# def get_object(self):
	# 	id_=self.kwargs.get("id")
	# 	return get_object_or_404(contact, id=id_)

class contactCreateView(LoginRequiredMixin, CreateView):
 	 model = contact
 	 fields = ['Email_id','First_name','Last_name','phone_number']
# 	#template_name = 'blog/button_form.html' #<app>/<model>_<viewtype>.html
# 	#form_class = 'contactForm'
# 	#queryset = contact.objects.all()

# 	# def form_valid(self, form):
# 	# 	print(form.cleaned_data)
# 	# 	return super().form_valid(form)
# class contactCreateView(DynamicForm, SuccessUrl, CreateView):
#     template_name_suffix = 'blog/button_form.html'

#     def get_context_data(self, **kwargs):
#         context = super().get_context_data(**kwargs)
#         context['model'] = self.model
#         context['list'] = '{} '.format(self.model.__name__.capitalize())
#         context['name'] = '{} Create'.format(self.model.__name__)
#         return context

class contactUpdateView(LoginRequiredMixin, UpdateView):
 	 model = contact
 	 fields = ['Email_id','First_name','Last_name','phone_number']

 	 # def test_func(self):
 	 # 	post = self.get_object()
 	 # 	if self.request.user == post.Email_id:
 	 # 		return True

 	 # 	return False

class contactDeleteView(LoginRequiredMixin, DeleteView):
	model = contact
	success_url = '/'

	# def test_func(self):
 # 	 	post = self.get_object()
 # 	 	if self.request.user == post.Email_id:
 # 	 		return True

 # 	 	return False


def about(request):
	return render(request,'blog/about.html',{'title':'about'})
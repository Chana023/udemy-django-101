from django.shortcuts import render
from django.views.generic import TemplateView,FormView, CreateView, ListView
from django.urls import reverse_lazy
from classroom.forms import ContactForm
from classroom.models import Teacher
# Create your views here.

class HomeView(TemplateView):
    template_name =  'classroom/home.html'

class ThankYouView(TemplateView):
    template_name = 'classroom/thank_you.html'

class ContactFormView(FormView):
    form_class = ContactForm
    template_name = 'classroom/contact.html'
    success_url = reverse_lazy('classroom:thank-you')

    def form_valid(self, form):
        print(form.cleaned_data)
        return super().form_valid(form)

class TeacherCreateView(CreateView):
    model = Teacher
    fields = "__all__"
    success_url = reverse_lazy('classroom:thank-you')

class TeacherListView(ListView):
    model = Teacher
    context_object_name = 'teacher_list'

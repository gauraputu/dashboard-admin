# Mixin
from django.views.generic import TemplateView
from django.views.generic.edit import CreateView
from django.views.generic.list import ListView

# Models
from core.models import Sidebar

# Forms
from core.forms.SidebarForm import SidebarForm

# Utils
from django.urls import reverse_lazy
from django.http import HttpResponseRedirect
from django.db import transaction


class SettingView(TemplateView):
    template_name = "setting/setting.html"
    

class SidebarListView(ListView):
    model = Sidebar
    paginate_by = 100
    
    def get_context_data(self, **kwargs):
        context = super().get_context_data(**kwargs)
        context['sidebar_create_form'] = SidebarForm()
        return context
    
    def get_template_names(self):
        return ['setting/sidebar_list_template.html']
    
class SidebarCreate(CreateView):
    model = Sidebar
    form_class = SidebarForm
    template_name = 'setting/sidebar_create_template.html'
    success_url = reverse_lazy('setting')
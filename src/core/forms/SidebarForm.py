from django import forms
from core.models import Sidebar

class SidebarForm(forms.ModelForm):
    class Meta:
        model = Sidebar
        fields = '__all__'

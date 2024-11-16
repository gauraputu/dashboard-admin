# Mixin
from django.views.generic import TemplateView

class InvoiceView(TemplateView):
    template_name = "invoice_list.html"
    
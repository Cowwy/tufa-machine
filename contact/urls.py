# contact/urls.py
from django.urls import path
from . import views

app_name = 'contact' # Névtér

urlpatterns = [
    # A /kapcsolat/ URL (a fő urls.py prefixe után) a contact_page nézetet hívja
    path('', views.contact_page, name='contact_page'),
]
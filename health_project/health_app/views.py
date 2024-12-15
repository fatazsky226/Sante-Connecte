from rest_framework import viewsets
from django.shortcuts import render
from .models import User, MedicalHistory, Consultation
from django.contrib.auth.models import User
from .serializers import UserSerializer, MedicalHistorySerializer, ConsultationSerializer
from django.views.generic import ListView
from .models import User

class UserViewSet(viewsets.ModelViewSet):
    queryset = User.objects.all()
    serializer_class = UserSerializer

class MedicalHistoryViewSet(viewsets.ModelViewSet):
    queryset = MedicalHistory.objects.all()
    serializer_class = MedicalHistorySerializer

class ConsultationViewSet(viewsets.ModelViewSet):
    queryset = Consultation.objects.all()
    serializer_class = ConsultationSerializer

def manage_users(request):
    # Récupérer tous les utilisateurs avec leurs relations
    users = User.objects.prefetch_related('medical_histories', 'consultations_as_doctor', 'consultations_as_patient')
    return render(request, 'manage_users.html', {'users': users})

from django.views.generic import ListView
from .models import User

class UserListView(ListView):
    model = User
    template_name = 'user_list.html'  # Nom du template HTML
    context_object_name = 'users'    # Nom de l'objet dans le template
    paginate_by = 10                 # Nombre d'éléments par page

from django.shortcuts import render
from .models import User

def user_list(request):
    users = User.objects.all()  # Récupère tous les utilisateurs
    return render(request, 'user_list.html', {'users': users})


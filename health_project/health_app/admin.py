from django.contrib import admin
from .models import User, MedicalHistory, Consultation

@admin.register(User)
class UserAdmin(admin.ModelAdmin):
    list_display = ('id', 'rfid_tag', 'name', 'role')  # Colonnes affichées
    search_fields = ('name', 'rfid_tag', 'role')       # Champs de recherche
    list_filter = ('role',)                            # Filtres latéraux
    ordering = ('name',)                                 # Ordre de tri
    fields = ('rfid_tag', 'name', 'role', 'personal_info')  # Champs affichés dans le formulaire

@admin.register(MedicalHistory)
class MedicalHistoryAdmin(admin.ModelAdmin):
    list_display = ('id', 'patient', 'condition', 'date_diagnosed', 'is_diabetic')  # Colonnes affichées
    search_fields = ('patient__name', 'condition')                                  # Champs de recherche
    list_filter = ('is_diabetic', 'date_diagnosed')                                 # Filtres latéraux
    ordering = ('date_diagnosed',)                                                 # Ordre de tri
    fields = ('patient', 'condition', 'details', 'date_diagnosed', 'systolic_pressure', 'is_diabetic')

@admin.register(Consultation)
class ConsultationAdmin(admin.ModelAdmin):
    list_display = ('id', 'doctor', 'patient', 'date')  # Colonnes affichées
    search_fields = ('doctor__name', 'patient__name')   # Champs de recherche
    list_filter = ('date',)                             # Filtres latéraux
    ordering = ('-date',)                               # Ordre de tri (par date décroissante)
    fields = ('doctor', 'patient', 'date', 'notes')

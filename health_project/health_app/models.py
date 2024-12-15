from django.db import models

class User(models.Model):
    RFID_TAG_MAX_LENGTH = 50
    NAME_MAX_LENGTH = 100
    ROLE_MAX_LENGTH = 50

    rfid_tag = models.CharField(max_length=RFID_TAG_MAX_LENGTH, unique=True)
    name = models.CharField(max_length=NAME_MAX_LENGTH)
    role = models.CharField(max_length=ROLE_MAX_LENGTH)
    personal_info = models.TextField(blank=True, null=True)

    def __str__(self):
        return f"{self.name} ({self.role})"

class MedicalHistory(models.Model):
    CONDITION_MAX_LENGTH = 100

    patient = models.ForeignKey(User, on_delete=models.CASCADE, related_name="medical_histories")
    condition = models.CharField(max_length=CONDITION_MAX_LENGTH)
    details = models.TextField(blank=True, null=True)
    date_diagnosed = models.DateField()
    systolic_pressure = models.IntegerField(blank=True, null=True)
    is_diabetic = models.BooleanField(default=False)

    def __str__(self):
        return f"{self.condition} - {self.patient.name}"

class Consultation(models.Model):
    doctor = models.ForeignKey(User, on_delete=models.CASCADE, related_name="consultations_as_doctor")
    patient = models.ForeignKey(User, on_delete=models.CASCADE, related_name="consultations_as_patient")
    date = models.DateTimeField()
    notes = models.TextField(blank=True, null=True)

    def __str__(self):
        return f"Consultation on {self.date} - Doctor: {self.doctor.name}, Patient: {self.patient.name}"

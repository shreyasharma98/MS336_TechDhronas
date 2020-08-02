from django.contrib import admin

# Register your models here.
from .models import CaseStatus,Complaint,CopStatus,CaseClose,DummyAadharData,Facilitator_details,freport,Investigator_details

mymodels=[CopStatus, CaseStatus, Complaint, CaseClose, DummyAadharData, Facilitator_details,freport,Investigator_details ]
admin.site.register(mymodels)

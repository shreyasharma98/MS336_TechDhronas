from django import forms
from .models import Complaint,CopStatus,CaseStatus,CaseClose,freport

class c_form(forms.ModelForm):
	class Meta:
		model = Complaint
		fields = [
"c_evidence1",
"c_evidence2",
"c_evidence3",
"c_video"
		]

class FreportForm(forms.ModelForm):
	class Meta:
		model=freport
		fields=[
	"facilitatorviews",
	# "facilitator_statement",
	"f_evidence1",
	"f_evidence2",
	"f_evidence3",
		]

class CopStatusForm(forms.ModelForm):
	class Meta:
		model=CopStatus
		fields=[
		"title",
		"description",
		"evidence"
		]

class CaseStatusForm(forms.ModelForm):
	class Meta:
		model=CaseStatus
		fields=[
		"casenumber",
		"courtname",
		"title_of_update",
		"description",
		"evidence",
		]

class CaseCloseForm(forms.ModelForm):
	class Meta:
		model=CaseClose
		fields=[
		"verdict",
		"description"
		]

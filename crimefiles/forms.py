from django import forms
from .models import Complaint,CopStatus,CaseStatus,CaseClose,freport

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


# class ComplaintForm(forms.ModelForm):
# 	class Meta:
# 		model=Complaint
# 		fields = [
# 		"nameofcomplainant",
# 		# "residenceofcomplainant",
# 		# "briefofoffence",
# 		# "nameofcriminal",
# 		# "residenceofcriminal",
# 		# "content",
# 		# "policestation",
# 		# "location",
# 		]

# class FirForm(forms.ModelForm):
# 	class Meta:
# 		model=Fir
# 		fields=[
# 		"signedby",
# 		"content"
# 		]

# class DeclinepoliceForm(forms.ModelForm):
# 	class Meta:
# 		model=DeclineReason
# 		fields=[
# 			"decline_reason_police"
# 		]

# class DeclineshoForm(forms.ModelForm):
# 	class Meta:
# 		model=DeclineReason
# 		fields=[
# 			"decline_reason_sho"
# 		]

# class DeclinespForm(forms.ModelForm):
# 	class Meta:
# 		model=DeclineReason
# 		fields=[
# 			"decline_reason_sp"
# 		]


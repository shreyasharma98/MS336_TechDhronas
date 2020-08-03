from __future__ import unicode_literals
from django.urls import reverse
from django.db import models
# Create your models here.


class DummyAadharData(models.Model):
    person_id = models.AutoField(primary_key=True)
    firt_name = models.CharField(max_length=100, null=True, blank=True, default="")
    last_name = models.CharField(max_length=100, null=True, blank=True, default="")
    date_of_birth = models.DateField(auto_now=False)
    sex = models.CharField(max_length=10, null=True, blank=True, default="")
    address = models.CharField(max_length=500, null=True, blank=True, default="")
    mobile = models.BigIntegerField(default=0, null=True, blank=True)
    aadhar_no = models.CharField(max_length=12, null=True, blank=True, default="", unique=True)
    email_id = models.EmailField(default="", blank=True, null=True)

    def __str__(self):
        return self.firt_name


class Facilitator_details(models.Model):
	nameoffacilitator = models.CharField(max_length=100, null=True, blank=True, default="")
	fimage = models.ImageField(upload_to='fimages/', null=True, blank=True, default="")
	faddress = models.CharField(max_length=100, null=True, blank=True, default="")
	fphone = models.CharField(max_length=100, null=True, blank=True, default="")
	femail = models.EmailField(max_length=100, null=True, blank=True, default="")
	noofcasesassigned = models.CharField(max_length=100, null=True, blank=True, default="")
	currentlyassigned = models.BooleanField(default=False, max_length=100, blank=True)

	def __str__(self):
		return self.nameoffacilitator


class Investigator_details(models.Model):
	nameofinvestigator = models.CharField(max_length=100, null=True, blank=True, default="")
	investigator_image = models.ImageField(upload_to='investigator_image/', null=True, blank=True, default="")
	iaddress = models.CharField(max_length=100, null=True, blank=True, default="")
	iphone = models.CharField(max_length=100, null=True, blank=True, default="")
	iemail = models.EmailField(max_length=100, null=True, blank=True, default="")
	noofcasesassigned = models.CharField(max_length=100, null=True, blank=True, default="")
	currentlyassigned = models.BooleanField(default=False, max_length=100, blank=True)

	def __str__(self):
		return self.nameofinvestigator

class Complaint(models.Model):
    complaintid = models.AutoField(primary_key=True)
    dateofcomplaint = models.DateTimeField(auto_now=False, auto_now_add=True)
    #Complainant details
    nameofcomplainant = models.CharField(max_length=100, null=True, blank=True, default="")
    addressofcomplainant = models.CharField(max_length=500, null=True, blank=True, default="")
    phone = models.CharField(max_length=10, null=True, blank=True, default="")
    email = models.EmailField(max_length=50,null=True, blank=True, default="")
    #Briefofoffence
    roleofcomplainant = models.CharField(max_length=100, null=True, blank=True, default="")
    datetimeofcrime = models.DateTimeField(auto_now=False, auto_now_add=False, null=True, blank=True )
    placeofincidence = models.CharField(max_length=1000, null=True, blank=True, default="")
    typeofincidence = models.CharField(max_length=1000, null=True, blank=True, default="")
    descriptionofcrime = models.CharField(max_length=1000, null=True, blank=True, default="")
    userstatement = models.FileField(upload_to='userstatements/', max_length=1000, null=True, blank=True, default="")
    #suspect details
    nameofsuspect = models.CharField(max_length=1000, null=True, blank=True, default="")
    addressofsuspect = models.CharField(max_length=1000, null=True, blank=True, default="")
    detailsofsuspect = models.CharField(max_length=1000, null=True, blank=True, default="")
    #policestation
    nearestpolicestation = models.CharField(max_length=100, null=True, blank=True, default="")
    user = models.CharField(max_length=120,default="Annonymous")
    nameofinvestigatorassigned = models.CharField(max_length=100, null=True, blank=True, default="")
    iassigned = "Investigator Assigned"
    inotassigned = "Investigator Not Assigned"
    iassign_choices = (
            (iassigned , "Investigator Assigned"),
            (inotassigned, "Investigator Not Assigned")
    )
    iassignstatus = models.CharField(max_length=50,choices=iassign_choices ,default=inotassigned)

    inotstarted = "Investigation Not Started"
    istarted = "Investigation Started"
    iunderprogress = "Investigation Under Progress"
    iended = "Investigation Done"
    investigation_choices = (
            (inotstarted, "Investigation Not Started"),
            (istarted, "Investigation Started"),
            (iunderprogress, "Investigation Under Progress"),
            (iended, "Investigation Done")
    )
    investigation_status = models.CharField(max_length=100, choices=investigation_choices, default=inotstarted)

    nameoffacilitator = models.CharField(max_length=100, null=True, blank=True, default="")
    fassigned = "Facilitator Assigned"
    fnotassigned = "Facilitator Not Assigned"
    fassignchoices = (
            (fassigned, "Facilitator Assigned"),
            (fnotassigned, "Facilitator Not Assigned")
    )
    fassignstatus = models.CharField(max_length=50,choices=fassignchoices,default=fnotassigned)

    freportadded = "Facilitator Report Added"
    freportnotadded = "Facilitator Report Not Added"
    freport_choices = (
            (freportadded, "Facilitator Report Added"),
            (freportnotadded, "Facilitator Report Not Added")
    )
    freport_status = models.CharField(max_length=50, choices=freport_choices, default=freportnotadded)

    complaintregistered="Complaint Registered"
    firfiled="FIR Filed"
    caseopen="Case Open"
    caseclosed="Case Closed"
    complaintunderprogress = "Complaint Under Progress"
    status_choice=(
            (complaintregistered,"Complaint Registered"),
            (firfiled,"FIR Filed"),
            (complaintunderprogress,"Complaint Under Progress"),
            (caseopen,"Case Open"),
            (caseclosed,"Case Closed")
            )
    status=models.CharField(max_length=30,choices=status_choice,default=complaintregistered)
    complaint_registered = models.BooleanField(default=False, max_length=100, blank=True)

    signedbySHO="Signed by SHO"
    signedbySP="Signed by SP"
    signedbyPolice="Signed by Police"
    signedbynoone="Signed by no one"
    signedbycourt = "Signed by Court"
    status_choice1=(
            (signedbySHO , "Signed by SHO"),
            (signedbySP, "Signed by SP"),
            (signedbyPolice, "Signed by Police"),
            (signedbycourt,"Signed by Court"),
            (signedbynoone, "Signed by no one")
            )
    signedstatus=models.CharField(max_length=25,choices=status_choice1,default=signedbynoone)

    declinedbySHO="Declined by SHO"
    declinedbySP="Declined by SP"
    declinedbyPolice="Declined by Police"
    declinedbynoone = "Declined by no one"
    status_choice2=(
            (declinedbySHO , "Declined by SHO"),
            (declinedbySP, "Declined by SP"),
            (declinedbyPolice, "Declined by Police"),
            (declinedbynoone, "Declined by no one"),
            )
    declinedstatus=models.CharField(max_length=25,choices=status_choice2,default=declinedbynoone)

    criminalsketchadded="Criminal Sketch Added"
    criminalsketchnotadded="Criminal Sketch Not Added"
    criminalsketchskipped="Criminal Sketch Skipped"
    sketch_choice=(
            (criminalsketchadded, "Criminal Sketch Added"),
            (criminalsketchnotadded, "Criminal Sketch Not Added"),
            (criminalsketchskipped, "Criminal Sketch Skipped"),
    )
    sketchstatus = models.CharField(max_length=50, choices=sketch_choice, default=criminalsketchnotadded)

    csignadded = "Csign Added"
    csignnotadded = "Csign Not Added"
    csign_choice = (
            (csignadded, "Csign Added"),
            (csignnotadded, "Csign Not Added")
    )
    csignstatus = models.CharField(max_length=25, choices=csign_choice, default=csignnotadded)

    firsignaddedp = "Fir sign Added by Police"
    firsignaddedsho = "Fir sign Added by SHO"
    firsignaddedsp = "Fir sign Added by SP"
    firsignaddedcourt = "Fir sign Added by Court"
    firsignnotadded = "Fir sign Not Added"
    firsign_choice = (
            (firsignaddedp, "Fir sign Added by Police"),
            (firsignaddedsho, "Fir sign Added by SHO"),
            (firsignaddedsp, "Fir sign Added by SP"),
            (firsignaddedcourt, "Fir sign Added by Court"),
            (firsignnotadded, "Fir sign Not Added")
    )
    firsignstatus = models.CharField(max_length=25, choices=firsign_choice, default=firsignnotadded)

    aadharverificationdone = "Aadhar Verified"
    aadharverificationnotdone = "Aadhar Not Verified"
    aadharverificationskipped = "Skipped Aadhar Verification"
    aadharverification_choice = (
            (aadharverificationdone, "Aadhar Verified"),
            (aadharverificationnotdone, "Aadhar Not Verified"),
            (aadharverificationskipped, "Skipped Aadhar Verification"),
    )
    aadharverification_status = models.CharField(max_length=50, choices=aadharverification_choice, default=aadharverificationnotdone)

    sho_decline = models.BooleanField(default=False, max_length=100, blank=True)
    sho_filefir = models.BooleanField(default=False, max_length=100, blank=True)
    sho_sign = models.BooleanField(default=False, max_length=100, blank=True)
    sho_aadharverification = models.BooleanField(default=False, max_length=100, blank=True)

    sp_decline = models.BooleanField(default=False, max_length=100, blank=True)
    sp_filefir = models.BooleanField(default=False, max_length=100, blank=True)
    sp_sign = models.BooleanField(default=False, max_length=100, blank=True)
    sp_aadharverification = models.BooleanField(default=False, max_length=100, blank=True)

    m_sign = models.BooleanField(default=False, max_length=100, blank=True)
    m_filefir = models.BooleanField(default=False, max_length=100, blank=True)
    m_aadharverification = models.BooleanField(default=False, max_length=100, blank=True)
    decline_reason_police = models.CharField(max_length=1000,null=True, blank=True, default="No Reason given by Police")
    decline_reason_sho = models.CharField(max_length=1000,null=True, blank=True, default="No Reason given by SHO")
    decline_reason_sp = models.CharField(max_length=1000,null=True, blank=True, default="No Reason given by SP")


    payment = models.BooleanField(default=False, max_length=100, blank=True)
    transfer_to_m = models.BooleanField(default=False, max_length=100, blank=True)

    priority = models.IntegerField(null=True, blank=True, default=0)

    c_evidence1 = models.FileField(upload_to='c_evidences/', null=True, blank=True, default="")
    c_evidence2 = models.FileField(upload_to='c_evidences/', null=True, blank=True, default="")
    c_evidence3 = models.FileField(upload_to='c_evidences/', null=True, blank=True, default="")

    c_video = models.FileField(upload_to='c_video/', null=True, blank=True, default="")

    def __unicode__(self):
            return self.complaintid
    def __str__(self):
            return str(self.complaintid)
    def get_absolute_url(self):
            return reverse("crimefiles:detail", kwargs={"id":self.complaintid})


class freport(models.Model):
	#faciliatator evidences
	complaintid=models.ForeignKey(Complaint,default=None,on_delete=models.CASCADE)
	facilitatorviews = models.CharField(max_length=2000, null=True, blank=True, default="")
	facilitator_statement = models.FileField(upload_to='fstatements/', max_length=1000, null=True, blank=True, default="")
	f_evidence1 = models.FileField(upload_to='f_evidences/', max_length=1000, null=True, blank=True, default="")
	f_evidence2 = models.FileField(upload_to='f_evidences/', max_length=1000, null=True, blank=True, default="")
	f_evidence3 = models.FileField(upload_to='f_evidences/', max_length=1000, null=True, blank=True, default="")

	def __unicode__(self):
		return self.complaintid

	def __str__(self):
		return str(self.complaintid)

#magistrate
class CaseStatus(models.Model):
	casenumber = models.CharField(max_length=10, primary_key=True,)
	description=models.TextField(max_length=1000,null=True, blank=True,default="")
	courtname= models.CharField(max_length=200,null=True, blank=True,default="")
	dateofregister=models.DateTimeField(auto_now=True )
	complaintid=models.ForeignKey(Complaint,default=None,on_delete=models.CASCADE)
	title_of_update = models.CharField(max_length=1000,null=True, blank=True,default="")
	evidence = models.FileField(upload_to='court_evidence/', null=True, blank=True, default="")

	def __unicode__(self):
		return str(self.complaintid)
	def __str__(self):
		return self.complaintid



class CopStatus(models.Model):
	title=models.CharField(max_length=1000,null=True, blank=True,default="")
	description=models.TextField(max_length=1000,null=True, blank=True,default="")
	complaintid=models.ForeignKey(Complaint,default=None,on_delete=models.CASCADE)
	dateofregister=models.DateTimeField(auto_now=False, auto_now_add=True)
	evidence = models.FileField(upload_to='police_evidence/', null=True, blank=True, default="")


	def  __unicode__(self):
		return str(self.complaintid)

	def __str__(self):
		return self.complaintid



class CaseClose(models.Model):
	verdict=models.CharField(max_length=100)
	description=models.TextField()
	complaintid=models.ForeignKey(Complaint,default=None,on_delete=models.CASCADE)
	dateofregister=models.DateTimeField(auto_now=False, auto_now_add=True)
# evidence
	def  __unicode__(self):
		return self.complaintid

	def __str__(self):
		return self.complaintid

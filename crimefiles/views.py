from django.contrib import messages
from django.http import HttpResponse,HttpResponseRedirect,Http404
from django.shortcuts import render,get_object_or_404,redirect
from django.core.paginator import Paginator, EmptyPage, PageNotAnInteger
from django.core.exceptions import ObjectDoesNotExist
from django.contrib.auth import authenticate, login
from django.contrib.auth.models import User, Group
from django.db.models import Q
from .forms import CopStatusForm,CaseStatusForm,CaseCloseForm,FreportForm, c_form
from .models import CaseStatus,Complaint,CopStatus,CaseClose,DummyAadharData,Facilitator_details,freport,Investigator_details

from wanted.models import Criminal_Info, user_criminal_info

from chat.views import getdata
# For sending msgs and emails on every update
import smtplib
from email.mime.multipart import MIMEMultipart            # for email subject
from email.mime.text import MIMEText                       # Message and text
import twilio
from twilio.rest import Client

# For creating pdf view
from django.template.loader import get_template
# from django.views.generic import View
from crimefiles.utils import render_to_pdf

from PIL import ImageGrab
import random
otp = 0
gid = 0
d_police = False
d_sho = False
d_sp = False
c_police = False
c_sho = False
c_sp = False
c_court = False

import requests
import json
#for payment
from django.views.decorators.csrf import csrf_exempt
from .Paytm import checksum as Checksum
# Create your views here.
from django.http import HttpResponse
MERCHANT_KEY = '21FAvxTDIEn_vyHk'

from googleplaces import GooglePlaces, types, lang
import requests
import json

import urllib
from bs4 import BeautifulSoup

import geocoder

import logging
logging.basicConfig(level=logging.INFO)
logger = logging.getLogger(__name__)
from django.conf import settings

# import Face_Recog
import numpy as np
from PIL import  Image
import os, cv2


def faceback(request):
	print(gid)
	complaint = get_object_or_404(Complaint,complaintid=gid)
	return HttpResponseRedirect(complaint.get_absolute_url())


def nextstep(request):
    print(gid)
    def draw_boundary(img, classifier, scaleFactor, minNeighbors, color, text, clf):
        # Converting image to gray-scale
        # print(img)
        gray_img = cv2.cvtColor(img, cv2.COLOR_BGR2GRAY)
        # detecting features in gray-scale image, returns coordinates, width and height of features
        features = classifier.detectMultiScale(gray_img, scaleFactor, minNeighbors)
        coords = []
        # drawing rectangle around the feature and labeling it
        for (x, y, w, h) in features:
            cv2.rectangle(img, (x,y), (x+w, y+h), color, 2)
            # Predicting the id of the user
            id, _ = clf.predict(gray_img[y:y+h, x:x+w])
            # Check for id of user and label the rectangle accordingly
            # if id==5:
            #     cv2.putText(img, "UNVERIFIED USER", (x, y-4), cv2.FONT_HERSHEY_SIMPLEX, 0.6, color, 1, cv2.LINE_AA)
            if id==4:
                cv2.putText(img, "VERIFIED USER", (x, y-4), cv2.FONT_HERSHEY_SIMPLEX, 0.9, color, 1, cv2.LINE_AA)
            else:
                cv2.putText(img, "UNVERIFIED USER", (x, y-4), cv2.FONT_HERSHEY_SIMPLEX, 0.9, color, 1, cv2.LINE_AA)
            coords = [x, y, w, h]
        return coords
    # Method to recognize the person
    def recognize(img, clf, faceCascade):
        color = {"blue": (255, 0, 0), "red": (0, 0, 255), "green": (0, 255, 0), "white": (255, 255, 255)}
        coords = draw_boundary(img, faceCascade, 1.1, 10, color["white"], "Face", clf)
        return img
    # Loading classifier
    def fun():
        faceCascade = cv2.CascadeClassifier('C://Users//Prashant Verma//Desktop//VirtualBOTOLD//crimefiles//models//haarcascade_frontalface2.xml')
        print("h print")
        print(faceCascade)

        # Loading custom classifier to recognize
        clf = cv2.face.LBPHFaceRecognizer_create()
        # file_ = open(os.path.join(settings.BASE_DIR, 'classifier.yml'))
        # url = staticfiles_storage.url('classifier.yml')
        # print(url)
        # clf.read(url)
        clf.read('C://Users//Prashant Verma//Desktop//VirtualBOTOLD//crimefiles//classifier.yml')
        print("done")

        # Capturing real time video stream. 0 for built-in web-cams, 0 or -1 for external web-cams
        video_capture = cv2.VideoCapture(0)

        while True:
            # Reading image from video stream
            _, img = video_capture.read()
            # Call method we defined above
            # print(img)
            img = recognize(img, clf, faceCascade)
            # Writing processed image in a new window
            cv2.imshow("face detection", img)
            if cv2.waitKey(1) & 0xFF == ord('q'):
                break

        # releasing web-cam
        video_capture.release()
        # Destroying output window
        cv2.destroyAllWindows()

    fun()
    who = request.user
    return render(request,"facemessage.html",{"who":who})

def complaint_create_new(request):
    form=c_form(request.POST or None, request.FILES )
    if request.method == 'POST':
        # print(request)*
        nameofcomplainant = request.POST.get('nameofcomplainant','')
        addressofcomplainant = request.POST.get('addressofcomplainant','')
        email = request.POST.get('email','')
        phone = request.POST.get('phone','')
        typeofincidence = request.POST.get('typeofincidence','')
        roleofcomplainant = request.POST.get('roleofcomplainant','')
        datetimeofcrime = request.POST.get('datetimeofcrime','')
        placeofincidence = request.POST.get('placeofincidence','')
        descriptionofcrime = request.POST.get('descriptionofcrime','')
        nameofsuspect = request.POST.get('nameofsuspect','')
        addressofsuspect = request.POST.get('addressofsuspect','')
        detailsofsuspect = request.POST.get('detailsofsuspect','')
        messages.success(request,"Complaint registered successfully")
        complaint = Complaint(email=email, phone=phone,nameofsuspect=nameofsuspect,addressofsuspect= addressofsuspect, detailsofsuspect= detailsofsuspect, nameofcomplainant=nameofcomplainant,addressofcomplainant=addressofcomplainant,typeofincidence=typeofincidence, roleofcomplainant=roleofcomplainant,datetimeofcrime=datetimeofcrime,placeofincidence=placeofincidence,descriptionofcrime=descriptionofcrime  )
        complaint.user = request.user.username
        complaint.complaint_registered = True
        complaint.save()

        msg = MIMEMultipart()
        msg['from'] = 'virtualcopforu@gmail.com'
        msg['to'] = str(email)
        msg['subject'] = "Complaint Registered Successfully!"
        body = 'Dear '+str(nameofcomplainant)+',<br> Your Complaint has been Registered successfully. <br><br>You can Track your Complaint status using our Complaint Tracker.'

        msg.attach(MIMEText(body, 'html'))
        server = smtplib.SMTP('smtp.gmail.com', 587)
        server.starttls()
        server.login('virtualcopforu@gmail.com', 'A1234@1234')
        text = msg.as_string()
        server.sendmail(msg['From'], msg["to"], text)
        server.quit()
        print("email send success")

        account_sid = 'AC8cdcb1aa84c769a175237de24cc1d18e'
        auth_token= '59f24898c577676e1403161a96910b6a'
        client = Client(account_sid,auth_token)
        message = client.messages.create(
            body='Dear '+str(nameofcomplainant)+', Your Complaint has been Registered successfully. You can Track your Complaint status using our Complaint Tracker.',
            from_='+12028662408',
            to='+91'+str(phone)
        )
        print("Message Send successfully")
        return HttpResponseRedirect(complaint.get_absolute_url())  # change it to digital signature
    data=getdata()
    print(data)
    try:
        data['idatetime']=data['date']+" "+data['time']
        data['idatetime']=data['idatetime'][:-3]
    except:
        pass
    return render(request,"newComplaintForm.html",{'data':data, "form":form})


def home_page(request):
	print(got_l)
	print('hhh')
	who = request.user
	criminals = Criminal_Info.objects.all()
	print(criminals)
	if request.method == "POST":
		name_of_criminal = request.POST.get('name_of_criminal','')
		info = request.POST.get('info','')

		userr = user_criminal_info(name_of_informer=who,name_of_criminal=name_of_criminal, info=info )
		userr.save()
		message = "Your Response has been saved successfully!"
		print(message)
		return render(request, "homepagen.html", {"who":who, "criminals":criminals, "message":message})

	return render(request, "homepagen.html", {"who":who, "criminals":criminals, "got_l":got_l})


def location(request):
	# print(location)
	g=geocoder.ip('me')
	print(g.latlng)
	lat= g.latlng[0]
	lon= g.latlng[1]

	API_KEY = 'AIzaSyAJwEDXMMbO5muyvDgJU4NqH9fpOAvmdlg'
	google_places = GooglePlaces(API_KEY)
	query_result = google_places.nearby_search(
        lat_lng ={'lat': lat, 'lng': lon},
        radius = 5000,
        types =[types.TYPE_HOSPITAL])
	if query_result.has_attributions:
		print (query_result.html_attributions)
	for place in query_result.places:
	    # print(type(place))
	    # place.get_details()
	    print (place.name)
	    print("Latitude", place.geo_location['lat'])
	    print("Longitude", place.geo_location['lng'])
	    print()
	query=query_result.places[0].name +" "+ g.city
	print(query+"hello")
	query = query.replace(' ', '+')
	URL = f"https://google.com/search?q={query}"

	USER_AGENT = "Mozilla/5.0 (Macintosh; Intel Mac OS X 10.14; rv:65.0) Gecko/20100101 Firefox/65.0"

	headers = {"user-agent" : USER_AGENT}
	resp = requests.get(URL, headers=headers)
	soup = BeautifulSoup(resp.content, "html.parser")
	try:
	    print(soup.find('span',{'class':'LrzXr zdqRlf kno-fv'}).find('span').text)
	except:
	    print(soup.find('span',{'class':'rllt__wrapped'}).find('span').text)
	global got_l
	got_l = True
	print(got_l)
	account_sid = 'ACeba6d7f9aa18ef4da127e66f8b47fd04'
	auth_token= '4b02602e3db3da0c74af0fe536f3cfef'
	client = Client(account_sid,auth_token)

	call = client.calls.create(
	    to = '+919896590848',
	    from_ = "+12513510374",
	    url = "https://demo.twilio.com/docs/voice.xml"
	)
	print(call.sid)

	who = request.user

	account_sid = 'AC8cdcb1aa84c769a175237de24cc1d18e'
	auth_token= '59f24898c577676e1403161a96910b6a'
	client = Client(account_sid,auth_token)
	message = client.messages.create(
		body='who wants help right now. Address is '+' ',
		from_='+12028662408',
		to='+919896590848'
	)
	print("Message Send successfully")

	return HttpResponseRedirect('/crimefiles/')


def home_page(request):
	# return HttpResponse("Home page")
	who = request.user
	criminals = Criminal_Info.objects.all()
	print(criminals)
	if request.method == "POST":
		name_of_criminal = request.POST.get('name_of_criminal','')
		info = request.POST.get('info','')

		userr = user_criminal_info(name_of_informer=who,name_of_criminal=name_of_criminal, info=info )
		userr.save()
		message = "Your Response has been saved successfully!"
		print(message)
		return render(request, "homepagen.html", {"who":who, "criminals":criminals, "message":message})

	return render(request, "homepagen.html", {"who":who, "criminals":criminals})


def CourtPayment(request):
	print(gid)
	who = request.user
	if request.method=="POST":
	    thank = True
        # Request paytm to transfer the amount to your account after payment by user
	    param_dict = {
                'MID': 'ApKlAA76011299426005',
                'ORDER_ID': str(gid),
                'TXN_AMOUNT': str(1000),
                'CUST_ID': 'aakritigupta1435@gmail.com',
                'INDUSTRY_TYPE_ID': 'Retail',
                'WEBSITE': 'WEBSTAGING',
                'CHANNEL_ID': 'WEB',
                'CALLBACK_URL':'http://127.0.0.1:8000/crimefiles/handlerequest/',
        }
	    print("courtpayment func")
	    param_dict['CHECKSUMHASH'] = Checksum.generate_checksum(param_dict, MERCHANT_KEY)
	    print(param_dict)
	    return render(request, 'paytm.html', {'param_dict': param_dict})
	return render(request, 'CourtPayment.html', {"who":who})


@csrf_exempt
def handlerequest(request):
	print(gid)
	instance=Complaint.objects.get(complaintid=gid)
    # paytm will send you post request here
	who = request.user
	form = request.POST
	response_dict = {}
	for i in form.keys():
	    response_dict[i] = form[i]
	    if i == 'CHECKSUMHASH':
	        checksum = form[i]
	print("handlerequest")
	verify = Checksum.verify_checksum(response_dict, MERCHANT_KEY, checksum)
	if verify:
	    if response_dict['RESPCODE'] == '01':
	        print('Payment successful')
	        # instance_Complaint = get_object_or_404(Complaint,complaintid=gid)
	        instance.payment = True
	        instance.transfer_to_m = True
	        instance.save()
			# instance = Complaint.objects.filter(complaintid = gid)
	    else:
	        print('payment was not successful because' + response_dict['RESPMSG'])
	# complaint = get_object_or_404(Complaint,complaintid=gid)
	# return HttpResponseRedirect(instance.get_absolute_url())
	return render(request, 'paymentstatus.html', {'response': response_dict, "who":who})


def request_magistrate(request, id=None):
	return render(request, "request_magistrate.html")




#### PENDING
def drop_complaint(request, id=None):
	return HttpResponse("Complaint dropped")


def i_portal(request, id=None):
	return render(request, 'Investigation_portal.html')


def investigator_details(request, id=None):
	investigators = Investigator_details.objects.all()
	# fname = Facilitator_details.objects.values('nameoffacilitator')
	# print(fname)
	params = {'investigators':investigators}

	if request.method == "POST":
		chooseniname = request.POST.get('inamechoosen','')
		print(chooseniname)
		instance = Investigator_details.objects.get(nameofinvestigator = chooseniname)
		instance.currentlyassigned = True
		instance.save()
		complaint = Complaint.objects.get(complaintid = id)
		complaint.nameofinvestigatorassigned = chooseniname
		complaint.iassignstatus = "Investigator Assigned"
		complaint.save()
		return HttpResponseRedirect(complaint.get_absolute_url())
	return render(request, 'investigator_details.html', params)
	# return HttpResponse("Investigator")


def upload(request):
	instance = get_object_or_404(Complaint,complaintid=gid)
	name = instance.nameofcomplainant
	if request.method=='POST':
		uploadedFile = open("C:/Users/Prashant Verma/Desktop/VirtualBOTOLD/crimefiles/static/fstatement/"+gid+"_"+name+".wav", "wb")
		# the actual file is in request.body
		uploadedFile.write(request.body)
		uploadedFile.close()
		print('audio saved')
		return HttpResponse('audio saved')
	# return render(request,'audio.html')

def uploadcomplaintrec(request):
	# instance = get_object_or_404(Complaint,complaintid=gid)
	# name = instance.nameofcomplainant
	who = request.user
	if request.method=='POST':
		uploadedFile = open("C:/Users/Prashant Verma/Desktop/VirtualBOTOLD/crimefiles/static/userstatement/"+who+".wav", "wb")
		# the actual file is in request.body
		uploadedFile.write(request.body)
		uploadedFile.close()
		print('audio saved')
		return HttpResponse('audio saved')

def uploaddsho(request):
	print(gid)
	instance = get_object_or_404(Complaint,complaintid=gid)
	name = instance.nameofcomplainant
	print("shooo")
	if request.method=='POST':
		uploadedFile = open("C:/Users/Prashant Verma/Desktop/VirtualBOTOLD/crimefiles/static/Decline Statements/SHO/"+gid+"_"+name+".wav", "wb")
		# the actual file is in request.body
		uploadedFile.write(request.body)
		uploadedFile.close()
		print('audio saved')
		return HttpResponse('audio saved')

def uploaddsp(request):
	print(gid)
	instance = get_object_or_404(Complaint,complaintid=gid)
	name = instance.nameofcomplainant
	if request.method=='POST':
		uploadedFile = open("C:/Users/Prashant Verma/Desktop/VirtualBOTOLD/crimefiles/static/Decline Statements/SP/"+gid+"_"+name+".wav", "wb")
		# the actual file is in request.body
		uploadedFile.write(request.body)
		uploadedFile.close()
		print('audio saved')
		return HttpResponse('audio saved')
	# return render(request,'audio.html')


def openfile(request):
	return render(request, 'audio.html')


def fevidences(request, id=None):
	# IMAGE_FILE_TYPES=['png','jpg','jpeg','mp4','mpeg','wav','ogg']
	complaintid = get_object_or_404(Complaint,complaintid=id)
	form=FreportForm(request.POST or None, request.FILES or None)
	complaint=get_object_or_404(Complaint,complaintid = id)
	# if request.method == "POST":
	# 	#uploadedFile = open(".wav","wb")
	# 	uploadedFile = open("audio.wav","wb")
	#  	uploadedFile.write(request.body)
	#  	uploadedFile.close()
	#  	print('audio Saved')
	if form.is_valid():
		evidence=form.save(commit=False)
		evidence.f_evidence2=request.FILES['f_evidence1']
		evidence.f_evidence2=request.FILES['f_evidence2']
		evidence.f_evidence3=request.FILES['f_evidence3']
		# evidence.facilitator_statement=request.FILES['facilitator_statement']
		# file_type=evidence.f_evidence1.url.split('.')[-1]
		# file_type=file_type.lower()
		print(evidence.facilitatorviews)
		evidence.complaintid=complaintid
		# if file_type not in IMAGE_FILE_TYPES:
		#     # context={'album':album,'form':form,'error_message':'Image file must be PNG,JPG or JPEG'}
		#     return HttpResponse('Erroooorrr')
		evidence.save()
		instance=Complaint.objects.get(complaintid=id)
		instance.freport_status="Facilitator Report Added"
		instance.save()
		return HttpResponseRedirect(complaintid.get_absolute_url())
		# return HttpResponse('done')
	return render(request,'facilitator_form.html',{'form':form})


def facilitator_details(request, id=None):
	# return HttpResponse('he')
	facilitators = Facilitator_details.objects.all()
	# print(facilitators)
	fname = Facilitator_details.objects.values('nameoffacilitator')
	# print(fname)
	params = {'facilitators': facilitators, 'fname':fname}

	if request.method == "POST":
		choosenfname = request.POST.get('fnamechoosen','')
		print(choosenfname)
		finstance = Facilitator_details.objects.get(nameoffacilitator = choosenfname)
		finstance.currentlyassigned = True
		finstance.save()
		complaint = Complaint.objects.get(complaintid = id)
		complaint.nameoffacilitator = choosenfname
		complaint.fassignstatus = "Facilitator Assigned"
		complaint.save()
		return HttpResponseRedirect(complaint.get_absolute_url())
	return render(request, 'facilitator_details.html', params)


def skip_aadhar(request, id=None):
	instance=Complaint.objects.get(complaintid=id)
	instance.aadharverification_status="Skipped Aadhar Verification"
	instance.save()
	complaint = get_object_or_404(Complaint,complaintid=id)
	return HttpResponseRedirect(complaint.get_absolute_url())
	# return render(request, 'facilitator_details.html')


def check_otp(request):
    print(gid)
    instance=Complaint.objects.get(complaintid=gid)
    complaint = get_object_or_404(Complaint,complaintid=gid)
    is_police=request.user.groups.filter(name='Police').exists()
    is_sho=request.user.groups.filter(name='SHO').exists()
    is_sp=request.user.groups.filter(name='SP').exists()
    is_fac=request.user.groups.filter(name='Facilitator').exists()
    is_court=request.user.groups.filter(name='Court').exists()
    print(is_police)
    who=request.user
    # choosen_f_name = Complaint.objects.filter(complaintid = gid)[0].nameoffacilitator
    # finstance = Facilitator_details.objects.get(nameoffacilitator= choosen_f_name)
    # finstance.currentlyassigned = False
    # finstance.save()
    if request.method == 'POST':
        user_otp = request.POST.get('otp','')
        if user_otp == str(otp):
            if not is_police and not is_sho and not is_sp and not is_fac and not is_court :
                instance.aadharverification_status="Aadhar Verified"
                instance.save()
                # return HttpResponse('Your verification process is Done.')
                print(instance.aadharverification_status)
            # return render(request, 'facilitator_details.html')
            if is_police and d_police:
                instance.status="Complaint Under Progress"
                instance.signedstatus="Signed by no one"
                instance.declinedstatus="Declined by SHO"
                instance.sho_decline = True
                instance.sho_aadharverification = True
                instance.save()
                print('declined complaint')
                print(instance.declinedstatus)
                mail = Complaint.objects.filter(complaintid = gid)[0].email
                phone = Complaint.objects.filter(complaintid = gid)[0].phone
                nameofcomplainant = Complaint.objects.filter(complaintid = gid)[0].nameofcomplainant
                msg = MIMEMultipart()
                msg['from'] = 'virtualcopforu@gmail.com'
                msg['to'] = str(mail)
                msg['subject'] = "FIR Filled"
                body = 'Dear '+str(nameofcomplainant)+',<br>Sorry to say but your Complaint has been declined by the SHO.<br><br>Now we are forwarding your Complaint to the SP.'
                msg.attach(MIMEText(body, 'plain'))
                server = smtplib.SMTP('smtp.gmail.com', 587)
                server.starttls()
                server.login('virtualcopforu@gmail.com', 'A1234@1234')
                text = msg.as_string()
                server.sendmail(msg['From'], msg["to"], text)
                server.quit()
                print("email send success")
                account_sid = 'AC8cdcb1aa84c769a175237de24cc1d18e'
                auth_token= '59f24898c577676e1403161a96910b6a'
                client = Client(account_sid,auth_token)
                message = client.messages.create(
                    body='Dear '+str(nameofcomplainant)+', Sorry to say but your Complaint has been declined by the SHO. Now we are forwarding your Complaint to the SP.',
                    from_='+12028662408',
                    to='+91'+str(phone)
                )
                print("Message Send successfully")
            if is_police and c_police:
                instance.status="FIR Filed"
                instance.signedstatus="Signed by SHO"
                instance.declinedstatus="Declined by no one"
                instance.sho_filefir = True
                instance.sho_aadharverification = True
                instance.save()
                choosen_f_name = Complaint.objects.filter(complaintid = gid)[0].nameoffacilitator
                finstance = Facilitator_details.objects.get(nameoffacilitator= choosen_f_name)
                finstance.currentlyassigned = False
                finstance.save()
                mail = Complaint.objects.filter(complaintid = gid)[0].email
                phone = Complaint.objects.filter(complaintid = gid)[0].phone
                nameofcomplainant = Complaint.objects.filter(complaintid = gid)[0].nameofcomplainant
                msg = MIMEMultipart()
                msg['from'] = 'virtualcopforu@gmail.com'
                msg['to'] = str(mail)
                msg['subject'] = "FIR Filled"
                body = 'Dear '+str(nameofcomplainant)+',<br>Your FIR has been filled successfully by the SHO.<br><br>'
                msg.attach(MIMEText(body, 'plain'))
                server = smtplib.SMTP('smtp.gmail.com', 587)
                server.starttls()
                server.login('virtualcopforu@gmail.com', 'A1234@1234')
                text = msg.as_string()
                server.sendmail(msg['From'], msg["to"], text)
                server.quit()
                print("email send success")
                account_sid = 'AC8cdcb1aa84c769a175237de24cc1d18e'
                auth_token= '59f24898c577676e1403161a96910b6a'
                client = Client(account_sid,auth_token)
                message = client.messages.create(
                    body='Dear '+str(nameofcomplainant)+', Your FIR has been filled successfully by the SHO.',
                    from_='+12028662408',
                    to='+91'+str(phone)
                )
                print("Message Send successfully")
            if is_sho and d_sho :
                instance.status="Complaint Under Progress"
                instance.signedstatus="Signed by no one"
                instance.declinedstatus="Declined by SP"
                instance.sp_decline = True
                instance.sp_aadharverification = True
                instance.save()
                print('declined complaint')
                print(instance.declinedstatus)
                mail = Complaint.objects.filter(complaintid = gid)[0].email
                phone = Complaint.objects.filter(complaintid = gid)[0].phone
                nameofcomplainant = Complaint.objects.filter(complaintid = gid)[0].nameofcomplainant
                msg = MIMEMultipart()
                msg['from'] = 'virtualcopforu@gmail.com'
                msg['to'] = str(mail)
                msg['subject'] = "FIR Filled"
                body = 'Dear '+str(nameofcomplainant)+',<br>Sorry to say but your Complaint has been declined by the SP.<br><br>Now you can request the magistrate to file an FIR regarding your complaint.'
                msg.attach(MIMEText(body, 'plain'))
                server = smtplib.SMTP('smtp.gmail.com', 587)
                server.starttls()
                server.login('virtualcopforu@gmail.com', 'A1234@1234')
                text = msg.as_string()
                server.sendmail(msg['From'], msg["to"], text)
                server.quit()
                print("email send success")
                account_sid = 'AC8cdcb1aa84c769a175237de24cc1d18e'
                auth_token= '59f24898c577676e1403161a96910b6a'
                client = Client(account_sid,auth_token)
                message = client.messages.create(
                    body='Dear '+str(nameofcomplainant)+', Sorry to say but your Complaint has been declined by the SP. <br> Now you can request the magistrate to file an FIR regarding your complaint.',
                    from_='+12028662408',
                    to='+91'+str(phone)
                )
                print("Message Send successfully")
            if is_sho and c_sho :
                instance.status="FIR Filed"
                instance.signedstatus="Signed by SP"
                instance.declinedstatus="Declined by SHO"
                instance.sp_filefir = True
                instance.sp_aadharverification = True
                instance.save()
                choosen_f_name = Complaint.objects.filter(complaintid = gid)[0].nameoffacilitator
                finstance = Facilitator_details.objects.get(nameoffacilitator= choosen_f_name)
                finstance.currentlyassigned = False
                finstance.save()
                mail = Complaint.objects.filter(complaintid = gid)[0].email
                phone = Complaint.objects.filter(complaintid = gid)[0].phone
                nameofcomplainant = Complaint.objects.filter(complaintid = gid)[0].nameofcomplainant
                msg = MIMEMultipart()
                msg['from'] = 'virtualcopforu@gmail.com'
                msg['to'] = str(mail)
                msg['subject'] = "FIR Filled"
                body = 'Dear '+str(nameofcomplainant)+',<br>Your FIR has been filled successfully by the SP.<br>'
                msg.attach(MIMEText(body, 'plain'))
                server = smtplib.SMTP('smtp.gmail.com', 587)
                server.starttls()
                server.login('virtualcopforu@gmail.com', 'A1234@1234')
                text = msg.as_string()
                server.sendmail(msg['From'], msg["to"], text)
                server.quit()
                print("email send success")
                account_sid = 'AC8cdcb1aa84c769a175237de24cc1d18e'
                auth_token= '59f24898c577676e1403161a96910b6a'
                client = Client(account_sid,auth_token)
                message = client.messages.create(
                    body='Dear '+str(nameofcomplainant)+', Your FIR has been filled successfully by the SP.  ',
                    from_='+12028662408',
                    to='+91'+str(phone)
                )
                print("Message Send successfully")
            if is_sp and d_sp :
                print("here")
                instance.status="Complaint Under Progress"
                instance.signedstatus="Signed by no one"
                instance.declinedstatus="Declined by SP"
                instance.save()
                print('declined complaint')
                print(instance.declinedstatus)
                mail = Complaint.objects.filter(complaintid = gid)[0].email
                phone = Complaint.objects.filter(complaintid = gid)[0].phone
                nameofcomplainant = Complaint.objects.filter(complaintid = gid)[0].nameofcomplainant
                msg = MIMEMultipart()
                msg['from'] = 'virtualcopforu@gmail.com'
                msg['to'] = str(mail)
                msg['subject'] = "FIR Filled"
                body = 'Dear '+str(nameofcomplainant)+',<br>Sorry to say but your Complaint has been declined by the SP.<br><br>Now we are forwarding your Complaint to the Court.<br>You can Track your Complaint status using our Complaint Tracker.'
                msg.attach(MIMEText(body, 'plain'))
                server = smtplib.SMTP('smtp.gmail.com', 587)
                server.starttls()
                server.login('virtualcopforu@gmail.com', 'A1234@1234')
                text = msg.as_string()
                server.sendmail(msg['From'], msg["to"], text)
                server.quit()
                print("email send success")
                account_sid = 'AC8cdcb1aa84c769a175237de24cc1d18e'
                auth_token= '59f24898c577676e1403161a96910b6a'
                client = Client(account_sid,auth_token)
                message = client.messages.create(
                    body='Dear '+str(nameofcomplainant)+', Sorry to say but your Complaint has been declined by the SP. Now we are forwarding your Complaint to the Court. You can Track your Complaint status using our Complaint Tracker.',
                    from_='+12028662408',
                    to='+91'+str(phone)
                )
                print("Message Send successfully")
            if is_sp and c_sp :
                instance.status="FIR Filed"
                instance.signedstatus="Signed by SP"
                instance.declinedstatus="Declined by SHO"
                instance.save()
                choosen_f_name = Complaint.objects.filter(complaintid = gid)[0].nameoffacilitator
                finstance = Facilitator_details.objects.get(nameoffacilitator= choosen_f_name)
                finstance.currentlyassigned = False
                finstance.save()
                print('declined complaint')
                print(instance.declinedstatus)
                mail = Complaint.objects.filter(complaintid = gid)[0].email
                phone = Complaint.objects.filter(complaintid = gid)[0].phone
                nameofcomplainant = Complaint.objects.filter(complaintid = gid)[0].nameofcomplainant
                msg = MIMEMultipart()
                msg['from'] = 'virtualcopforu@gmail.com'
                msg['to'] = str(mail)
                msg['subject'] = "FIR Filled"
                body = 'Dear '+str(nameofcomplainant)+',<br>Your FIR has been filled successfully by the SP.<br><br>You can Track your Complaint status using our Complaint Tracker.'
                msg.attach(MIMEText(body, 'plain'))
                server = smtplib.SMTP('smtp.gmail.com', 587)
                server.starttls()
                server.login('virtualcopforu@gmail.com', 'A1234@1234')
                text = msg.as_string()
                server.sendmail(msg['From'], msg["to"], text)
                server.quit()
                print("email send success")
                account_sid = 'AC8cdcb1aa84c769a175237de24cc1d18e'
                auth_token= '59f24898c577676e1403161a96910b6a'
                client = Client(account_sid,auth_token)
                message = client.messages.create(
                    body='Dear '+str(nameofcomplainant)+', Your FIR has been filled successfully by the SP. You can Track your Complaint Status using our Complaint Tracker ',
                    from_='+12028662408',
                    to='+91'+str(phone)
                )
                print("Message Send successfully")
            if is_court and c_court :
                instance.status="FIR Filed"
                instance.signedstatus="Signed by Court"
                instance.declinedstatus="Declined by SP"
                instance.m_filefir = True
                instance.m_aadharverification = True
                instance.save()
                choosen_f_name = Complaint.objects.filter(complaintid = gid)[0].nameoffacilitator
                finstance = Facilitator_details.objects.get(nameoffacilitator= choosen_f_name)
                finstance.currentlyassigned = False
                finstance.save()
                mail = Complaint.objects.filter(complaintid = gid)[0].email
                phone = Complaint.objects.filter(complaintid = gid)[0].phone
                nameofcomplainant = Complaint.objects.filter(complaintid = gid)[0].nameofcomplainant
                msg = MIMEMultipart()
                msg['from'] = 'virtualcopforu@gmail.com'
                msg['to'] = str(mail)
                msg['subject'] = "FIR Filled"
                body = 'Dear '+str(nameofcomplainant)+',<br>Your FIR has been filled successfully by the Magistrate.<br>'
                msg.attach(MIMEText(body, 'plain'))
                server = smtplib.SMTP('smtp.gmail.com', 587)
                server.starttls()
                server.login('virtualcopforu@gmail.com', 'A1234@1234')
                text = msg.as_string()
                server.sendmail(msg['From'], msg["to"], text)
                server.quit()
                print("email send success")
                account_sid = 'AC8cdcb1aa84c769a175237de24cc1d18e'
                auth_token= '59f24898c577676e1403161a96910b6a'
                client = Client(account_sid,auth_token)
                message = client.messages.create(
                    body='Dear '+str(nameofcomplainant)+', Your FIR has been filled successfully by the Magistrate. ',
                    from_='+12028662408',
                    to='+91'+str(phone)
                )
                print("Message Send successfully")
            complaint = get_object_or_404(Complaint,complaintid=gid)
            # return HttpResponseRedirect(complaint.get_absolute_url())
            return render(request, 'next.html',{"who":who})
        else:
            return render(request, 'aadhar.html', {"message":"Invalid OTP. Please Enter your aadhar no again for verification.", "who":who})
    return render(request, 'check_otp.html', {"who":who})
	# return HttpResponse('otp')


def verify_aadhar(request, id=None):
	complaint = get_object_or_404(Complaint,complaintid=id)
	global gid
	gid = id
	print(gid)
	who=request.user
	if request.method == "POST":
		print(request)
		user_aadhar = request.POST.get('aadharNo','')
		print(user_aadhar)
		length_of_aadhar = len(user_aadhar)
		print(length_of_aadhar)

		#recaptcha backend
		clientKey = request.POST['g-recaptcha-response']
		secretKey = '6LeqbrAZAAAAALDa_ZBSmsp3pAkIQwG-rioGcpnl'
		captchaData = {
			'secret' : secretKey,
			'response' : clientKey
		}
		#API URL
		r = requests.post('https://www.google.com/recaptcha/api/siteverify', data = captchaData)
		response = json.loads(r.text)
		verify = response['success']
		print('your success is ', verify)

		if length_of_aadhar == 12 and verify :
			present = DummyAadharData.objects.filter(aadhar_no = user_aadhar).exists()
			if present:
				user_phone = DummyAadharData.objects.filter(aadhar_no = user_aadhar)[0].mobile
				print(user_phone)
				print(present)
				#present = DummyAadharData.objects.filter(aadhar_no = user_aadhar).exists()
				#present = Entry.objects.filter(name='name', title='title').exists()
				generated_otp = random.randint(100000,999999)
				print(generated_otp)
				global otp
				otp = generated_otp
				account_sid = 'AC8cdcb1aa84c769a175237de24cc1d18e'
				auth_token = '59f24898c577676e1403161a96910b6a'
				client = Client(account_sid, auth_token)
				message = client.messages.create(
					body='OTP for your Aadhar card verification is - '+str(generated_otp),
					from_='+12028662408',
					to='+91'+str(user_phone)
				)
				print(message.sid)
				#global send_otp
				#send_otp = True
				# return render(request, 'check_otp.html', {'id':id})
				# return HttpResponseRedirect('/crimefiles/complaint.get_absolute_url()/check_otp')
				return HttpResponseRedirect('/crimefiles/check_otp')
				# return HttpResponseRedirect(complaint.get_absolute_url()/check_otp)
			else:
				return render(request, 'aadhar.html', {"message":"Not a valid Aadhar Number. Please enter a Valid aadhar number", "who":who})
		else:
			print(verify)
			return render(request, 'aadhar.html', {"message":"Please enter a Valid aadhar number", "verify":verify,"who":who})
	return render(request, 'aadhar.html', {"who":who})


def save_signature(request,id=None):
	instance = get_object_or_404(Complaint,complaintid=id)
	name = instance.nameofcomplainant
	print(name)
	print(id)
	image = ImageGrab.grab(bbox=(30,155,640,520))  #x axis, y axis, height, width
	path = "C:/Users/Prashant Verma/Desktop/VirtualBOTOLD/crimefiles/static/Complainant Signatures/"+id+"_"+name+".png"
	image.save(path)
	print('Signature saved')
	instance=Complaint.objects.get(complaintid=id)
	instance.csignstatus="Csign Added"
	instance.save()
	# return HttpResponse('signature saved')
	# return render(request, 'aadhar.html')
	# return HttpResponseRedirect('/validate_aadhar/')
	# return HttpResponseRedirect('/crimefiles/')
	complaint = get_object_or_404(Complaint,complaintid=id)
	return HttpResponseRedirect(complaint.get_absolute_url())
	# return render(request,'complaint_list.html')


def save_signature_p(request, id=None):
	instance = get_object_or_404(Complaint,complaintid=id)
	name = instance.nameofcomplainant
	print(name)
	print(id)
	instance.sho_sign = True
	instance.save()
	if d_police:
		image = ImageGrab.grab(bbox=(30,155,640,520))  #x axis, y axis, height, width
		path = "C:/Users/Prashant Verma/Desktop/VirtualBOTOLD/crimefiles/static/Decline Signatures/Police/"+id+"_"+"policesign.png"
		image.save(path)
		print('Signature saved')
	if c_police:
		image = ImageGrab.grab(bbox=(30,155,640,520))  #x axis, y axis, height, width
		path = "C:/Users/Prashant Verma/Desktop/VirtualBOTOLD/crimefiles/static/Fir Confirm Signatures/Police/"+id+"_"+"policesign.png"
		image.save(path)
		print('Signature saved')
	return render(request, 'declineaadhar.html')


def save_signature_sho(request, id=None):
	instance = get_object_or_404(Complaint,complaintid=id)
	name = instance.nameofcomplainant
	print(name)
	print(id)
	instance.sp_sign = True
	instance.save()
	if d_sho:
		image = ImageGrab.grab(bbox=(30,155,640,520))  #x axis, y axis, height, width
		path = "C:/Users/Prashant Verma/Desktop/VirtualBOTOLD/crimefiles/static/Decline Signatures/SHO/"+id+"_"+"shosign.png"
		image.save(path)
		print('Signature saved')
	if c_sho:
		image = ImageGrab.grab(bbox=(30,155,640,520))  #x axis, y axis, height, width
		path = "C:/Users/Prashant Verma/Desktop/VirtualBOTOLD/crimefiles/static/Fir Confirm Signatures/SHO/"+id+"_"+"shosign.png"
		image.save(path)
		print('Signature saved')
	return render(request, 'declineaadhar.html')


def save_signature_sp(request, id=None):
	instance = get_object_or_404(Complaint,complaintid=id)
	name = instance.nameofcomplainant
	print(name)
	print(id)
	if d_sp:
		image = ImageGrab.grab(bbox=(30,155,640,520))  #x axis, y axis, height, width
		path = "C:/Users/Prashant Verma/Desktop/VirtualBOTOLD/crimefiles/static/Decline Signatures/SHO/"+id+"_"+"spsign.png"
		image.save(path)
		print('Signature saved')
	if c_sp:
		image = ImageGrab.grab(bbox=(30,155,640,520))  #x axis, y axis, height, width
		path = "C:/Users/Prashant Verma/Desktop/VirtualBOTOLD/crimefiles/static/Fir Confirm Signatures/SHO/"+id+"_"+"spsign.png"
		image.save(path)
		print('Signature saved')
	return render(request, 'declineaadhar.html')


def save_signature_court(request, id=None):
	instance = get_object_or_404(Complaint,complaintid=id)
	name = instance.nameofcomplainant
	print(name)
	print(id)
	instance.m_sign = True
	instance.save()
	if c_sp:
		image = ImageGrab.grab(bbox=(30,155,640,520))  #x axis, y axis, height, width
		path = "C:/Users/Prashant Verma/Desktop/VirtualBOTOLD/crimefiles/static/Fir Confirm Signatures/Court/"+id+"_"+"courtsign.png"
		image.save(path)
		print('Signature saved')
	return render(request, 'declineaadhar.html')


def open_sketch(request,id=None):
	return render(request, 'sketch.html')


def save_sketch(request, id=None):
	instance = get_object_or_404(Complaint,complaintid=id)
	name = instance.nameofcomplainant
	print(name)
	print(id)#410,200,900,720
	image = ImageGrab.grab(bbox=(500,250, 1000,800))  #x axis, y axis, height, width
	path = "C:/Users/Prashant Verma/Desktop/VirtualBOTOLD/crimefiles/static/Criminal Sketches/"+id+"_"+name+".png"
	image.save(path)
	print('Sketch saved')
	instance=Complaint.objects.get(complaintid=id)
	instance.sketchstatus="Criminal Sketch Added"
	instance.save()
	# return HttpResponse('saved')
	return render(request, 'signature_pad.html')


def skip_sketch(request, id=None):
	instance=Complaint.objects.get(complaintid=id)
	instance.sketchstatus="Criminal Sketch Skipped"
	instance.save()
	return render(request, 'signature_pad.html')


def fir_pdf(request, id=None):
	print(id)
	instance_Complaint = get_object_or_404(Complaint,complaintid=id)
	# print(instance.nameofcomplainant)
	# print(instance.signedby)
	template = get_template('fir_pdf.html')
	name = instance_Complaint.nameofcomplainant
	filename = id + "_"+name
	filep = id + "_policesign"
	filesho = id + "_shosign"
	filesp = id + "_spsign"
	print(filename)
	context={
		"fir_id": id,
		"instance":instance_Complaint,
		"filename": filename,
		"filep":filep,
		"filesho":filesho,
		"filesp":filesp,
	}
	html = template.render(context)
	pdf = render_to_pdf('fir_pdf.html', context)
	if pdf:
		response = HttpResponse(pdf, content_type = 'application/pdf')
		filename = "fir_%s.pdf" % (str(id))
		content = "inline; filename='%s'" % (filename)
		download = request.GET.get("download")
		if download:
			content = "attachment; filename= '%s'" % (filename)
		response['Content-Disposition'] = content
		return response
	return HttpResponse("Not found")


def fir_create_police(request,id=None):
	if not request.user.groups.filter(name="Police").exists():
		raise Http404
	if CaseClose.objects.filter(complaintid=id).exists():
		raise Http404
	complaintid = get_object_or_404(Complaint,complaintid=id)
	instance2=Complaint.objects.get(complaintid=id)
	# instance3=Fir.objects.filter(complaintid=id)
	global c_police
	c_police = True
	is_police=request.user.groups.filter(name='Police').exists()
	is_sho=request.user.groups.filter(name='SHO').exists()
	is_sp=request.user.groups.filter(name='SP').exists()
	is_court=request.user.groups.filter(name='Court').exists()
	params = {'is_police':is_police, 'is_sho':is_sho, 'is_sp':is_sp, 'is_court':is_court}
	return render(request, 'signature_pad.html',params)


def fir_decline_police(request,id=None):
	if not request.user.groups.filter(name="Police").exists():
		raise Http404
	if CaseClose.objects.filter(complaintid=id).exists():
		raise Http404
	complaintid = get_object_or_404(Complaint,complaintid=id)
	instance=Complaint.objects.get(complaintid=id)
	who = request.user
	global gid
	gid = id
	is_police=request.user.groups.filter(name='Police').exists()
	is_sho=request.user.groups.filter(name='SHO').exists()
	is_sp=request.user.groups.filter(name='SP').exists()
	is_court=request.user.groups.filter(name='Court').exists()
	params = {'is_police':is_police, 'is_sho':is_sho, 'is_sp':is_sp, 'is_court':is_court, "who":who}
	if request.method == "POST":
		print(request)
		decline_reason_sho = request.POST.get('decline_reason','')
		instance.decline_reason_sho=decline_reason_sho
		instance.save()
		global d_police
		d_police = True
		return render(request, 'signature_pad.html',params)
	return render(request,"fir_decline_sho.html" ,params)


def fir_create_sho(request,id=None):
	if not request.user.groups.filter(name="SHO").exists():
		raise Http404
	if CaseClose.objects.filter(complaintid=id).exists():
		raise Http404
	complaintid = get_object_or_404(Complaint,complaintid=id)
	instance2=Complaint.objects.get(complaintid=id)
	# instance3=Fir.objects.filter(complaintid=id)
	global c_sho
	c_sho = True
	is_police=request.user.groups.filter(name='Police').exists()
	is_sho=request.user.groups.filter(name='SHO').exists()
	is_sp=request.user.groups.filter(name='SP').exists()
	is_court=request.user.groups.filter(name='Court').exists()
	params = {'is_police':is_police, 'is_sho':is_sho, 'is_sp':is_sp, 'is_court':is_court}
	return render(request, 'signature_pad.html',params)


def fir_decline_sho(request,id=None):
	if not request.user.groups.filter(name="SHO").exists():
		raise Http404
	if CaseClose.objects.filter(complaintid=id).exists():
		raise Http404
	complaintid = get_object_or_404(Complaint,complaintid=id)
	instance=Complaint.objects.get(complaintid=id)
	who = request.user
	global gid
	gid = id
	is_police=request.user.groups.filter(name='Police').exists()
	is_sho=request.user.groups.filter(name='SHO').exists()
	is_sp=request.user.groups.filter(name='SP').exists()
	is_court=request.user.groups.filter(name='Court').exists()
	params = {'is_police':is_police, 'is_sho':is_sho, 'is_sp':is_sp, 'is_court':is_court, "who":who}
	if request.method == "POST":
		print(request)
		decline_reason_sp = request.POST.get('decline_reason','')
		instance.decline_reason_sp =decline_reason_sp
		instance.save()
		global d_sho
		d_sho = True
		print(d_sho)
		print(instance.decline_reason_sho)
		return render(request, 'signature_pad.html',params)
	return render(request,"fir_decline_sp.html", params)


def fir_create_sp(request,id=None):
	if not request.user.groups.filter(name="SP").exists():
		raise Http404
	if CaseClose.objects.filter(complaintid=id).exists():
		raise Http404
	complaintid = get_object_or_404(Complaint,complaintid=id)
	instance2=Complaint.objects.get(complaintid=id)
	# instance3=Fir.objects.filter(complaintid=id)
	global c_sp
	c_sp = True
	is_police=request.user.groups.filter(name='Police').exists()
	is_sho=request.user.groups.filter(name='SHO').exists()
	is_sp=request.user.groups.filter(name='SP').exists()
	is_court=request.user.groups.filter(name='Court').exists()
	params = {'is_police':is_police, 'is_sho':is_sho, 'is_sp':is_sp, 'is_court':is_court}
	return render(request, 'signature_pad.html',params)


def fir_decline_sp(request,id=None):
	if not request.user.groups.filter(name="SP").exists():
		raise Http404
	if CaseClose.objects.filter(complaintid=id).exists():
		raise Http404
	complaintid = get_object_or_404(Complaint,complaintid=id)
	instance=Complaint.objects.get(complaintid=id)
	# instance3=Fir.objects.filter(complaintid=id)
	is_police=request.user.groups.filter(name='Police').exists()
	is_sho=request.user.groups.filter(name='SHO').exists()
	is_sp=request.user.groups.filter(name='SP').exists()
	is_court=request.user.groups.filter(name='Court').exists()
	who= request.user
	global gid
	gid = id
	params = {'is_police':is_police, 'is_sho':is_sho, 'is_sp':is_sp, 'is_court':is_court, "who":who}
	if request.method == "POST":
		print(request)
		decline_reason_sp = request.POST.get('decline_reason','')
		instance.decline_reason_sp=decline_reason_sp
		instance.save()
		global d_sp
		d_sp = True
		return render(request, 'signature_pad.html',params)
	return render(request,"fir_decline.html")


def fir_create_court(request,id=None):
	if not request.user.groups.filter(name="Court").exists():
		raise Http404
	if CaseClose.objects.filter(complaintid=id).exists():
		raise Http404
	complaintid = get_object_or_404(Complaint,complaintid=id)
	instance2=Complaint.objects.get(complaintid=id)
	# instance3=Fir.objects.filter(complaintid=id)
	global c_court
	c_court = True
	is_police=request.user.groups.filter(name='Police').exists()
	is_sho=request.user.groups.filter(name='SHO').exists()
	is_sp=request.user.groups.filter(name='SP').exists()
	is_court=request.user.groups.filter(name='Court').exists()
	params = {'is_police':is_police, 'is_sho':is_sho, 'is_sp':is_sp, 'is_court':is_court}
	return render(request, 'signature_pad.html',params)


def copstatus_create(request,id=None):
	if not request.user.groups.filter(name="Police").exists() and not request.user.groups.filter(name="SHO").exists() and not request.user.groups.filter(name="SP").exists() :
		raise Http404
	if CaseClose.objects.filter(complaintid=id).exists():
		raise Http404
	complaintid= get_object_or_404(Complaint,complaintid=id)
	form =CopStatusForm(request.POST or None)
	if form.is_valid():
		instance=form.save(commit=False)
		instance.complaintid=complaintid
		instance.save()

		mail = Complaint.objects.filter(complaintid = id)[0].email
		phone = Complaint.objects.filter(complaintid = id)[0].phone
		nameofcomplainant = Complaint.objects.filter(complaintid = id)[0].nameofcomplainant

		msg = MIMEMultipart()
		msg['from'] = 'virtualcopforu@gmail.com'
		msg['to'] = str(mail)
		msg['subject'] = "Police Updates"
		body = 'Dear '+str(nameofcomplainant)+ ',<br>Police has updated some Proceedings regarding your FIR. Please Check it.'

		msg.attach(MIMEText(body, 'html'))
		server = smtplib.SMTP('smtp.gmail.com', 587)
		server.starttls()
		server.login('virtualcopforu@gmail.com', 'A1234@1234')
		text = msg.as_string()
		server.sendmail(msg['From'], msg["to"], text)
		server.quit()
		print("email send success")

		account_sid = 'AC8cdcb1aa84c769a175237de24cc1d18e'
		auth_token= '59f24898c577676e1403161a96910b6a'
		client = Client(account_sid,auth_token)
		message = client.messages.create(
			body='Dear '+str(nameofcomplainant)+ ',Police has updated some Proceedings regarding your FIR. Please Check it.',
			from_='+12028662408',
			to='+91'+str(phone)
		)
		print("Message Send successfully")

		messages.success(request,"Police proceeding successfully added")
		return HttpResponseRedirect(complaintid.get_absolute_url())
	who = request.user
	context={
	"form":form,"who":who,
	}
	return render(request,"CopStatus_form.html",context)


def casestatus_create(request,id=None):
	if not request.user.groups.filter(name="Court").exists():
		raise Http404
	if CaseClose.objects.filter(complaintid=id).exists():
		raise Http404
	complaintid= get_object_or_404(Complaint,complaintid=id)
	instance2=Complaint.objects.get(complaintid=id)

	form =CaseStatusForm(request.POST or None)
	if form.is_valid():
		instance1=form.save(commit=False)
		instance1.complaintid=complaintid
		instance1.save()
		instance2.status="Case Open"
		instance2.save()

		mail = Complaint.objects.filter(complaintid = id)[0].email
		phone = Complaint.objects.filter(complaintid = id)[0].phone
		nameofcomplainant = Complaint.objects.filter(complaintid = id)[0].nameofcomplainant

		msg = MIMEMultipart()
		msg['from'] = 'virtualcopforu@gmail.com'
		msg['to'] = str(mail)
		msg['subject'] = "FIR Filled"
		body = 'Dear '+str(nameofcomplainant)+ ',<br>Court has updated some Proceedings regarding your Case. Please Check them.'

		msg.attach(MIMEText(body, 'html'))
		server = smtplib.SMTP('smtp.gmail.com', 587)
		server.starttls()
		server.login('virtualcopforu@gmail.com', 'A1234@1234')
		text = msg.as_string()
		server.sendmail(msg['From'], msg["to"], text)
		server.quit()
		print("email send success")

		account_sid = 'AC8cdcb1aa84c769a175237de24cc1d18e'
		auth_token= '59f24898c577676e1403161a96910b6a'
		client = Client(account_sid,auth_token)
		message = client.messages.create(
			body='Dear '+str(nameofcomplainant)+ ', Court has updated Some Proceedings regarding your Case. Please Check them. ',
			from_='+12028662408',
			to='+91'+str(phone)
		)
		print("Message Send successfully")

		messages.success(request,"Court proceeding successfully added")
		return HttpResponseRedirect('instance2.get_absolute_url()')
	who= request.user
	context={
	"form":form,
	"who":who
	}
	return render(request,"CourtStatus_form.html",context)


def caseclose(request,id=None):
	if not request.user.groups.filter(name="Court").exists():
		raise Http404
	if CaseClose.objects.filter(complaintid=id).exists():
		raise Http404
	complaintid= get_object_or_404(Complaint,complaintid=id)
	instance2=Complaint.objects.get(complaintid=id)
	form =CaseCloseForm(request.POST or None)
	title="Case Verdict Form"
	if form.is_valid():
		instance=form.save(commit=False)
		instance.complaintid=complaintid
		instance.save()
		instance2.status="Case Closed"
		instance2.save()

		mail = Complaint.objects.filter(complaintid = id)[0].email
		phone = Complaint.objects.filter(complaintid = id)[0].phone
		nameofcomplainant = Complaint.objects.filter(complaintid = id)[0].nameofcomplainant

		msg = MIMEMultipart()
		msg['from'] = 'virtualcopforu@gmail.com'
		msg['to'] = str(mail)
		msg['subject'] = "FIR Filled"
		body = 'Dear '+str(nameofcomplainant)+ ',<br>Your case has been closed Now.<br>Final decision of the court regarding your case is:'
		msg.attach(MIMEText(body, 'html'))
		server = smtplib.SMTP('smtp.gmail.com', 587)
		server.starttls()
		server.login('virtualcopforu@gmail.com', 'A1234@1234')
		text = msg.as_string()
		server.sendmail(msg['From'], msg["to"], text)
		server.quit()
		print("email send success")

		account_sid = 'AC8cdcb1aa84c769a175237de24cc1d18e'
		auth_token= '59f24898c577676e1403161a96910b6a'
		client = Client(account_sid,auth_token)
		message = client.messages.create(
			body='Dear '+str(nameofcomplainant)+ ', Your case has been closed Now. Final decision of the court regarding your case is:',
			from_='+12028662408',
			to='+91'+str(phone)
		)
		print("Message Send successfully")

		messages.success(request,"Case closed successfully")
		return HttpResponseRedirect('/crimefiles/')
	context={
	"title":title,
	"form":form
	}
	return render(request,"CopStatus_form.html",context)


def track_status(request,id=None):
    instance=get_object_or_404(Complaint,complaintid=id)
    if not (request.user.groups.filter(name="Court").exists() or request.user.groups.filter(name="Police").exists() or request.user.groups.filter(name="SHO").exists() or request.user.groups.filter(name="SP").exists() or request.user.groups.filter(name="Facilitator").exists() or request.user.groups.filter(name="Investigator").exists()):
        if not request.user.username==instance.user:
            raise Http404
    instance3=CopStatus.objects.filter(complaintid=id)
    instance4=CaseStatus.objects.filter(complaintid=id)
    instance5=CaseClose.objects.filter(complaintid=id)

    is_compainant = request.user.groups.filter(name='citizen').exists()
    is_cop=request.user.groups.filter(name='Police').exists()
    is_court=request.user.groups.filter(name='Court').exists()

    who=request.user
    print(instance.sho_filefir)
    print(instance.sho_sign)
    print(instance.complaint_registered)
    context={
    "instance":instance,
    "instance3":instance3,
    "instance4":instance4,
    "instance5":instance5,
    "is_compainant":is_compainant,
    "is_court":is_court,
    "is_cop":is_cop,
    "who":who,
    }
    return render(request,"track_status.html",context)


def complaint_detail(request,id=None):
	instance=get_object_or_404(Complaint,complaintid=id)
	if not (request.user.groups.filter(name="Police").exists()or request.user.groups.filter(name="Court") or request.user.groups.filter(name="SHO").exists() or request.user.groups.filter(name="SP").exists() or request.user.groups.filter(name="Facilitator").exists()):
		if not request.user.username==instance.user:
			raise Http404

	instance3=CopStatus.objects.filter(complaintid=id)
	instance4=CaseStatus.objects.filter(complaintid=id)
	instance5=CaseClose.objects.filter(complaintid=id)
	instance6=freport.objects.filter(complaintid=id)

	# # mail = User.objects.filter
	# who=request.user
	# # mail = request.user
	# # print(mail)
	# id1 = instance.complaintid
	# print(id1)
	# # mail = User.objects.all()
	print(instance.declinedstatus)
	print(instance.decline_reason_police)
	print(instance.sketchstatus)
	print(instance.csignstatus)
	print(instance.aadharverification_status)
	print(instance.fassignstatus)
	print(instance.freport_status)
	print(instance.nameoffacilitator)
	print(instance.status)
	print(instance.signedstatus)
	print(instance.declinedstatus)
	print(instance.iassignstatus)
	print(instance.payment)

	global gid
	gid = id
	print(gid)
	is_compainant = request.user.groups.filter(name='citizen').exists()
	is_police=request.user.groups.filter(name='Police').exists()
	is_court=request.user.groups.filter(name='Court').exists()
	is_sho = request.user.groups.filter(name='SHO').exists()
	is_sp = request.user.groups.filter(name='SP').exists()
	is_facilitator = request.user.groups.filter(name='Facilitator').exists()

	filename = id+"_"+instance.nameofcomplainant
	print(filename)
	# newfile='Criminal Sketches/'+str(filename)+'.png'

	print(instance.nameoffacilitator)
	choosen_f = instance.nameoffacilitator
	f_instance = Facilitator_details.objects.filter(nameoffacilitator = str(choosen_f))
	print(f_instance)

	choosen_i = instance.nameofinvestigatorassigned
	i_instance = Investigator_details.objects.filter(nameofinvestigator = choosen_i)

	freport_instance = freport.objects.filter(complaintid = id)
	# print(freport_instance.f_evidence1)

	who=request.user
	context={
	"title":instance.complaintid, "instance":instance,
	"instance3":instance3, "instance4":instance4, "instance5":instance5,"instance6":instance6,
	"is_compainant":is_compainant, "is_court":is_court, "is_police":is_police,
	"is_sho":is_sho, "is_sp":is_sp, "is_facilitator":is_facilitator,"filename":filename, "who":who,"f_instance":f_instance,
	"freport_instance":freport_instance,"i_instance":i_instance,
	}

	return render(request,"complaint_detail.html",context)


def complaint_list(request):
	# print request.user
	if not request.user.is_authenticated:
		return HttpResponseRedirect("/crimefiles/login")
	if request.user.groups.filter(name="Police").exists():
		queryset_list=Complaint.objects.all().order_by("-dateofcomplaint")
		# fir = "Complaint Registered"
		# queryset_list = Complaint.objects.all().order_by("-priority","dateofcomplaint")
	elif request.user.groups.filter(name='Court').exists():
		# queryset_list=Complaint.objects.all().order_by("-dateofcomplaint")
		queryset_list = Complaint.objects.filter(payment = True).order_by("-dateofcomplaint")
	elif request.user.groups.filter(name='SHO').exists():
		# fir = "Complaint Registered"
		# queryset_list = Complaint.objects.all().order_by("-priority","dateofcomplaint")
		queryset_list = Complaint.objects.all().order_by("-dateofcomplaint")
	elif request.user.groups.filter(name='SP').exists():
		queryset_list = Complaint.objects.all().order_by("-dateofcomplaint")
	elif request.user.groups.filter(name='Facilitator').exists():
		# queryset_list = Complaint.objects.all().order_by("-dateofcomplaint")
		fstatus = "Facilitator Assigned"
		queryset_list = Complaint.objects.filter(fassignstatus = fstatus).order_by("-dateofcomplaint")
		# print(queryset_list)
	elif request.user.groups.filter(name='Investigator').exists():
		# queryset_list = Complaint.objects.all().order_by("-dateofcomplaint")
		istatus = "Investigator Assigned"
		queryset_list = Complaint.objects.filter(iassignstatus = istatus).order_by("-dateofcomplaint")
		# print(queryset_list)
	else:
		queryset_list=Complaint.objects.filter(user=request.user.username).order_by("-dateofcomplaint")
	query = request.GET.get("q")
	if query:
		queryset_list=queryset_list.filter(Q(complaintid__icontains=query)|
		Q(content__icontains=query)|
		Q(policestation__icontains=query)|
		Q(location__icontains=query)
		).distinct()
	paginator = Paginator(queryset_list, 5) # Show 25 contacts per page
	who=request.user
	page = request.GET.get('page')
	is_facilitator = request.user.groups.filter(name='Facilitator').exists()
	is_investigator = request.user.groups.filter(name='Investigator').exists()
	try:
		queryset = paginator.page(page)
	except PageNotAnInteger:
		# If page is not an integer, deliver first page.
		queryset = paginator.page(1)
	except EmptyPage:
		# If page is out of range (e.g. 9999), deliver last page of results.
		queryset = paginator.page(paginator.num_pages)
	colors='danger'
	instance = Complaint.objects.all()
	instance1 = Complaint.objects.filter(nameoffacilitator = who )
	# print(instance1[0].nameoffacilitator==str(who))
	instance2 = Complaint.objects.filter(nameoffacilitator = who )
	# print(instance1)
	# print(instance2.nameoffacilitator)
	# print(type(str(who)))
	context={
	"who":str(who),
	"object_list":queryset,
	"title":"Complaint lists",
	"colors":colors,
	"instance":instance,
	"instance1":instance1,
	"is_facilitator":is_facilitator,
	"is_investigator":is_investigator,
	}
	# print(instance.nameoffacilitator == who)
	return render(request,"complaint_list.html",context)

#
# def complaint_update(request,id= None):
# 	if not request.user.is_superuser:
# 		if request.user.groups.filter(name="Police").exists() or request.user.groups.filter(name="Court").exists():
# 	 		raise Http404
# 	if Fir.objects.filter(complaintid=id).exists():
# 		raise Http404
# 	instance=get_object_or_404(Complaint,complaintid=id)
# 	if not request.user.username==instance.user:
# 		raise Http404
# 	form =ComplaintForm(request.POST or None,instance=instance)
# 	if form.is_valid():
# 		instance=form.save(commit=False)
# 		instance.save()
#
# 		#update by sending mail and msg
#
# 		messages.success(request,"sucessfully updated",extra_tags="xtra")
# 		return HttpResponseRedirect(instance.get_absolute_url())
# 	context={
# 	"title":instance.complaintid,
# 	"instance":instance,
# 	"form":form,
# 	}
# 	return render(request,"complaint_form.html",context)

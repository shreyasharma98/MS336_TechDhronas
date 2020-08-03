from django.urls import path,re_path,include
from django.contrib import admin
from django.contrib.auth.views import login
from django.views.generic import TemplateView
from .views import faceback,nextstep,location, home_page, uploaddsp, uploaddsho,uploadcomplaintrec,CourtPayment,handlerequest,request_magistrate,drop_complaint,i_portal,investigator_details,save_signature_court,save_signature_p,save_signature_sho,save_signature_sp, openfile, upload,fevidences, check_otp, skip_aadhar, verify_aadhar, facilitator_details, skip_sketch, save_signature,open_sketch, save_sketch, fir_pdf, complaint_create_new, complaint_detail,track_status,complaint_list,copstatus_create,casestatus_create,login,caseclose,fir_create_police,fir_create_sho,fir_create_sp,fir_create_court,fir_decline_police,fir_decline_sho,fir_decline_sp
from django.contrib.auth import views as auth_views
from . import views

app_name='crimefiles'
urlpatterns = [
    re_path(r'^login/',auth_views.login,name='login',kwargs={'template_name': 'login_form.html'}),
	# re_path(r'^createcomplaint$',complaint_create),
	re_path(r'^createcomplaintnew$',complaint_create_new),

    re_path('analytics/',include("app.urls")),
	re_path('wanted/',include("wanted.urls")),

	re_path(r'^faceback$',faceback),
	re_path(r'^nextstep$',nextstep),

	re_path(r'^(?P<id>\d+)/createfirpolice$',fir_create_police),
	re_path(r'^(?P<id>\d+)/createfirsho$',fir_create_sho),
	re_path(r'^(?P<id>\d+)/createfirsp$',fir_create_sp),
	re_path(r'^(?P<id>\d+)/createfircourt$',fir_create_court),

	re_path(r'^(?P<id>\d+)/declinefirpolice$',fir_decline_police),
	re_path(r'^(?P<id>\d+)/declinefirsho$',fir_decline_sho),
	re_path(r'^(?P<id>\d+)/declinefirsp$',fir_decline_sp),

	re_path(r'^(?P<id>\d+)/createcopstatus$',copstatus_create),
	re_path(r'^(?P<id>\d+)/createcasestatus$',casestatus_create),
	re_path(r'^(?P<id>\d+)/closecase$',caseclose),

	re_path(r'^(?P<id>\d+)/fir_pdf$',fir_pdf),
	re_path(r'^(?P<id>\d+)/open_sketch$',open_sketch),
	re_path(r'^(?P<id>\d+)/save_sketch$',save_sketch),
	re_path(r'^(?P<id>\d+)/skip_sketch$',skip_sketch),

    re_path(r'^location/$', location,name="location"),


	re_path(r'^(?P<id>\d+)/verify_aadhar$',verify_aadhar),
	re_path(r'^(?P<id>\d+)/skip_aadhar$',skip_aadhar),
	re_path(r'^check_otp$',check_otp),

	re_path(r'^(?P<id>\d+)/save_signature$',save_signature),
	re_path(r'^(?P<id>\d+)/save_signature_p$',save_signature_p),
	re_path(r'^(?P<id>\d+)/save_signature_sho$',save_signature_sho),
	re_path(r'^(?P<id>\d+)/save_signature_sp$',save_signature_sp),
	re_path(r'^(?P<id>\d+)/save_signature_court$',save_signature_court),

    path("upload/", upload,name="upload"),
	path("uploaddsp/", uploaddsp,name="uploaddsp"),
	path("uploaddsho/", uploaddsho,name="uploaddsho"),
	path("uploadcomplaintrec/", uploadcomplaintrec,name="uploadcomplaintrec"),
	path("openfile/", openfile,name="openfile"),

	re_path(r'^(?P<id>\d+)/facilitator_details$',facilitator_details),
	re_path(r'^(?P<id>\d+)/fevidences$',fevidences),

	re_path(r'^(?P<id>\d+)/investigator_details$',investigator_details),
	re_path(r'^(?P<id>\d+)/i_portal$',i_portal),

	path('', home_page,name="home_page"),
	path('complaint_list/', complaint_list,name="list"),

	# re_path(r'^(?P<id>\d+)/edit$', complaint_update,name="update"),
	re_path(r'^(?P<id>\d+)/$', complaint_detail,name="detail"),
	re_path(r'^(?P<id>\d+)/track$', track_status,name="track"),

    re_path(r'^(?P<id>\d+)/request_magistrate$',request_magistrate),
	re_path(r'^(?P<id>\d+)/drop_complaint$',drop_complaint),

#payment
	path("courtpayment/", CourtPayment, name="Checkout"),
    path("handlerequest/",handlerequest, name="HandleRequest"),	]

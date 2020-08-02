# from django.conf.re_paths import re_path
from . import views
# from django.re_paths import path
# from django.re_paths import path,re_path,include
from .views import home_page, wrtstate
from django.urls import path,re_path,include

app_name='app'

urlpatterns = [
	# re_path(r'^$', views.redi , name = 'redi'),
    # # re_path(r'^index', views.login , name = 'login'),
    # re_path(r'^login/$', views.login , name = 'login'),
    # re_path(r'^register', views.register , name = 'register'),

    # path('', home_page,name="home_page"),
    re_path(r'^overyears$', wrtstate),
    re_path(r'^chart2001$', views.chart2001 , name = 'chart2001'),
    re_path(r'^chart2002$', views.chart2002 , name = 'chart2002'),
    re_path(r'^chart2003$', views.chart2003 , name = 'chart2003'),
    re_path(r'^chart2004$', views.chart2004 , name = 'chart2004'),
    re_path(r'^chart2005$', views.chart2005 , name = 'chart2005'),
    re_path(r'^chart2006$', views.chart2006 , name = 'chart2006'),
    re_path(r'^chart2007$', views.chart2007 , name = 'chart2007'),
    re_path(r'^chart2008$', views.chart2008 , name = 'chart2008'),
    re_path(r'^chart2009$', views.chart2009 , name = 'chart2009'),
    re_path(r'^chart2010$', views.chart2010 , name = 'chart2010'),

    re_path(r'^pie2001', views.pie2001 , name = 'pie2001'),
    re_path(r'^pie2002', views.pie2002 , name = 'ddds'),
    re_path(r'^pie2003', views.pie2003 , name = 'sdf'),
    re_path(r'^pie2004', views.pie2004 , name = 'mzzm'),
    re_path(r'^pie2005', views.pie2005 , name = 'amm'),
    re_path(r'^pie2006', views.pie2006 , name = 'mdmsd'),
    re_path(r'^pie2007', views.pie2007 , name = 'sms'),
    re_path(r'^pie2008', views.pie2008 , name = 'smsss'),
    re_path(r'^pie2009', views.pie2009 , name = 'lvl'),
    re_path(r'^pie2010', views.pie2010 , name = 'trr'),

    re_path(r'^murders$', views.murders , name = 'murders'),
    re_path(r'^murd2001', views.murd2001 , name = 'murd2001'),
    re_path(r'^murd2002', views.murd2002 , name = 'murd2002'),
    re_path(r'^murd2003', views.murd2003 , name = 'murd20103'),
    re_path(r'^murd2004', views.murd2004 , name = 'murd201022'),
    re_path(r'^murd2005', views.murd2005 , name = 'murd2010we'),
    re_path(r'^murd2006', views.murd2006 , name = 'murd2010weqw'),
    re_path(r'^murd2007', views.murd2007 , name = 'murd2010wrar'),
    re_path(r'^murd2008', views.murd2008 , name = 'murd201011'),
    re_path(r'^murd2009', views.murd2009 , name = 'murd2010emke'),
    re_path(r'^murd2010', views.murd2010 , name = 'murd2010'),

    re_path(r'^murdpie2001', views.murdpie2001 , name = 'murdpie2001'),
    re_path(r'^murdpie2002', views.murdpie2002 , name = 'murdpie2002'),
    re_path(r'^murdpie2003', views.murdpie2003 , name = 'murdpie2003'),
    re_path(r'^murdpie2004', views.murdpie2004 , name = 'murdpie2004'),
    re_path(r'^murdpie2005', views.murdpie2005 , name = 'murdpie2005'),
    re_path(r'^murdpie2006', views.murdpie2006 , name = 'murdpie2006'),
    re_path(r'^murdpie2007', views.murdpie2007 , name = 'murdpie2007'),
    re_path(r'^murdpie2008', views.murdpie2008 , name = 'murdpie2008'),
    re_path(r'^murdpie2009', views.murdpie2009 , name = 'murdpie2009'),
    re_path(r'^murdpie2010', views.murdpie2010 , name = 'murdpie2010'),

    re_path(r'^shooting', views.shooting , name = 'shooting'),
    re_path(r'^shot_kil', views.shot_kil , name = 'shot_kil'),
    re_path(r'^shot_inj', views.shot_inj , name = 'shot'),
    re_path(r'^injkill', views.injkill , name = 'shotkill'),
    re_path(r'^fatal', views.fatal , name = 'fatal'),
    re_path(r'^death', views.death , name = 'death'),
    re_path(r'^inj', views.inj , name = 'inj'),
    re_path(r'^diainj', views.diainj , name = 'diainj'),
    re_path(r'^deaandinj', views.deaandinj , name = 'deaandinj'),
    re_path(r'^formcrimesagaintswomen', views.add , name = 'add_model'),
    re_path(r'^formmurder', views.addmv , name = 'addmv'),
    re_path(r'^sanfrancisco', views.sss , name = 'sanfrancisco'),
    re_path(r'^page1', views.page1 , name = 'page1'),

]

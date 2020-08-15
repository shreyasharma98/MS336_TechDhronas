# -*- coding: utf-8 -*-
from __future__ import unicode_literals
from django.http import JsonResponse
from django.shortcuts import render
from django.http import HttpResponse
from django.views.decorators.http import require_http_methods
import dialogflow
import os
import json
from django.views.decorators.csrf import csrf_exempt
from django.http import HttpResponse,HttpResponseRedirect,Http404
from django.contrib.auth import authenticate, login
#from dialogflow_v2 import dialogflow_v2 as Dialogflow
# Create your views here.
data={}
query="Victim/Witness"
@require_http_methods(['GET'])
def index_view(request):
    if not request.user.is_authenticated:
        return HttpResponseRedirect("/crimefiles/login")
    who = request.user
    return render(request, 'ItHasNavigationBar.html', {"who":who})
def getdata():
    return data
def convert(data):
    if isinstance(data, bytes):
        return data.decode('ascii')
    if isinstance(data, dict):
        return dict(map(convert, data.items()))
    if isinstance(data, tuple):
        return map(convert, data)

    return data

@csrf_exempt
@require_http_methods(['POST'])
def chat_view(request):
    print('Body', request.body)
    input_dict = convert(request.body)
    input_text = json.loads(input_dict)['text']

    GOOGLE_AUTHENTICATION_FILE_NAME = "xyz-clofsr.json"
    current_directory = os.path.dirname(os.path.realpath(__file__))
    path = os.path.join(current_directory, GOOGLE_AUTHENTICATION_FILE_NAME)
    os.environ["GOOGLE_APPLICATION_CREDENTIALS"] = path

    GOOGLE_PROJECT_ID = "xyz-clofsr"
    session_id = "1234567891"
    context_short_name = "does_not_matter"

    context_name = "projects/" + GOOGLE_PROJECT_ID + "/agent/sessions/" + session_id + "/contexts/" + \
               context_short_name.lower()

    parameters = dialogflow.types.struct_pb2.Struct()
    #parameters["foo"] = "bar"

    context_1 = dialogflow.types.context_pb2.Context(
        name=context_name,
        lifespan_count=2,
        parameters=parameters
    )
    query_params_1 = {"contexts": [context_1]}

    language_code = 'en'
    response = detect_intent_with_parameters(
        project_id=GOOGLE_PROJECT_ID,
        session_id=session_id,
        query_params=query_params_1,
        language_code=language_code,
        user_input=input_text
    )
    return HttpResponse(response.query_result.fulfillment_text, status=200)

def detect_intent_with_parameters(project_id, session_id, query_params, language_code, user_input):
    """Returns the result of detect intent with texts as inputs.

    Using the same `session_id` between requests allows continuation
    of the conversaion."""
    session_client = dialogflow.SessionsClient()

    session = session_client.session_path(project_id, session_id)
    print('Session path: {}\n'.format(session))

    #text = "this is as test"
    text = user_input

    text_input = dialogflow.types.TextInput(
        text=text, language_code=language_code)

    query_input = dialogflow.types.QueryInput(text=text_input)

    response = session_client.detect_intent(
        session=session, query_input=query_input,
        query_params=query_params
    )

    print('=' * 20)
    print('Query text: {}'.format(response.query_result.query_text))
    try:
        print(response.query_result.parameters.fields,"-----------------------------.")
        print(response.query_result.parameters.fields['any'].string_value,"-----------------------------.")
        # print(response.query_result)
        print(response.query_result.parameters.fields,"-----------------------------.")
    except:
        print('Nope')
    print('Detected intent: {} (confidence: {})\n'.format(
        response.query_result.intent.display_name,
        response.query_result.intent_detection_confidence))
    print('Fulfillment text: {}\n'.format(
        response.query_result.fulfillment_text))
    global query
    print(query,response.query_result.query_text)
    if 'full name' in query:
        data['name']=response.query_result.parameters.fields['any'].string_value
    elif 'age' in query:
        data['age']=response.query_result.parameters.fields['number'].number_value
    elif 'current address' in query:
        data['address']=response.query_result.parameters.fields['any'].string_value
    elif 'contact number' in query:
        data['phone']=response.query_result.parameters.fields['phone-number'].string_value
    elif 'Email-Id' in query:
        data['email']=response.query_result.parameters.fields['email'].string_value
    elif 'witness or victim' in query:
        data['role']=response.query_result.query_text
    elif 'date of Incident' in query:
        data['date']=response.query_result.query_text
    elif "Incident's time" in query:
        data['time']=response.query_result.query_text
    elif "Place" in query:
        data['iplace']=response.query_result.query_text
    elif "Type of incidence" in query:
        data['itype']=response.query_result.query_text
    elif 'Description of' in query:
        data['idescription']=response.query_result.query_text
    elif 'name of suspect' in query:
        data['suspectname']=response.query_result.query_text
    elif 'address of suspect' in query:
        data['suspectaddress']=response.query_result.query_text
    elif 'know about the suspect' in query:
        data['suspectdescription']=response.query_result.query_text
    else:
        pass
    print(data)
    query=response.query_result.fulfillment_text
    return response


def about(request):
    return render(request, 'chat/about.html')
from django.shortcuts import render
from django.http import JsonResponse, HttpResponse, FileResponse
from django.template.response import TemplateResponse
from .models import *
from .forms import *

# Create your views here.
def index(request):
    return render(request, 'Messenger/index.html')



def home(request, phone = "000"):
    if request.method == 'POST':
        data = request.POST.copy()
        data['From'] = phone
        formComp = MessageForm2(data)
        fCp = formComp.save(commit = False)
        if 'photo' in request.FILES:
            fCp.photo = request.FILES['photo']
        fCp.save()
    msgs = Messages.objects.all()
    user_msgs = []
    for msg in msgs:
        if msg.From==phone or msg.To==phone:
            user_msg = {}
            user_msg["is_from"] = msg.From == phone
            user_msg["other_phone"] = msg.From if msg.To == phone else msg.To
            user_msg['text'] = msg.Text
            user_msg['date'] = msg.date_time
            user_msg['url'] = msg.photo.url if msg.photo else ''
            user_msg['isphoto'] = True if msg.photo else False
            user_msgs.append(user_msg)
    user_msgs.reverse()
    form = MessageForm()
    mydict = {
        'form' : form,
        'user_msgs' : user_msgs,
        'phone' : phone
    }
    return TemplateResponse(request, 'Messenger/home.html', context = mydict)




def send_message(request):
    if request.method == 'POST':
        formComp = MessageForm2(request.POST)
        fCp = formComp.save(commit = False)
        if 'photo' in request.FILES:
            fCp.photo = request.FILES['photo']
        fCp.save()
        response = {
            'message' : 'Message sent'
        }
        return JsonResponse(response)

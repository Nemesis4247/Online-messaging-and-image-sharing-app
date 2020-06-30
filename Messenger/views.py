from django.shortcuts import render
from django.http import JsonResponse, HttpResponse, FileResponse
from django.template.response import TemplateResponse
from .models import *
from .forms import *

# Create your views here.
def index(request):
    return render(request, 'Messenger/index.html')

def home(request, phone = 000):
    form = MessageForm()
    mydict = {
        'form' : form,
    }
    if request.method == 'POST':
        data = request.POST.copy()
        data['From'] = phone
        formComp = MessageForm2(data)
        fCp = formComp.save(commit = False)
        if 'photo' in request.FILES:
            fCp.photo = request.FILES['photo']
        fCp.save()
    user = phone
    msgs = Messages.objects.all()
    # print(msgs)
    user_msgs = []
    user_photos = []
    for msg in msgs:
        user_msg = {}
        user_photo = {}
        if msg.From == user:
            user_msg["is_from"] = True
            user_msg["other_phone"] = msg.To

            user_msg['text'] = msg.Text
            user_msg['date'] = msg.date_time
            user_msgs.append(user_msg)
            if msg.photo :
                user_photo["other_phone"] = msg.To
                user_photo['url'] = msg.photo.url
                # print(user_photo)
                user_photos.append(user_photo)
        if msg.To == user:
            user_msg["is_from"] = False
            user_msg["other_phone"] = msg.From
            user_msg['text'] = msg.Text
            user_msg['date'] = msg.date_time
            user_msgs.append(user_msg)
            if msg.photo :
                user_photo["other_phone"] = msg.From
                user_photo['url'] = msg.photo.url
                # print(user_photo)
                user_photos.append(user_photo)
    user_msgs.reverse()
    user_photos.reverse()
    mydict['user_msgs'] = user_msgs
    mydict['user_photos'] = user_photos
    # mydict['show_prompt'] = False
    mydict['phone'] = user

    return TemplateResponse(request, 'Messenger/home.html', context = mydict)


def send_message(request):
    if request.method == 'POST':
        # print(request.POST)
        # print(request.POST['To'])
        # print(request.POST['From'])
        # Messages.objects.create(From = request.POST['From'], To = request.POST['To'], Text = request.POST['Text'])
        form = MessageForm2(request.POST)
        form.save(commit = True)
        response = {
            'message' : 'Message sent'
        }
        return JsonResponse(response)

def recent_conv(request):
    if request.method=='POST':
        print("sssssssssssssssssssssssssssssssssssssssssssssssssssssssss")
        print(request.POST)
        user = "9415900191"
        msgs = Messages.objects.all()
        print(msgs)
        user_msgs = []
        for msg in msgs:
            user_msg = {}
            if msg.From == user:
                user_msg["is_from"] = True
                user_msg["other_phone"] = msg.To
                user_msg['text'] = msg.Text
                user_msg['date'] = msg.date_time
            if msg.To == user:
                user_msg["is_from"] = False
                user_msg["other_phone"] = msg.From
                user_msg['text'] = msg.Text
                user_msg['date'] = msg.date_time
            print(user_msg)
            user_msgs.append(user_msg)
        response = {
            'result' : user_msgs
        }
        return JsonResponse(response)

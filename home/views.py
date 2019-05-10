from django.shortcuts import render
from django.shortcuts import redirect
from .models import Posts, Comments
from django.http import HttpResponse, HttpResponseRedirect
from django.views.generic import DetailView
from django.db.models import Q
from .forms import Commentform

#
# import base64
# from email.mime.audio import MIMEAudio
# from email.mime.base import MIMEBase
# from email.mime.image import MIMEImage
# from email.mime.multipart import MIMEMultipart
# from email.mime.text import MIMEText
# import mimetypes
# import os
# from apiclient.discovery import build
#
# from apiclient import errors

def Homepage(request):
    return render(request,'homepage/home.html')

def Projectpage(request,category):
    # category = kwargs.get("category")
    query = request.GET.get('search', None)
    print(query)
    if query:
        obj = Posts.objects.filter(Q(title__iexact=query)|Q(title__icontains=query)|Q(mission__icontains=query)|Q(ssrid__icontains=query)|Q(content__icontains=query))
        print(obj)
        if not obj:
            obj = Posts.objects.all()
    else:
        if category == 'all':
            obj = Posts.objects.all()
        else:
            obj = Posts.objects.filter(Q(category__icontains=category))
    # obj = obj.order_by('-views')
    context = {
        "obj":obj,
    }
    return render(request,'projectpage/project.html',context)

# def create_message(sender, to, subject, message_text):
#   message = MIMEText(message_text)
#   message['to'] = to
#   message['from'] = sender
#   message['subject'] = subject
#   return {'raw': base64.urlsafe_b64encode(message.as_string())}
#
# def send_message(service, user_id, message):
#     try:
#         message = (service.users().messages().send(userId=user_id, body=message).execute())
#         print('Message Id: %s' % message['id'])
#         return message
#     except(errors.HttpError, error):
#         print('An error occurred: %s' % error)

import os
import random

def Blogpage(request, id):
    path="./static/images/"+str(id)  # insert the path to your directory
    img_list = os.listdir(path)
    l = len(img_list)
    if len(img_list) > 5:
        ind = random.sample(range(0,l),5)
        print(ind)
    else:
        ind = random.sample(range(0,l),l)
        lis = img_list
    lis = [img_list[i] for i in ind]

    print(img_list)
    obj = Posts.objects.get(ssrid=id)
    form = Commentform()
    if request.method == 'POST':
        form2 = Commentform(request.POST)
        if form2.is_valid():
            Comments1 = form2.save(commit=False)
            Comments1.ssrid = id
            Comments1.save()
            return HttpResponseRedirect('/blog/'+str(id))
    else:
        com = Comments.objects.filter(Q(ssrid__iexact=id))
        obj.views = obj.views + 1;
        obj.save()
        context = {
            "obj":obj,
            "form":form,
            "comment":com,
            "img":lis,
        }
        return render(request,'blogpage/blog.html',context)

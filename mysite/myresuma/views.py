from django.shortcuts import render
from myresuma.bot import *

def chatbot_response(question):
    chat_with_gpt(question)
    return chat_with_gpt(question)

def my_view(request):
    response = ""
    if request.method == 'POST':
        question = request.POST.get('question')
        response = chatbot_response(question)
    return render(request, 'index.html', {'response': response})
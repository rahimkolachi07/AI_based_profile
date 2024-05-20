from django.shortcuts import render
from myresuma.bot import *
from myresuma.main import *
import threading

def chatbot_response(question):
    chat_with_gpt(question)
    return chat_with_gpt(question)

def my_view(request):
    response = ""
    if request.method == 'POST':
        question = request.POST.get('question')
        response = chatbot_response(question)
    return render(request, 'index.html', {'response': response})

def home(request):
    text = "Enter any Website"
    if request.method == 'POST':
        text = request.POST.get('input_text')
        print("text", text)
        input_thread = threading.Thread(target=main_func, args=(text,))
        input_thread.start()

    return render(request, 'email.html')
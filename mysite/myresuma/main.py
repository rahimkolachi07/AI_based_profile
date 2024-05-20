from myresuma.gemini.gemini import *
from myresuma.email_extr import *
from myresuma.email_sending import *
import sqlite3 
conn=sqlite3.connect("website_database.db")
cursor=conn.cursor()
tables="CREATE TABLE IF NOT EXISTS tab (website TEXT)"
cursor.execute(tables)
conn.commit()
def main_func(url):
    try:
        print("url:",url)
        conn=sqlite3.connect("website_database.db")
        cursor=conn.cursor()
        cursor.execute("SELECT * FROM tab")
        rows=cursor.fetchall()
        a=0
        for row in rows:
            
            if row[0]==url:
                a=1
                return "already done"

        if a==0:
            cursor.execute("INSERT INTO tab (website) VALUES (?)",[url])
            conn.commit()
            emails,text=extract_emails(url)
            print("emails :",emails)
            try:
                text=g_modelpr(f"write best email body for job. this is description of my cv [Name ABDUL RAHIM I am a Machine Learning Engineer with over 4 years of professional experience in developing, implementing and optimizing AI-based solutions. I have an extensive knowledge of deep learning, natural language processing (NLP) and machine learning frameworks such as Transformers, Pytorch, TensorFlow, Keras and Scikit-Learn. My experience includes developing, training and deploying LLMs, GPT, LLAMA, GAN, image generation, Automation Systems, AI Bots, Image Recognition, Voice Cloning, Deepfake, lip2wav to production systems, as well as building custom APIs and web applications. I am proficient in programming languages such as Python. I have also implemented end-to-end AI projects, including Data Pre-processing, Model training, Testing and Deployment on AWS. My work has enabled clients to improve their efficiency, accuracy and cost effectiveness. i am availbe for remote job, on site, hybride i can relocate for your company ] and here is the company website details [{text}] modify email according to conmpany website. must add my portfolio link http://rahimkolachi.site:7005/ . this portfolio link is most important to send to recruter. dont add [], * etc make professional emails no any dummy words etc, try to fetch compnay name from text if company name not avaialbe then dont mention [Company Name]. dont add subject. extract compnay name from emails if possible {emails}")
                subject=g_modelpr(f"retun only subject for my email body for job, return professional subject. . no extra text. i need only subject text. this is the body of the email {text}. i only need subject")
            
            except Exception as e:
                print(e)
            for email in emails:
                email_sending(email,text,subject)
        return "done"
    except Exception as e:
        print(e)

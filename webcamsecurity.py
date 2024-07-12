import tkinter as tk
from PIL import ImageTk, Image
from tkinter import Tk,PhotoImage
import random
import string
import os
from tkinter import messagebox
import subprocess
import tempfile
import webbrowser
import io

def projectinfo():
    html_code="""
        <!DOCTYPE html>
        <html>
        <head>
            <title>Developers Information</title>
            <meta name="viewport" content="width=device-width, initial-scale=1.0">
            <style>
                body{
                    font-family:Arial,sans-serif;
                    margin:0;
                    padding:0;
                    background-color: #f2f2f2;
                }
                .container{
                    max-width: 800px;
                    margin: 0 auto;
                    padding: 50px 20px;
                    background-color: #fff;
                    box-shadow: 0 0 10px rgba(0,0,0,0.2);
                    border-radius: 4px;
                    position: relative;
                }
                h1{
                    font-size: 36px;
                    margin-bottom: 30px;
                }
                p{
                    font-size: 18px;
                    line-height: 1.5;
                    margin-bottom: 20px;
                }
                table {
                    width:100%;
                    margin-bottom: 20px;
                    border-collapse: collapse;
                }
                table td,table th {
                    padding: 8px;
                    text-align: left;
                    border:1px solid #ddd;
                }
                table th {
                    background-color: #f2f2f2;
                    font-size: 18px;
                }
                @media only screen and (max-Width: 600px){
                    .container{
                        padding: 30px 10px;
                    }
                    h1{
                        font-size:24px;
                    }
                    p{
                        font-size: 16px;
                    }
                    table td,
                    table th{
                        padding:5px;
                        font-size: 16px;

                    }
                    table th{
                        font-size:16px;
                    }
                }
            </style>
        </head>
        <body>
            <div class="container">
            <h1>
                Project Information
            </h1>
            <p>
                This project was developed by <strong>Vikram , Bhavana , Jahnavi</strong> as part of <strong>cybersecurity Internship</strong>. This project is designed to <strong>Secure the Organisation in Real World from Cyber Frauds performed by Hackers</strong>.
            </p>
            <table>
                <thead>
                    <tr>
                        <th>Project Details</th>
                        <th>Value</th>
                    </tr>
                </thead>
                <tbody>
                    <tr>
                        <td>Project Name</td>
                        <td>Web Cam Security from spyware</td>
                    </tr>
                    <tr>
                        <td>Project Description</td>
                        <td>Implementing Physical Security Policy on Web Cam in Devices to Prevent Spyware Activities</td>
                    </tr>
                    <tr>
                        <td>Project Start Date</td>
                        <td>17-Febrauary-2024</td>
                    </tr>
                    <tr>
                        <td>Project End Dte</td>
                        <td>17-March-2024</td>
                    </tr>
                    <tr>
                        <td>Project Status</td>
                        <td><b>Completed</b></td>
                    </tr>
                </tbody>
            </table>
            <h2>Developer Details</h2>
            <table>
                <thead>
                    <tr>
                        <th>Name</th>
                        <th>Email</th>
                    </tr>
                </thead>
                <tbody>
                    <tr>
                        <td>V.Vikram</td>
                        <td>Vemanaboinavikram04@gmail.com</td>
                    </tr>
                    <tr>
                        <td>Ch.Bhavana</td>
                        <td>bhavanachimmili15@gmail.com</td>
                    </tr>
                    <tr>
                        <td>Ch.Jahnavi</td>
                        <td>jahnavich2003@gmail.com</td>
                    </tr>
                </tbody>
            </table>
            <h2>Company Details</h2>
            <table>
                <thead>
                    <tr>
                        <th>Name</th>
                        <th>Email</th>
                    </tr>
                </thead>
                <tbody>
                    <tr>
                        <td>Supraja Technologies</td>
                        <td>contact@suprajatechnologies.com</td>
                    </tr>
                </tbody>
            </table>
        </div>
        </center>
        </body>
        </html>
    """
    
    with tempfile.NamedTemporaryFile(mode='w',delete=False,suffix='.html') as temp_file:
        temp_file.write(html_code)
        temp_file_path=temp_file.name
        
    webbrowser.open('file://'+os.path.realpath(temp_file_path))


def gen_pas(entry):
    def generate_password(length=10):
        characters = string.ascii_letters + string.digits
        password = ''.join(random.choice(characters) for _ in range(length))
        return password
    
    def store_password(filename, password):
        with open(filename, 'w') as file:
            file.write(password)
    
    random_password = generate_password()
    filename = 'password.txt'
    store_password(filename, random_password)

def display_passwords(entry):
    if "password.txt" in os.listdir():
        with open("password.txt", "r") as file:
            passwords = file.read()

            entry.insert(0, passwords)
    else:
        entry.delete(0, tk.END)
        entry.insert(0, "Password file not found")

def che_dis(entry):
    input_password = entry.get()
    with open("password.txt", "r") as file:
        saved_passwords = file.readlines()
    if input_password in saved_passwords:
        del_cmd = r'reg delete "HKLM\SOFTWARE\Microsoft\Windows\CurrentVersion\CapabilityAccessManager\ConsentStore\webcam" /v Value /f'
        subprocess.run(del_cmd, shell=True)
        add_cmd = r'reg add "HKLM\SOFTWARE\Microsoft\Windows\CurrentVersion\CapabilityAccessManager\ConsentStore\webcam" /v Value /t REG_DWORD /d 0 /f'
        subprocess.run(add_cmd, shell=True)
        success_label.config(text="Camera disabled!",bg="white" ,fg="green")
    else:
        success_label.config(text="Password is incorrect",bg="white" ,fg="red")  

def dis_click():
    global success_label  
    root1 = tk.Toplevel()
    root1.title("DISABLE")
    root1.geometry("550x550")
    root1.configure(bg="#6E4040")
    img1= Image.open('logo.png')
    image1 = ImageTk.PhotoImage(img1)
    image_label1 = tk.Label(root1, image=image1)
    image_label1.pack(pady=10,padx=100)
    label = tk.Label(root1, text="Enter Text:",bg="antiquewhite",fg="black",font=("HELVETICA",13,"bold"),activebackground="rosybrown",width=20)
    label.pack(pady=10)
    entry = tk.Entry(root1,show='*',width=30)
    entry.pack(pady=10)
    button1 = tk.Button(root1, text="GENERATE THE PASSWORD",bg="antiquewhite",fg="black",font=("HELVETICA",13,"bold"),activebackground="rosybrown",width=25, command=lambda: gen_pas(entry))
    button1.pack(pady=10, padx=100)
    button1 = tk.Button(root1, text="USE GENERATED PASSWORD",bg="antiquewhite",fg="black",font=("HELVETICA",13,"bold"),activebackground="rosybrown",width=25, command=lambda: display_passwords(entry))
    button1.pack(pady=10, padx=100)
    img2= Image.open('Disable.png')
    image2 = ImageTk.PhotoImage(img2)
    image_label2 = tk.Label(root1, image=image2)
    image_label2.pack(pady=10,padx=100)
    button3 = tk.Button(root1, text="DISABLE THE CAMERA",bg="antiquewhite",fg="black",font=("HELVETICA",13,"bold"),activebackground="rosybrown",width=25,command=lambda: che_dis(entry))
    button3.pack(pady=10, padx=100)
    success_label = tk.Label(root1,bg="#6E4040") 
    success_label.pack()  
    root1.mainloop()

def che_ena(entry):
    input_password = entry.get()
    with open("password.txt", "r") as file:
        saved_passwords = file.readlines()
    if input_password in saved_passwords:
        del_cmd = r'reg delete "HKLM\SOFTWARE\Microsoft\Windows\CurrentVersion\CapabilityAccessManager\ConsentStore\webcam" /v Value /f'
        subprocess.run(del_cmd,shell=True)
        success_label.config(text="Camera Enabled",bg="white",fg="green")
    else:
        success_label.config(text="Password is incorrect",bg="white",fg="red")      
    
def ena_click():
    global success_label  
    root2 = tk.Toplevel()
    root2.title("ENABLE")
    root2.geometry("550x550")
    root2.configure(bg="#6E4040")
    img1= Image.open('logo.png')
    image1 = ImageTk.PhotoImage(img1)
    image_label1 = tk.Label(root2, image=image1)
    image_label1.pack(pady=10,padx=100)
    label = tk.Label(root2, text="Enter Text:",bg="antiquewhite",fg="black",font=("HELVETICA",13,"bold"),activebackground="rosybrown",width=20)
    label.pack(pady=10)
    entry = tk.Entry(root2,show='*',width=30)
    entry.pack(pady=10)
    button1 = tk.Button(root2, text="USE THE SAVED PASSWORD:",bg="antiquewhite",fg="black",font=("HELVETICA",13,"bold"),activebackground="rosybrown",width=25 ,command=lambda: display_passwords(entry))
    button1.pack(pady=10, padx=100)
    img2= Image.open('enable.png')
    image2 = ImageTk.PhotoImage(img2)
    image_label2 = tk.Label(root2, image=image2)
    image_label2.pack(pady=10,padx=100)
    button2 = tk.Button(root2, text="ENABLE THE CAMERA",bg="antiquewhite",fg="black",font=("HELVETICA",13,"bold"),activebackground="rosybrown",width=25,command=lambda: che_ena(entry))
    button2.pack(pady=10, padx=100)      
    success_label = tk.Label(root2,bg="#6E4040")  # Initialize success_label
    success_label.pack()  # Pack the success_label 
    root2.mainloop()

root = tk.Tk()
root.title("Web cam security")
root.geometry("550x550")
root.configure(bg="#6E4040")
img1= Image.open('logo.png')
image1 = ImageTk.PhotoImage(img1)
image_label1 = tk.Label(root, image=image1)
image_label1.pack(pady=10,padx=100)
button3 = tk.Button(root, text="Developers Info",bg="antiquewhite",fg="black",font=("HELVETICA",13,"bold"),activebackground="rosybrown",width=20,command=projectinfo)
button3.pack(pady=10, padx=100)
img2= Image.open('cam.png')
image2 = ImageTk.PhotoImage(img2)
image_label2 = tk.Label(root, image=image2)
image_label2.pack(pady=10,padx=100)
button1 = tk.Button(root, text="Disable Camera",bg="antiquewhite",fg="black",font=("HELVETICA",13,"bold"),activebackground="rosybrown",width=20 ,command=dis_click)
button1.pack(pady=10, padx=100)
button2 = tk.Button(root, text="Enable Camera",bg="antiquewhite",fg="black",font=("HELVETICA",13,"bold"),activebackground="rosybrown",width=20 ,command=ena_click)
button2.pack(pady=10, padx=100)   
root.mainloop()

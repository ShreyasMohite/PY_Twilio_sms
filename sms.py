from tkinter import *
from tkinter.ttk import Combobox
import tkinter.messagebox
from twilio.rest import Client
import threading

class Twillo:
    def __init__(self,root):
        self.root=root
        self.root.title("Twilio Send SMS To Mobile")
        self.root.geometry("500x400")
        self.root.iconbitmap("logo357.ico")
        self.root.resizable(0,0)


        send_by=StringVar()
    
    #=============================================================#
        def on_enter1(e):
            but_clear['background']="black"
            but_clear['foreground']="cyan"
  
        def on_leave1(e):
            but_clear['background']="SystemButtonFace"
            but_clear['foreground']="SystemButtonText"

        def on_enter2(e):
            but_push_notification['background']="black"
            but_push_notification['foreground']="cyan"
  
        def on_leave2(e):
            but_push_notification['background']="SystemButtonFace"
            but_push_notification['foreground']="SystemButtonText"

    #================================================================#
        def Clear():
            txt.delete("1.0","end")
            lab_message_sent.config(text="Enter Message")




        def send_messages():
            try:
                account_sid = 'account_sid'  #your twilio accout id
                auth_token = 'auth_token'    #your twilio access token
                client = Client(account_sid, auth_token)
                message = client.messages.create(
                            body=txt.get("1.0","end"),
                            from_='from',     #from number get twilio                                          
                            to='to'           #your authorised number
                        ) 
                a=message.sid
                if a:
                    lab_message_sent.config(text="Message sent succesfully")
            except Exception as e:
                tkinter.messagebox.showerror("Error",e)
                tkinter.messagebox.showerror("Error","Network Error")

        
        def thread_message():
            t1=threading.Thread(target=send_messages)
            t1.start()

               


#============================frame===================================================#
        mainframe=Frame(self.root,width=500,height=500,relief="ridge",bd=3)
        mainframe.place(x=0,y=0)

        firstframe=Frame(mainframe,width=494,height=300,relief="ridge",bd=3,bg="#023047")
        firstframe.place(x=0,y=0)

        secondframe=Frame(mainframe,width=494,height=95,relief="ridge",bd=3,bg="#6d6875")
        secondframe.place(x=0,y=300)

#===================================================================================#
        
        but_clear=Button(secondframe,width=20,height=2,text="Clear",cursor="hand2",font=('times new roman',12,'bold'),command=Clear)
        but_clear.place(x=30,y=20)
        but_clear.bind("<Enter>",on_enter1)
        but_clear.bind("<Leave>",on_leave1)

        but_push_notification=Button(secondframe,width=20,height=2,text="Send",cursor="hand2",font=('times new roman',12,'bold'),command=thread_message)
        but_push_notification.place(x=270,y=20)
        but_push_notification.bind("<Enter>",on_enter2)
        but_push_notification.bind("<Leave>",on_leave2)

#===================================================================================#
        
        lab_message=Label(firstframe,text="Enter Message",font=('times new roman',12),bg="#023047",fg="white")
        lab_message.place(x=200,y=10)


        txt=Text(firstframe,width=55,height=8,font=('times new roman',12))
        txt.place(x=20,y=50)

        lab_message_sent=Label(firstframe,text="Enter Message",font=('times new roman',12),bg="#023047",fg="white")
        lab_message_sent.place(x=200,y=240)


#====================================================================================#



if __name__ == "__main__":
    root=Tk()
    app=Twillo(root)
    root.mainloop()

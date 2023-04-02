import customtkinter
import tkinter
import validators
from youtube_transcript_api import YouTubeTranscriptApi

global url, Link, searchUrl, transcript_text


class Frame(customtkinter.CTkFrame):
    def __init__(self, master, **kwargs):
        super().__init__(master, **kwargs)




class Application(customtkinter.CTk):
    def summarize(self):
        global transcript_text
        if searchUrl > -1:
            unique_id = url.split("=")[-1]
            transcript_list = YouTubeTranscriptApi.get_transcript(unique_id)
            transcript_text = ''.join([t['text'] for t in transcript_list])
            for transcript in transcript_list:
                print(transcript['text'])
        else:
            print("Error")

    def onclicksubmit(self):
        global url, searchUrl
        url = self.entry.get()
        validation = validators.url(url)
        if validation:
            self.lable3.configure(text="Link Entered=" + url, text_color="White")
            global Link
            Link = True
        else:
            self.lable3.configure(text="Invalid Input", text_color="Red")
            Link = False
        if Link:
            searchUrl = url.find("youtube.com")
        else:
            print("Error")

    def __init__(self):
        super().__init__()
        self.geometry("640x480")
        self.title("SnippetVision")
        self.minsize(width=640, height=480)
        self.maxsize(width=640, height=480)
        self.grid_rowconfigure(0, weight=1)
        self.grid_columnconfigure(0, weight=1)
        self.my_frame = Frame(master=self, )
        self.my_frame.grid(row=0, column=0, padx=20, pady=20, sticky="nsew")
        self.summary = customtkinter.CTkButton(master=self,
                                               width=120,
                                               height=32,
                                               border_width=0,
                                               corner_radius=8,
                                               text="Summarize",
                                               command=self.summarize
                                               )

        self.summary.place(relx=0.50, rely=0.75, anchor=tkinter.CENTER)
        textvar1 = tkinter.StringVar(value="Snippet Vision")
        self.lable2 = customtkinter.CTkLabel(master=self,
                                             textvariable=textvar1,
                                             width=120,
                                             height=25,
                                             fg_color="white",
                                             text_color="Black",
                                             font=("", 30),
                                             corner_radius=8)
        self.lable2.place(relx=0.50, rely=0.15, anchor=tkinter.CENTER)
        self.entry = customtkinter.CTkEntry(master=self, placeholder_text="Enter the URL", width=240, height=25,
                                            border_width=2, corner_radius=10)
        self.entry.place(relx=0.50, rely=0.40, anchor=tkinter.CENTER)
        self.Submit = customtkinter.CTkButton(master=self,
                                              width=110,
                                              height=28,
                                              border_width=0,
                                              corner_radius=8,
                                              text="Submit",
                                              command=self.onclicksubmit
                                              )

        self.Submit.place(relx=0.50, rely=0.47, anchor=tkinter.CENTER)

        self.lable3 = customtkinter.CTkLabel(master=self,
                                             text="",
                                             width=120,
                                             height=25,
                                             text_color="RED",
                                             font=("", 16),
                                             corner_radius=0)
        self.lable3.place(relx=0.50, rely=0.55, anchor=tkinter.CENTER)


application = Application()

application.mainloop()

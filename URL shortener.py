import pyperclip
import pyshorteners
from tkinter import *

s_url = Tk()
s_url.geometry("500x500")
s_url.title("URL Shortener")
s_url.config(bg="#000000")
url = StringVar()
url_address = StringVar()


def urlshortener():
    urladdress = url.get()
    url_short = pyshorteners.Shortener().tinyurl.short(urladdress)
    url_address.set(url_short)


def copyurl():
    url_short = url_address.get()
    pyperclip.copy(url_short)




heading = Label(s_url, text="URL Shortener", font=(
    "Cooper Black", 20, "bold"))
heading.place(x=85, y=45, height=50, width=330)

url_enty = Entry(s_url, textvariable=url)
url_enty.place(x=85, y=135, height=50, width=330)

button_generate = Button(s_url, text="Generate Short URL", font=(
    "Cooper Black", 18, "bold"), command=urlshortener)
button_generate.place(x=85, y=200, height=50, width=330)

display_url = Entry(s_url, textvariable=url_address)
display_url.place(x=85, y=290, height=50, width=330)

button_copy = Button(s_url, text="Copy URL", font=("Cooper Black",
                                                 16, "bold"), command=copyurl)
button_copy.place(x=85, y=355, height=50, width=330)

s_url.mainloop()
import requests as r
from tkinter import messagebox as m
import tkinter as tk
import os

TK_SILENCE_DEPRECATION=1

# url = 'https://pine64.com/product/pinecil-smart-mini-portable-soldering-iron/?v=0446c16e2e66'
url = 'https://pine64.com/product/14"-pinebook-pro-linux-laptop-ansi-us-keyboard/?v=0446c16e2e66'

#don't show a main window
root = tk.Tk()
root.withdraw()

response = r.get(url)

source = response.text

startIndex = source.find("<title>")
endIndex = source.find("</title>")

if (startIndex == -1) or (endIndex == -1):
    m.showerror(title="could not check pine64.com", message="please check your internet connection")
    quit()

if("[Out of Stock]" in source[startIndex:endIndex]):
    print(source[startIndex:endIndex])
    m.showinfo(title="OUT OF STOCK", message="the Pinebook is still out of stock, unfortunately")
else:
    choice = m.askquestion(title="IN STOCK", message="THE PINEBOOK IS BACK\nGo to the store?")
    if choice == 'yes':
        os.system("firefox "+url)

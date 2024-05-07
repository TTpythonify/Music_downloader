from tkinter import *
import tkinter as tk
from songs import *
from tkinter import messagebox

class MusicDownloader(tk.Tk):
    def __init__(self):
        super().__init__()
        self.geometry("500x500")
        self.configure(bg='ghost white')
        self.title("Music Downloader")

        Label(self, text="Music Downloader", font="Arial 20 bold", bg='white smoke').pack()
        Label(text="Pythonify", font='Arial 15 bold', bg='white smoke', width='20').pack(side='bottom')

        self.query_var = StringVar()
        Label(self, text="Search Music", font='Arial 15 bold', bg='white smoke').place(x=20, y=60)
        self.entry_field = Entry(self, textvariable=self.query_var, width='30',font='Arial 15 bold')
        self.entry_field.place(x=20, y=100)

        self.search_button = Button(self, text="Download", font='Arial 15 bold', bg='light grey', command=self.download_music)
        self.search_button.place(x=350, y=100)

        # Display Listbox
        self.display_listbox = Listbox(self, height=10, width=30, font='Arial 15 bold', bg='light grey')
        self.display_listbox.place(x=20, y=140)

        self.exit_button = Button(self, text="Exit", font='Arial 15 bold', bg='red', command=self.exit_window)
        self.exit_button.place(x=50, y=400)

        self.downloaded_button = Button(self, text="Downloaded", font='Arial 15 bold', bg='light grey', command=self.downloaded_music)
        self.downloaded_button.place(x=200, y=400)

    def download_music(self):
        query = self.entry_field.get()
        self.display_listbox.delete(0, END)
        self.display_listbox.insert(END, f"Downloading {query.upper()}")

        if search_song(query):
            messagebox.showinfo("Message", "Song has been downloaded successfully")
        else:
            messagebox.showerror("Error", "An error occurred. Please try again.")
      

    def exit_window(self):
        self.destroy()


    def downloaded_music(self):
        self.display_listbox.delete(0, END)
        # Imports the function from songs
        my_songs=list_downloaded_songs()
        for i in my_songs:
            self.display_listbox.insert(END, i)
            
            

def main():
    window = MusicDownloader()
    window.mainloop()

if __name__ == "__main__":
    main()

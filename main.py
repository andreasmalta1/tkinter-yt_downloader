import tkinter
import customtkinter
from pytube import YouTube


def start_download():
    try:
        yt_link = link.get()
        yt_object = YouTube(yt_link, on_progress_callback=on_progress)
        yt_video = yt_object.streams.get_highest_resolution()
        title.configure(text=yt_object.title, text_color="white")
        finish_label.configure(text="")
        yt_video.download()
    except Exception as e:
        print(e)
        finish_label.configure(text="Download Error", text_color="red")
    else:
        finish_label.configure(text="Downloaded!", text_color="green")


def on_progress(stream, chunk, bytes_remaining):
    total_size = stream.filesize
    bytes_downloaded = total_size - bytes_remaining
    pct_complete = bytes_downloaded / total_size * 100
    pct_complete = str(int(pct_complete))
    progress_pct.configure(text=pct_complete + "%")
    progress_pct.update()

    progress_bar.set(float(pct_complete) / 100)


customtkinter.set_appearance_mode("System")
customtkinter.set_default_color_theme("blue")

app = customtkinter.CTk()
app.geometry("720x480")
app.title("YouTube Downloader")

title = customtkinter.CTkLabel(app, text="Insert a YouTube Link")
title.pack(padx=10, pady=10)

url = tkinter.StringVar()
link = customtkinter.CTkEntry(app, width=350, height=40, textvariable=url)
link.pack()

finish_label = customtkinter.CTkLabel(app, text="")
finish_label.pack()

progress_pct = customtkinter.CTkLabel(app, text="0%")
progress_pct.pack()

progress_bar = customtkinter.CTkProgressBar(app, width=400)
progress_bar.set(0)
progress_bar.pack(padx=10, pady=10)

down_btn = customtkinter.CTkButton(app, text="Download", command=start_download)
down_btn.pack(padx=10, pady=10)

app.mainloop()

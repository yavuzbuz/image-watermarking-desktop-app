from tkinter import *
from PIL import ImageTk, Image, ImageDraw, ImageFont

tk = Tk()

tk.title("Image Watermarking")
tk.geometry("800x100")


def button():
    top = Toplevel(tk)
    top.geometry("800x550")
    top.title("Image Watermarking")

    Label(top, text="Image name:", font="Verdana 12 bold", bg="red", fg="white").pack()
    entry = Entry(top, width=25)
    entry.pack()

    def close_popup():
        text_entry = entry.get()
        # top.destroy()

        canvas = Canvas(top, width=680, height=800)
        canvas.pack()
        image = Image.open(f"/Users/yavuzbuz/Desktop/images/{text_entry}").convert("RGBA").resize((700, 400))

        txt = Image.new('RGBA', image.size, (255, 255, 255, 0))

        image_width, image_height = image.size
        font_size = int(image_width / 8)
        font = ImageFont.truetype("Georgia.ttf", font_size)

        d = ImageDraw.Draw(txt)
        d.text((0, 0), "bahilix", fill=(0, 0, 0, 100), font=font)

        combined = Image.alpha_composite(image, txt)

        new_image = ImageTk.PhotoImage(combined)
        canvas.create_image(10, 10, anchor=NW, image=new_image)
        canvas.theimage = new_image

        combined.save(f"/Users/yavuzbuz/Desktop/watermarked_images/watermarked_{text_entry}")

    btn2 = Button(top,
                  text="Confirm",
                  command=close_popup)
    btn2.pack()


lbl = Label(tk, text="Upload an image, so i can watermark it for you", font="Verdana 12 bold", bg="red", fg="white")
lbl.pack()


btn = Button(tk,
             text="Upload Image",
             padx=20, pady=20,
             command=button,)
btn.pack()


tk.mainloop()


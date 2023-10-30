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
        image = Image.open(f"/Users/yavuzbuz/Desktop/images/{text_entry}")
        resized_image = image.resize((700, 400))

        image_width, image_height = resized_image.size
        draw = ImageDraw.Draw(resized_image)

        font_size = int(image_width / 8)
        font = ImageFont.truetype("Arial.ttf", font_size)

        x, y = int(image_width / 2), int(image_height / 2)

        draw.text((x, y), "bahilix", font=font, fill="#FFF", stroke_width=5, stroke_fill="#222", anchor="ms")

        new_image = ImageTk.PhotoImage(resized_image)
        canvas.create_image(10, 10, anchor=NW, image=new_image)
        canvas.theimage = new_image

        resized_image.save(f"/Users/yavuzbuz/Desktop/watermarked_images/watermarked_{text_entry}")

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


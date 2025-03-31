# IMPORTANT!!!: Run 'CreateMNISTModel.py before running this, or it will not work.'


import numpy as np
import tkinter as tk
from PIL import Image, ImageDraw
import tensorflow as tf

model = tf.keras.models.load_model('mnist_model.h5')

window = tk.Tk()
window.title("Draw a Digit")

canvas_width, canvas_height = 280, 280
canvas = tk.Canvas(window, width=canvas_width, height=canvas_height, bg="black")
canvas.pack()

image = Image.new("L", (canvas_width, canvas_height), 0)
draw = ImageDraw.Draw(image)

def paint(event):
    x, y = event.x, event.y
    radius = 10
    canvas.create_oval(x-radius, y-radius, x+radius, y+radius, fill="white", outline="white")
    draw.ellipse([x-radius, y-radius, x+radius, y+radius], fill="white")

def clear_canvas():
    canvas.delete("all")
    draw.rectangle((0, 0, canvas_width, canvas_height), fill="black")

def predict_digit():
    img = image.resize((28, 28))
    img = np.array(img) / 255.0
    img = img.reshape(1, 28, 28, 1)
    prediction = model.predict(img)
    digit = np.argmax(prediction)
    result_label.config(text=f"Prediction: {digit}")

canvas.bind("<B1-Motion>", paint)

button_frame = tk.Frame(window)
button_frame.pack()
tk.Button(button_frame, text="Clear", command=clear_canvas).pack(side=tk.LEFT)
tk.Button(button_frame, text="Predict", command=predict_digit).pack(side=tk.RIGHT)

result_label = tk.Label(window, text="Draw a digit!", font=("Arial", 14))
result_label.pack()

window.mainloop()

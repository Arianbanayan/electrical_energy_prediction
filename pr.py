import sys
import os
import tensorflow as tf
import numpy as np
from tkinter import *
from tkinter import ttk
from tkinter import messagebox

def get_resource_path(relative_path):
    """Get the absolute path to the resource, works for dev and for PyInstaller."""
    try:
        # PyInstaller creates a temp folder and stores path in _MEIPASS
        base_path = sys._MEIPASS
    except Exception:
        base_path = os.path.abspath(".")
    return os.path.join(base_path, relative_path)

model_path = get_resource_path('my_model.keras')
model = tf.keras.models.load_model(model_path)

def predict():
    try:
        # Retrieve input values
        inputs = [float(entry.get()) for entry in entries]
        # Make prediction
        prediction = model.predict([np.array(inputs).reshape(1, -1)])[0][0]
        # Display the prediction
        result_var.set(f'Prediction: {prediction:.2f}')
    except ValueError:
        messagebox.showerror('Input error', 'Please enter valid numbers')

# Initialize the GUI application
root = Tk()
root.title("ANN Model Prediction")

# Initialize StringVar to display the prediction result
result_var = StringVar()

# Define the layout of the GUI
frame = ttk.Frame(root, padding="10 10 10 10")
frame.grid(column=0, row=0, sticky=(N, W, E, S))

# Define labels for input fields
labels_text = ['Ambient Temperature (AT):', 'Vacuum (V):', 'Ambient Pressure (AP):', 'Relative Humidity (RH):']
entries = []

# Create input fields
for i, text in enumerate(labels_text):
    ttk.Label(frame, text=text).grid(column=0, row=i, sticky=W)
    entry = ttk.Entry(frame)
    entry.grid(column=1, row=i, sticky=(W, E))
    entries.append(entry)

# Configure the column within the frame to expand and fill space
frame.columnconfigure(1, weight=1)

# Add a button to trigger prediction
predict_button = ttk.Button(frame, text="Predict", command=predict)
predict_button.grid(column=1, row=len(labels_text), sticky=E)

# Add a label to display prediction results
result_label = ttk.Label(frame, textvariable=result_var)
result_label.grid(column=0, row=len(labels_text)+1, columnspan=2, sticky=(W, E))

# Start the GUI application
root.mainloop()

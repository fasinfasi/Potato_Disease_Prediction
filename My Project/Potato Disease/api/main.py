from fastapi import FastAPI, File, UploadFile
from fastapi.middleware.cors import CORSMiddleware
import uvicorn
import numpy as np
from io import BytesIO
from PIL import Image
import tensorflow as tf

app = FastAPI()

# Defining allowed origins for CORS
origins = [
    "http://localhost",
    "http://localhost:3000",
]
# Adding CORS middleware to the app
app.add_middleware(
    CORSMiddleware,
    allow_origins=origins, # List of allowed origins
    allow_credentials=True, # Allow cookies and authentication headers
    allow_methods=["*"], # Allow all HTTP methods (GET, POST, etc.)
    allow_headers=["*"], # Allow all HTTP headers
)

MODEL = tf.keras.models.load_model("../models/version_1")

CLASS_NAMES = ["Early Blight", "Late Blight", "Healthy"]

@app.get("/ping")
async def ping():
    return "Hey i am here : )"

def read_file_as_image(data) -> np.ndarray:
    image = np.array(Image.open(BytesIO(data))) # Readed image is bytes fromat that convert into a NumPy array
    return image

@app.post("/predict")
async def predict(
    file: UploadFile = File(...)
):
    image = read_file_as_image(await file.read()) # image shape to be  (height, width, channels)
    img_batch = np.expand_dims(image, 0) # It make batch_size in image shape (batch_size, height, width, channels)
    
    predictions = MODEL.predict(img_batch)

    predicted_class = CLASS_NAMES[np.argmax(predictions[0])]
    confidence = np.max(predictions[0])
    return {
        'class': predicted_class,
        'confidence': float(confidence)
    }

if __name__ == "__main__":
    uvicorn.run(app, host='localhost', port=8000)
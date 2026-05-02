import os
import fitz  # PyMuPDF
import base64
from openai import OpenAI
from dotenv import load_dotenv

from ..db.db import files_table

from ..utils.constants import STATUS

load_dotenv(dotenv_path=".env")

GROQ_API_KEY = os.getenv("GROQ_API_KEY")

client = OpenAI(
    api_key=GROQ_API_KEY,
    base_url="https://api.groq.com/openai/v1"
)

def encode_image(image_path: str):
  with open(image_path, "rb") as image_file:
    return base64.b64encode(image_file.read()).decode("utf-8")

def process_file(id: str, file_path: str):
  files_table.update(
    {"status": STATUS["PROCESSING"]},
    doc_ids=[id]
  )
  
  
  # Convert pdf file to image
  
  files_table.update(
    {"status": STATUS["CONVERTING_TO_IMAGES"]},
    doc_ids=[id]
  )
  
  images = []
  
  doc = fitz.open(file_path)
  
  for i, page in enumerate(doc):
    # Render page to an image (pixmap)
    
    image_path = f"./mnt/uploads/images/{id}/image-{i}.png"
    
    os.makedirs(os.path.dirname(image_path), exist_ok=True)
    
    pix = page.get_pixmap(dpi=300) 
    pix.save(image_path)
    images.append(image_path)
    
  doc.close()
  
  files_table.update(
    {"status": STATUS["CONVERTING_TO_IMAGES_SUCCESS"]},
    doc_ids=[id]
  )
  
  images_base64 = [encode_image(img) for img in images]
  
  response = client.chat.completions.create(
    model="meta-llama/llama-4-scout-17b-16e-instruct",  # vision-capable model
    messages=[
        {
            "role": "user",
            "content": [
                {"type": "text", "text": "Based on the resume below. Please roast the resume. If you find the image is not of the resume then ignore it and just let the user know that the file is not resume."},
                {
                    "type": "image_url",
                    "image_url": {
                        "url": f"data:image/jpeg;base64,{images_base64[0]}"
                    },
                },
            ],
        }
    ],
    max_tokens=500,
  )
  
  ai_result = response.choices[0].message.content
  
  files_table.update(
    {"status": STATUS["PROCESSED"], "result": ai_result },
    doc_ids=[id]
  )
    
    
  
  
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

def process_file(id: str, file_path: str, job_description: str):
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
    
    image_path = f"./mnt/uploads/images/{id}/image-{i}.jpg"
    
    os.makedirs(os.path.dirname(image_path), exist_ok=True)
    
    pix = page.get_pixmap(dpi=200) 
    pix.save(image_path)
    images.append(image_path)
    
  doc.close()
  
  files_table.update(
    {"status": STATUS["CONVERTING_TO_IMAGES_SUCCESS"]},
    doc_ids=[id]
  )
  
  images_base64 = [encode_image(img) for img in images]
  
  SYSTEM_PROMPT = f"""
        You are an expert resume reviewer and career coach.

        Your goal is to provide highly actionable, honest, and job-specific feedback that will significantly improve the candidate’s chances of getting shortlisted. 

        Task:
        1. Analyze the provided resume images (they may contain multiple pages).
        2. Compare them with the following job description.
        3. Identify alignment, gaps, and missed opportunities.
        4. If the images are not a resume, clearly state that and stop.

        Job Description: {job_description}
        
        Output format (strictly follow):
        
        ### Strengths
        - Bullet points of what matches well with the job description
        
        ### Weaknesses / Gaps
        - Missing skills, unclear experience, or mismatches with the job
        
        ### Improvements (High Impact)
        - Specific changes the user should make immediately
        - Rewrite suggestions where applicable (e.g., better bullet points)
        
        ### Optimization Tips (ATS + Recruiter Friendly)
        - Keywords to add
        - Formatting fixes
        - Section-level improvements
        
        ### Match Score
        - Provide a percentage (0–100%)
        - Brief justification (2–3 lines max)
        
        Rules:
        - Be specific and reference actual resume content
        - Avoid generic advice like “improve formatting” without explaining how
        - Prefer concrete examples over abstract suggestions
        - Focus on what will materially improve shortlist chances
        - For at least 2 improvement points, rewrite the candidate’s resume bullet into a stronger, quantifiable version.
      """
  
  content = [
    {
      "type": "text",
      "text": SYSTEM_PROMPT
    }
  ]
  
  # Add all images
  
  for img_b64 in images_base64:
    content.append({
      "type": "image_url",
      "image_url": {
        "url": f"data:image/jpeg;base64,{img_b64}"
      },
    })
  
  response = client.chat.completions.create(
    model="meta-llama/llama-4-scout-17b-16e-instruct",  # vision-capable model
    messages=[
        {
            "role": "user",
            "content": content
        }
    ],
    max_tokens=800,
  )
  
  ai_result = response.choices[0].message.content
  
  files_table.update(
    {"status": STATUS["PROCESSED"], "result": ai_result, "job_description": job_description },
    doc_ids=[id]
  )
    
    
  
  
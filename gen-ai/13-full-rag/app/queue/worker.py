import os
import fitz  # PyMuPDF

from ..db.db import files_table

from ..utils.constants import STATUS

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
  
  doc = fitz.open(file_path)
  
  for i, page in enumerate(doc):
    # Render page to an image (pixmap)
    
    image_path = f"./mnt/uploads/images/{id}/image-{i}.png"
    
    os.makedirs(os.path.dirname(image_path), exist_ok=True)
    
    pix = page.get_pixmap(dpi=300) 
    pix.save(image_path)
    
  doc.close()
  
  files_table.update(
    {"status": STATUS["CONVERTING_TO_IMAGES_SUCCESS"]},
    doc_ids=[id]
  )
    
    
  
  
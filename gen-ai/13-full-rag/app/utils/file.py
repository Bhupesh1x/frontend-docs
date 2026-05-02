import os
import shutil
import aiofiles

async def save_to_desk(file: bytes, path: str) -> bool:
  os.makedirs(os.path.dirname(path), exist_ok=True)
  
  async with aiofiles.open(path, "wb") as out_file:
    await out_file.write(file)
    
  return True  


def clean_up_files(folder_path: str):
  if os.path.exists(folder_path):
    shutil.rmtree(folder_path, ignore_errors=True)
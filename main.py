from fastapi import FastAPI, UploadFile, File
from pydantic import BaseModel
import whisper
import numpy as np
import os



model = whisper.load_model("base")
app = FastAPI()

# class AudioData(BaseModel):
#     audio_file: UploadFile | None = File(...)

@app.post("/process_audio")
async def process_audio(file: UploadFile):
    """
    Receives an uploaded audio file and returns a simulated processing result.
    """
    # try:
    audio_content = await file.read()
    with open('temp.mp3', 'wb') as f:
        f.write(audio_content)

    # with open(f'uploaded_files/{file.audio_file}', 'wb') as buffer:
        # shutil.copyfileobj(file.audio_file, buffer)
    # Simulate processing the audio content (replace with your actual logic)
    result = model.transcribe('temp.mp3')
    os.remove('temp.mp3')
    # print("processed", audio_content.__str__)
    return {"processed_file": result}
    # return {"processed_file": result}
    # except:
        # return {"error": "No audio file uploaded"}


@app.get("/process_audio")
async def process_audio():
    """
    Receives an uploaded audio file and returns a simulated processing result.
    """
    return {"error": "you should use post method!"}

if __name__ == "__main__":
    import uvicorn
    uvicorn.run("main:app", host="0.0.0.0", port=8000)
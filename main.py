from fastapi import FastAPI, UploadFile, File
from pydantic import BaseModel
import whisper

model = whisper.load_model("base")


app = FastAPI()

class AudioData(BaseModel):
    audio_file: UploadFile | None = File(...)

@app.post("/process_audio")
async def process_audio(data: AudioData):
    """
    Receives an uploaded audio file and returns a simulated processing result.
    """
    if data.audio_file:
        audio_content = await data.audio_file.read()
        # Simulate processing the audio content (replace with your actual logic)
        result = model.transcribe(audio_content)
        print("processed")
        return {"processed_data": result}
    else:
        return {"error": "No audio file uploaded"}

if __name__ == "__main__":
    import uvicorn
    uvicorn.run("main:app", host="0.0.0.0", port=8000)
from fastapi import FastAPI, FileResponse, Response
from pathlib import Path

print("pechpeching...")


app = FastAPI()

# Specify the path to your HTML file
html_filepath = Path("./index.html")

@app.get("/")
async def root():
    return FileResponse(html_filepath, media_type="text/html")

# Optional: Additional routes serving other static files
@app.get("/static/{filename:path}")
async def static_files(filename: str):
    static_dir = Path("path/to/your/static/files")
    file_path = static_dir / filename
    if file_path.is_file():
        return FileResponse(file_path)
    else:
        return Response(status_code=404, content="File not found")
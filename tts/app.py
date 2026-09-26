from fastapi import FastAPI, Header, HTTPException
from fastapi.responses import FileResponse
from pydantic import BaseModel
import os
import subprocess
import uuid

app = FastAPI()

API_KEY = os.environ.get("TTS_API_KEY", "")
MODEL = "/app/models/ur_PK-aegis_female-medium.onnx"
CONFIG = "/app/models/ur_PK-aegis_female-medium.onnx.json"

class TTSRequest(BaseModel):
    text: str

@app.get("/")
def home():
    return {
        "status": "ok",
        "service": "Piper Urdu TTS",
        "voice": "ur-PK-aegis_female-medium"
    }

@app.post("/tts")
def generate_tts(request: TTSRequest, x_api_key: str = Header(default="")):
    if API_KEY and x_api_key != API_KEY:
        raise HTTPException(status_code=401, detail="Invalid API key")

    text = request.text.strip()
    if not text:
        raise HTTPException(status_code=400, detail="text is required")

    filename = f"/tmp/{uuid.uuid4()}.wav"

    try:
        subprocess.run(
            ["piper", "--model", MODEL, "--config", CONFIG, "--output_file", filename],
            input=text.encode("utf-8"),
            check=True,
            timeout=180
        )
    except subprocess.TimeoutExpired:
        raise HTTPException(status_code=504, detail="TTS generation timed out")
    except Exception as e:
        raise HTTPException(status_code=500, detail=str(e))

    if not os.path.exists(filename):
        raise HTTPException(status_code=500, detail="Audio generation failed")

    return FileResponse(filename, media_type="audio/wav", filename="urdu-tts.wav")

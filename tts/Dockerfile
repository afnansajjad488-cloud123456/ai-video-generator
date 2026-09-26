FROM python:3.11-slim

WORKDIR /app

RUN apt-get update && \
    apt-get install -y --no-install-recommends \
    espeak-ng \
    wget \
    ca-certificates && \
    rm -rf /var/lib/apt/lists/*

RUN pip install --no-cache-dir \
    fastapi \
    "uvicorn[standard]" \
    pydantic \
    piper-tts

RUN mkdir -p /app/models

RUN wget -O /app/models/ur_PK-aegis_female-medium.onnx \
    https://huggingface.co/mahwizzzz/piper-voice-ur-aegis-female/resolve/main/ur_PK-aegis_female-medium.onnx

RUN wget -O /app/models/ur_PK-aegis_female-medium.onnx.json \
    https://huggingface.co/mahwizzzz/piper-voice-ur-aegis-female/resolve/main/ur_PK-aegis_female-medium.onnx.json

COPY app.py /app/app.py

EXPOSE 10000

CMD ["sh", "-c", "uvicorn app:app --host 0.0.0.0 --port ${PORT:-10000}"]

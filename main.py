from fastapi import FastAPI, File, UploadFile
from fastapi.responses import StreamingResponse
from fastapi.middleware.cors import CORSMiddleware
from rembg import remove
from io import BytesIO

app = FastAPI()

# Habilita CORS para permitir acesso do frontend
app.add_middleware(
    CORSMiddleware,
    allow_origins=["*"],  # Pode restringir depois
    allow_credentials=True,
    allow_methods=["*"],
    allow_headers=["*"],
)

@app.post("/remover-fundo")
async def remover_fundo(file: UploadFile = File(...)):
    image_bytes = await file.read()
    output_bytes = remove(image_bytes)
    result_image = BytesIO(output_bytes)
    return StreamingResponse(result_image, media_type="image/png")

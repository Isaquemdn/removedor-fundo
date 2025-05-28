from fastapi import FastAPI, File, UploadFile
from fastapi.middleware.cors import CORSMiddleware
from fastapi.responses import StreamingResponse
from rembg import remove
from io import BytesIO

app = FastAPI()

# ✅ CORS CORRETAMENTE CONFIGURADO
app.add_middleware(
    CORSMiddleware,
    allow_origins=["http://localhost:8080"],  # durante desenvolvimento, o * é aceitável
    allow_credentials=True,
    allow_methods=["*"],
    allow_headers=["*"],
)

@app.post("/remover-fundo")
async def remover_fundo(file: UploadFile = File(...)):
    input_data = await file.read()
    output_data = remove(input_data)
    return StreamingResponse(BytesIO(output_data), media_type="image/png")

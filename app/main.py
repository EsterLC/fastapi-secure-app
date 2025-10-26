from fastapi import FastAPI
from fastapi.middleware.cors import CORSMiddleware
from app.middlewares.security_headers import SecurityHeadersMiddleware
from app.middlewares.request_id import RequestIDMiddleware
from app.routers import admin

app = FastAPI(docs_url="/docs", redoc_url="/redoc")

ALLOWED_ORIGINS = []  # agrega tu frontend si lo tienes
app.add_middleware(
    CORSMiddleware,
    allow_origins=ALLOWED_ORIGINS,
    allow_credentials=True,
    allow_methods=["GET","POST","PUT","DELETE"],
    allow_headers=["Authorization","Content-Type"],
)
app.add_middleware(SecurityHeadersMiddleware)
app.add_middleware(RequestIDMiddleware)

@app.get("/health")
def health():
    return {"status": "ok"}

app.include_router(admin.router)

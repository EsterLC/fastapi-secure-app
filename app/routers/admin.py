from fastapi import APIRouter, Depends
from app.security.roles import require_role

router = APIRouter(prefix="/admin", tags=["admin"])

@router.get("/reports")
def get_reports(_: dict = Depends(require_role("admin"))):
    return {"ok": True}

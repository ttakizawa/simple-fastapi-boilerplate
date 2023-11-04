from fastapi import APIRouter

from api.sample.v1.sample import sample_router as sample_v1_router

router = APIRouter()
router.include_router(sample_v1_router, prefix="/api/v1/sample", tags=["Sample"])


__all__ = ["router"]

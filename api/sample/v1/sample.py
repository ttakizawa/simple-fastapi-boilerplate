from fastapi import APIRouter

from api.sample.v1.request.sample import SampleRequest
from api.sample.v1.response.sample import SampleResponse


sample_router = APIRouter()


@sample_router.post(
    "",
    response_model=SampleResponse,
)
def create_sample(request: SampleRequest):
    return {"message": request.message}


@sample_router.get(
    "",
    response_model=SampleResponse,
)
def get_sample():
    return {"message": "Hello World."}

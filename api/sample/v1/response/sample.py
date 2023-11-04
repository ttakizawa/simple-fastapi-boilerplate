from pydantic import BaseModel, Field


class SampleResponse(BaseModel):
    message: str = Field(..., description="message")

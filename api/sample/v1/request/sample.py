from pydantic import BaseModel, Field


class SampleRequest(BaseModel):
    message: str = Field(..., description="message")

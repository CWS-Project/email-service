from pydantic import BaseModel


class SendMailRequest(BaseModel):
    type: str
    data: dict
from pydantic import BaseModel


class RequestHeaders(BaseModel):
    """
    リクエストヘッダ
    """

    host: str
    user_agent: str

    class Config:
        allow_mutation = False

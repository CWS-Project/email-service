from fastapi import APIRouter, Response
from util import Mailer, CustomLogger
from dtypes import make_response, SendMailRequest
from service import MailService

router = APIRouter(prefix="/api/v1/mail", tags=["Mail"])\

mail_service = MailService(
    mailer=Mailer(),
    logger=CustomLogger("mail")
)

@router.post("/send")
async def send_mail(request: SendMailRequest, response: Response):
    mail_type = request.type
    data = request.data
    if mail_type is None or data is None:
        return make_response(
            response,
            status=400,
            message="Mail type and data are required"
        )
    success, data = mail_service.send_mail(mail_type, data)
    if not success:
        return make_response(
            response,
            status=500,
            message="Failed to send mail"
        )
    
    return make_response(
        response,
        status=201,
        message=data
    )
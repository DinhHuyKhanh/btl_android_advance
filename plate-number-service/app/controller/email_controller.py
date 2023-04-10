from fastapi import APIRouter
from fastapi_mail import FastMail, MessageSchema, MessageType
from util.helper import wrap_responses
from schemas import EmailSchema
from conf import EMAIL
from app.settings import mail_service
from app.settings import user_model

router = APIRouter(
    prefix='/email',
    tags=['email']
)

async def _send_email_async(email_to: str, otp):
    html = f"""<p>This is code to validate: {otp} </p> """

    message = MessageSchema(
        subject="Verification code forgot password",
        recipients=[email_to],
        body=html,
        subtype=MessageType.html)

    fm = FastMail(EMAIL)
    await fm.send_message(message)

@router.post('')
@wrap_responses
async def simple_send(emailInfo: EmailSchema):
    try:
        otp, _, _ = mail_service.create_code(emailInfo.email, user_model)
        await _send_email_async(emailInfo.email, otp)
        return otp, 0, "otp sent to mail"
    except Exception:
        return None, -1, "otp not sent to mail"
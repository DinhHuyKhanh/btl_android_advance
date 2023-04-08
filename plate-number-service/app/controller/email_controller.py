from fastapi import APIRouter
from fastapi_mail import FastMail, MessageSchema, MessageType
from schemas import EmailSchema
from conf import EMAIL
from app.settings import mail_service
from app.settings import user_model

router = APIRouter(
    prefix='/email',
    tags=['email']
)

async def _send_email_async(email_to: str):
    code = mail_service.create_code(email_to, user_model)
    html = f"""<p>This is code to validate: {code} </p> """

    message = MessageSchema(
        subject="Verification code forgot password",
        recipients=[email_to],
        body=html,
        subtype=MessageType.html)

    fm = FastMail(EMAIL)
    await fm.send_message(message)

@router.post('/')
async def simple_send(emailInfo: EmailSchema):
    try:
        await _send_email_async(emailInfo.email)
        return {"message": "email has been sent"}
    except Exception as ex:
        return {"message": str(ex)}
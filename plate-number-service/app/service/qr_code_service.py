from datetime import datetime
import io
import segno


class QrCodeService():
    def create_qrcode(self, id, model):
        user = model.get_by_id(id)

        if user:
            return self.__process_create_qrcode(user.Id)

        return None
        
    def __process_create_qrcode(self, user_id):
        data_qr = str(user_id) + ", " + datetime.now().strftime("%d/%m/%Y %H:%M:%S")
        img = segno.make_qr(data_qr, error='h', version=5)
        buf = io.BytesIO()
        img.save(buf, kind='png', scale=5)
        binary = buf.getvalue()

        return binary
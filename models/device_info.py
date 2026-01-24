from extensions import db
import datetime

class DeviceInfo(db.Model):
    __tablename__ = 'device_info'
    sn = db.Column(db.String(255), primary_key=True)
    imei = db.Column(db.String(255))
    stid = db.Column(db.String(255))
    status = db.Column(db.String(50), default='active')
    st_data = db.Column(db.Text) # Stores the extra ST keys as JSON or raw text
    updated_at = db.Column(db.DateTime, default=datetime.datetime.utcnow, onupdate=datetime.datetime.utcnow)

    def __repr__(self):
        return f"<DeviceInfo {self.sn}>"

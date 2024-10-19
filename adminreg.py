from models import Admin, db
from werkzeug.security import generate_password_hash

hashed_password = generate_password_hash('password123', method='sha256')
new_admin = Admin(username='admin', password_hash=hashed_password)
db.session.add(new_admin)
db.session.commit()

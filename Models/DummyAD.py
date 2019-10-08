from sqlalchemy import Column
from sqlalchemy.dialects.postgresql import INTEGER, TEXT, JSON
from Models.Model import Model

"""
    id integer NOT NULL DEFAULT nextval('requisition."Users_id_seq"'::regclass),
    email text COLLATE pg_catalog."default" NOT NULL,
    name text COLLATE pg_catalog."default" NOT NULL,
    surname text COLLATE pg_catalog."default" NOT NULL,
    department text COLLATE pg_catalog."default" NOT NULL,
    "position" text COLLATE pg_catalog."default" NOT NULL,
    CONSTRAINT "Users_pkey" PRIMARY KEY (id),
    CONSTRAINT "Users_email_key" UNIQUE (email)
"""


class Users(Model):
    __tablename__ = 'Users'
    __table_args__ = {'schema': 'requisition'}
    id = Column(INTEGER, primary_key=True, nullable=False, autoincrement=True)
    email = Column(TEXT, nullable=False)
    name = Column(TEXT, nullable=False)
    surname = Column(TEXT, nullable=False)
    department = Column(TEXT, nullable=False)
    position = Column(TEXT, nullable=False)

    def serialize(self):
        return {
            "id": self.id,
            "email": self.email,
            "name": self.name,
            "surname": self.surname,
            "department": self.department,
            "position": self.position
        }

from sqlalchemy import Column
from sqlalchemy.dialects.postgresql import INTEGER, TEXT, JSON
from Models.Model import Model

"""
    id integer NOT NULL DEFAULT nextval('requisition."Employees_id_seq"'::regclass),
    email text COLLATE pg_catalog."default" NOT NULL,
    roles json NOT NULL,
    CONSTRAINT "Employees_pkey" PRIMARY KEY (id),
    CONSTRAINT "Employees_email_key" UNIQUE (email)
"""


class Roles(Model):
    __tablename__ = 'Roles'
    __table_args__ = {'schema': 'requisition'}
    id = Column(INTEGER, primary_key=True, nullable=False, autoincrement=True)
    email = Column(TEXT, nullable=False)
    roles = Column(JSON, nullable=False)

    def serialize(self):
        return {
            "id": self.id,
            "email": self.email,
            "roles": self.roles
        }

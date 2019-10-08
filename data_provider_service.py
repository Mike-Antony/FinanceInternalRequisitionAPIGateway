from sqlalchemy import create_engine
from sqlalchemy.orm import sessionmaker
from sqlalchemy.exc import IntegrityError as DuplicateKey
from Models.InitDB import init_database
from Models.Roles import Roles
from Models.DummyAD import Users


class DataProviderService:
    def __init__(self, engine):
        """
        :param engine: The engine route and login details
        :return: a new instance of DAL class
        :type engine: string
        """
        if not engine:
            raise ValueError('The values specified in engine parameter has to be supported by SQLAlchemy')
        self.engine = engine
        db_engine = create_engine(engine)
        db_session = sessionmaker(bind=db_engine)
        self.session = db_session()

    def init_database(self):
        """
        Initializes the database tables and relationships
        :return: None
        """
        init_database(self.engine)

    # User Role Methods
    def get_roles(self, email=None, serialize=False):
        """
        If the email parameter is  defined then it looks up the role with the given email address,
        otherwise it loads all the roles
        """

        if email is None:
            all_roles = self.session.query(Roles).all()
        else:
            all_roles = self.session.query(Roles).filter(Roles.email == email).all()

        if serialize:
            return [role.serialize() for role in all_roles]
        else:
            return all_roles

    def add_role(self, email, is_hod=0, is_finance_admin=0, is_system_admin=0):
        """
        Creates and saves a new role to the database
        {
            "employee": 1,
            "finance admin": is_finance_admin,
            "hod": is_hod,
            "system admin": is_system_admin
        }
        """
        roles = {
            "employee": 1,
            "finance admin": is_finance_admin,
            "hod": is_hod,
            "system admin": is_system_admin
        }
        new_role = Roles(email=email, roles=roles)
        self.session.add(new_role)
        try:
            self.session.commit()
            return new_role.id
        except DuplicateKey:
            self.session.rollback()

    def update_role(self, email, edited_roles):
        updated_roles = None
        users_roles = self.get_roles(email)
        users_role = users_roles[0]
        if users_role:
            users_role.roles = edited_roles
            self.session.add(users_role)
            self.session.commit()
            updated_roles = self.get_roles(email)[0]
        return updated_roles.serialize()

    # User Detail Methods
    def get_user_details(self, email=None, serialize=False):
        """
        If the email parameter is  defined then it looks up the role with the given email address,
        otherwise it loads all the users
        """

        if email is None:
            all_users = self.session.query(Users).all()
        else:
            all_users = self.session.query(Users).filter(Users.email == email).all()

        if serialize:
            return [user.serialize() for user in all_users]
        else:
            return all_users

from flask import jsonify
from flask import abort
from flask import make_response
from flask import request
from flask import url_for

from data_provider_service import DataProviderService

db_engine = 'postgresql+psycopg2://postgres:12345678@localhost/FinanceRequisition'
DATA_PROVIDER = DataProviderService(db_engine)
request_obj = None


# Roles Objects
def roles(serialize=True):
    roles = DATA_PROVIDER.get_roles(serialize=True)
    if serialize:
        return jsonify({"roles": roles, "total": len(roles)})
    else:
        return roles


def role_by_email(email_address):
    user_roles = DATA_PROVIDER.get_roles(email_address, serialize=True)
    if user_roles:
        return jsonify({"roles": user_roles})
    else:
        #
        # In case we did not find the candidate by id
        # we send HTTP 404 - Not Found error to the client
        #
        abort(404)


def add_role(email_address):
    user_roles = DATA_PROVIDER.add_role(email_address)
    if user_roles:
        return jsonify({"roles": user_roles})
    else:
        #
        # In case we did not find the candidate by id
        # we send HTTP 404 - Not Found error to the client
        #
        abort(404)


def update_role(email_address):
    edited_roles = request.json
    updated_role = DATA_PROVIDER.update_role(email_address, edited_roles)
    if not updated_role:
        return make_response('', 204)
    else:
        return jsonify({"roles": updated_role})


# User Objects
def user_details(serialize=True):
    users = DATA_PROVIDER.get_user_details(serialize=True)
    if serialize:
        return jsonify({"users": users, "total": len(users)})
    else:
        return users


def user_details_by_email(email_address):
    user_details = DATA_PROVIDER.get_user_details(email_address, serialize=True)
    if user_details:
        return jsonify({"user": user_details})
    else:
        #
        # In case we did not find the candidate by id
        # we send HTTP 404 - Not Found error to the client
        #
        abort(404)

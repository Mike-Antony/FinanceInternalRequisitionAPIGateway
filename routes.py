from flask import jsonify
from flask import render_template
from flask import flash
from flask import current_app
from flask import abort
# Roles
from middleware import roles
from middleware import role_by_email
from middleware import add_role
from middleware import update_role
# Users
from middleware import user_details
from middleware import user_details_by_email
import requests
import json


def init_api_routes(app):
    if app:
        app.add_url_rule('/api', 'list_routes', list_routes, methods=['GET'], defaults={'app': app})
        # Roles
        app.add_url_rule('/api/roles', 'roles', roles, methods=['GET'])
        app.add_url_rule('/api/roles/<string:email_address>', 'role_by_email', role_by_email, methods=['GET'])
        app.add_url_rule('/api/roles/<string:email_address>', 'add_role', add_role, methods=['POST'])
        app.add_url_rule('/api/roles/<string:email_address>', 'update_role', update_role, methods=['PUT'])
        # Users
        app.add_url_rule('/api/users', 'user_details', user_details, methods=['GET'])
        app.add_url_rule('/api/users/<string:email_address>', 'user_details_by_email', user_details_by_email,
                         methods=['GET'])


def init_website_routes(app):
    if app:
        app.add_url_rule('/crash', 'crash_server', crash_server, methods=['GET'])
        app.add_url_rule('/about', 'page_about', page_about, methods=['GET'])
        app.add_url_rule('/', 'page_index', page_index, methods=['GET'])


def page_about():
    if current_app:
        flash('The application was loaded', 'info')
        flash('The secret key is {0}'.format(current_app.config['SECRET_KEY']), 'info')
    return render_template('about.html', selected_menu_item="about")


def page_index():
    api_link = 'http://127.0.0.1:1996/api'
    routes = requests.get(api_link)
    data = json.loads(routes.text)
    return render_template('index.html', data=data)


def crash_server():
    abort(500)


def list_routes(app):
    result = []
    for rt in app.url_map.iter_rules():
        result.append({
            'methods': list(rt.methods),
            'route': str(rt)
        })
    return jsonify({'routes': result, 'total': len(result)})

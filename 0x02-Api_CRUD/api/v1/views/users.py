#!/usr/bin/env python3
"""The blueprint for all CRUD operation for user."""
from models.user import User
from flask import jsonify, abort, request
from api.v1.views import app_views
from models import storage
from api.v1.views import *

parent_cls = User


@app_views.route(
    "/api",
    methods=["GET"],
    strict_slashes=False,
    defaults={"user_id": None}
)
@app_views.route("/api/<user_id>", methods=["GET"], strict_slashes=False)
def get_user(user_id):
    """Get all the user or get a specific user by user id."""
    if user_id:
        return get_match(parent_cls, user_id)
    uxr = [users.to_dict() for users in storage.all(User).values()]
    return jsonify(uxr)


@app_views.route(
    "/api/<user_id>",
    methods=["DELETE"],
    strict_slashes=False
)
def delete_user(user_id):
    """Delete a user by id."""
    return delete_match(parent_cls, user_id)


@app_views.route(
    "/api",
    methods=["POST"],
    strict_slashes=False,
)
def create_user():
    """Create a user via a POST request."""
    if not request.json:
        abort(400, description="Error: Not a valid JSON")
    if "name" not in request.json:
        abort(400, description="Error: Missing name")
    kwargs = request.get_json()
    return create_new(parent_cls, kwargs)


@app_views.route(
    "/api/<user_id>",
    methods=["PUT"],
    strict_slashes=False
)
def update_user(user_id):
    """Update a user by id."""
    if not request.json:
        abort(400, description="Error: Not a valid JSON")
    # validate if the current content exists
    get_user_obj = storage.get(parent_cls, user_id)
    if not get_user_obj:
        abort(404, description="Object instance not found")
    kwargs = request.get_json()
    return update_match(get_user_obj, kwargs)


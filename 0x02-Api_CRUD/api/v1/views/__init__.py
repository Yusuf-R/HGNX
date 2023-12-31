"""model for blue print view"""
from flask import Blueprint, make_response, jsonify, abort
from models import storage

app_views = Blueprint("app_views", __name__, url_prefix="/")


def get_match(cls, id):
    """GET: get the object of a specific class based on its id"""
    obj = storage.get(cls, id)
    if obj:
        return jsonify(obj.to_dict())
    abort(404)


def delete_match(cls, id):
    """DELETE: delete the object of a specific class based on its id"""
    obj = storage.get(cls, id)
    if obj:
        storage.delete(obj)
        storage.save()
        return make_response(jsonify({}), 200)
    abort(404)


def create_new(p_cls, kwargs):
    """POST: creating a new object for the class"""
    if p_cls:
        if not isinstance(kwargs["name"], str):
            abort(400, description="Error: name must be a string")
        # validate if the current name exists
        current_obj = storage.all(p_cls)
        if kwargs["name"] in [obj.name for obj in current_obj.values()]:
            abort(400, description="Error: name already exists")
        obj = p_cls(**kwargs)
        obj.save()
        return jsonify(obj.to_dict()), 201
    else:
        abort(404)


def update_match(obj, kwargs):
    """PUT: update the brand object"""
    exempt = ["id"]

    for key, value in kwargs.items():
        # validate if the current name exist in db
        current_obj = storage.all(obj.__class__)
        if kwargs[key] in [obj.name for obj in current_obj.values()]:
            abort(400, description="Update Error: name already exists")
        if key not in exempt and type(kwargs[key]) is str:
            setattr(obj, key, value)
        else:
            abort(400, description="Error: invalid key")
    obj.save()
    ret_data = jsonify(obj.to_dict())
    return make_response(ret_data, 200)


# used to instantiate the blueprint routes upon program start-up
from api.v1.views.users import *

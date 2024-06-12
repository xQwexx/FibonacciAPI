import functools

from flask import (
    Blueprint, flash, g, redirect, render_template, request, session, url_for
)

from api.db import get_db

bp = Blueprint('fibonacci', __name__, url_prefix='/fibonacci')

@bp.route('/<int:number>', methods=('GET'))
def register(number: int):
    return "test"

@bp.route('/list/<int:number>', methods=('GET'))
def register(number: int):
    return "test"

@bp.route('/blacklist/<int:number>', methods=('POST', 'DELETE'))
def register(number: int):
    return "test"
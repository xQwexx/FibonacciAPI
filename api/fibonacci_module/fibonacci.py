import functools

from flask import (
    Blueprint, flash, g, redirect, render_template, request, session, url_for
)

from flask import jsonify

from api.db import get_db
from api.fibonacci_module.calculator import fibpair_schema, fibpairs_schema, calcFibonacci, calcFibonacciList

bp = Blueprint('fibonacci', __name__, url_prefix='/fibonacci')

@bp.route('/<int:index>', methods=['GET'])
def getNumber(index: int):
    return fibpair_schema.dump(calcFibonacci(index))

@bp.route('/list/<int:index>', methods=['GET'])
def getList(index: int):
    fib_list = calcFibonacciList(index)
    return fibpairs_schema.dump(calcFibonacciList(index))

@bp.route('/blacklist/<int:index>', methods=['POST', 'DELETE'])
def blacklist(index: int):
    return "test"
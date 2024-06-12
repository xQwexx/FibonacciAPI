import functools

from flask import (
    Blueprint, flash, g, redirect, render_template, request, session, url_for
)

from flask import jsonify

from api.db import get_db
from api.fibonacci_module.calculator import FibonacciCalulator, fibpair_schema, fibpairs_schema

bp = Blueprint('fibonacci', __name__, url_prefix='/fibonacci')
calculator = FibonacciCalulator()

@bp.route('/<int:index>', methods=['GET'])
def getNumber(index: int):
    return fibpair_schema.dump(calculator.calcFibonacci(index))

@bp.route('/list/<int:index>', methods=['GET'])
def getList(index: int):
    page_size = request.args.get('page-size', default=100, type=int)
    page_number = request.args.get('page', default=1, type=int)
    fib_list = calculator.calcFibonacciList(index)
    return fibpairs_schema.dump(fib_list[(page_number-1) * page_size:][:page_size])

@bp.route('/blacklist/<int:index>', methods=['POST', 'DELETE'])
def blacklist(index: int):
    if request.method == 'POST':
        calculator.blacklistIndex(index)
    if request.method == 'DELETE':
        calculator.unBlacklistIndex(index)
    return "test"
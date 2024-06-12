import json
from operator import index
from marshmallow import Schema, fields


class FibPair():
    def __init__(self, index:int, value:int):
        self.index = index
        self.value = value

    def toJSON(self):
        return json.dumps(
            self,
            default=lambda o: o.__dict__, 
            sort_keys=True,
            indent=4)

class FibPairSchema(Schema):
    index = fields.Str()
    value = fields.Str()

fibpair_schema = FibPairSchema()
fibpairs_schema = FibPairSchema(many=True)

fib_cache = [FibPair(0, 0), FibPair(1, 1)]

def calcFibonacci(index: int) -> FibPair:
    return calcFibonacciList(index)[index]

def calcFibonacciList(index: int) -> list[FibPair]:
    if index < 0:
        raise "Incorrect input"

    elif index < len(fib_cache):
        return fib_cache[:index + 1]
    else:        
        fib_cache.append(FibPair(index, calcFibonacci(index - 1).value + calcFibonacci(index - 2).value))
        return fib_cache

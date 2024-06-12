import json
from operator import index
from marshmallow import Schema, fields

from api.db import get_db


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

class FibonacciCalulator():
    fib_cache = [FibPair(0, 0), FibPair(1, 1)]

    def calcFibonacci(self, index: int) -> FibPair:
        return self.calcFibonacciList(index)[index]

    def _calcFibonacciList(self, index: int) -> list[FibPair]:
        if index < 0:
            raise Exception("Incorrect index")

        elif index < len(self.fib_cache):
            return self.fib_cache[:index + 1]
        else:        
            self.fib_cache.append(FibPair(index, self.calcFibonacci(index - 1).value + self.calcFibonacci(index - 2).value))
            return self.fib_cache


    def calcFibonacciList(self, index: int) -> list[FibPair]:
        blacklisted = self.getBlacklistedIndexes()
        print(blacklisted)
        return self._calcFibonacciList(index)

    def getBlacklistedIndexes(self):
        db = get_db()
        cur = db.cursor()
        try:
            cur.execute(
                "SELECT * FROM blacklisted_index"
            )
            db.commit()
        except Exception as e:
            raise Exception(f"Index {index} update was unsucessful. Error: {e}")
        return [int(record[0]) for record in cur.fetchall()]

    def blacklistIndex(self, index: int):
        db = get_db()
        if index < 0:
            raise Exception("Incorrect index")
        print(index)
        try:
            cur = db.cursor()
            cur.execute(
                "INSERT INTO blacklisted_index (fib_index) VALUES (?)",
                (str(index),)
            )
            db.commit()
        except db.IntegrityError:
            raise Exception(f"Index {index} is already registered.")
        except Exception as e:
            raise Exception(f"Index {index} update was unsucessful. Error: {e}")

    def unBlacklistIndex(self, index: int):
        db = get_db()
        if index < 0:
            raise Exception("Incorrect index")
        print(index)
        try:
            cur = db.cursor()
            cur.execute(
                "DELETE FROM blacklisted_index WHERE fib_index = ?",
                (str(index),)
            )
            db.commit()
        except Exception as e:
            raise Exception(f"Index {index} delete was unsucessful. Error: {e}")
import web
from pprint import pprint

db = web.database(dbn='sqlite', db='db/db.sqlite3')

class Path:
    @classmethod
    def get_or_create(self, uid, start, dots, end, time):
        # todo check the data

        path = Path.query_by_uid(uid)
        if path:
            return path
        else:
            db.insert("paths", uid=uid, start=start, dots=dots, end=end, time=time)
            return Path.query_by_uid(uid)

    @classmethod
    def query_by_uid(self, uid):
        rst = db.select("paths", where=("uid=%s" % uid))
        for i in rst:
            return i
        return None

if __name__ == "__main__":
    Path.get_or_create(1, 1, "2", 3, 7)
    Path.get_or_create(2, 3, "2", 1, 7)

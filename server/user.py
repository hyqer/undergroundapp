import web
from pprint import pprint

db = web.database(dbn='sqlite', db='db/db.sqlite3')

class User:
    @classmethod
    def get_or_create(self, phone_id, name=None):
        if not name:
            name = phone_id
        user =  User.query_by_phone_id(phone_id)
        if user:
            return user
        else:
            db.insert("users", phone_id=phone_id, name=name)
            return User.query_by_phone_id(phone_id)

    @classmethod
    def query_by_phone_id(self, phone_id):
        rst = db.select("users", where=("phone_id=\"%s\"" % phone_id))
        for u in rst:
            return u
        return None

    @classmethod
    def query_by_uid(self, uid):
        rst = db.select("users", where=("id=%s" % uid))
        for u in rst:
            return u
        return None

    @classmethod
    def rec_friends_for_user(self, uid):
        # get path p of user u
        # calc the user list can rec to user u
        rst = db.select("users", where=("id != %s" % uid), limit=5)
        users = []
        for i in rst:
            users.append(i)
        return users

if __name__ == "__main__":
    User.get_or_create(name="xyz", phone_id="phs")
    User.get_or_create( phone_id="phonly")

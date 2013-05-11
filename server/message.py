import web
from datetime import datetime

from pprint import pprint

db = web.database(dbn='sqlite', db='db/db.sqlite3')

class Message:
    @classmethod
    def create(self, msg, source_uid, target_uid):
        id = db.insert("messages", msg=msg, source_uid=source_uid, target_uid=target_uid, is_read=0, created_at=datetime.utcnow())
        return Message.query_by_id(id)

    @classmethod
    def query_by_id(self, id):
        rst = db.select("messages", where=("id=%s" % id))
        for u in rst:
            return u
        return None

    @classmethod
    def query_unread_messages_by_target_uid(self, target_uid):
        rst = db.select("messages", where=(" target_uid=%s and is_read = 0" % target_uid), order="created_at desc") # add order limit
        messages = []
        for u in rst:
            messages.append(u)
        if len(messages) > 0:
            return messages
        return None

    @classmethod
    def set_message_as_read_by_id(cls, id):
        message = Message.query_by_id(id)
        if message:
            db.update("messages", where=(" id = %s " % id), is_read=1)

if __name__ == "__main__":
    # print Message.create("who r u?", 1, 2)
    print "before:"
    print "unread message of user(id=2)"
    pprint(Message.query_unread_messages_by_target_uid(2))

    for message in Message.query_unread_messages_by_target_uid(2):
        Message.set_message_as_read_by_id(message.id)
    print "\n\nafter:"
    print "unread message of user(id=2)"
    pprint(Message.query_unread_messages_by_target_uid(2))

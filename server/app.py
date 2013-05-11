import sqlite3
import json
import web

from user import User
from message import Message
        
urls = (
    '/(.*)', 'api'
)

app = web.application(urls, globals())

class api:        
    def GET(self, param):
        data = web.input()
        web.header('Content-Type', 'application/json')
        if "search" == data.api_name:
            return json.dumps({"search": "..............."})
        if "get_unread_message" == data.api_name:
            ret = {}
            user = User.query_by_uid(data.uid)
            messages = Message.query_unread_messages_by_target_uid(user.id)

            ret["user"] = user
            ret["messages"] = messages

            return json.dumps(ret)
        if "get_rec_users" == data.api_name:
            users = User.rec_friends_for_user(data.uid)
            ret = {"users": users}
            return json.dumps(ret)
        return json.dumps({"todo": "tada"})

if __name__ == "__main__":
    app.run()


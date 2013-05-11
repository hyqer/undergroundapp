import sqlite3
import json
import web

import user
        
urls = (
    '/(.*)', 'api'
)

app = web.application(urls, globals())

class api:        
    def GET(self, param):
        return json.dumps([1, 2, {"name": "cainanyang", "age": 12}])

if __name__ == "__main__":
    app.run()


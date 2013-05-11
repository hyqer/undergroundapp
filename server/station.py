import web

from pprint import pprint

db = web.database(dbn='sqlite', db='db/db.sqlite3')

class Station:
    @classmethod
    def get_or_create(self, name):
        station =  Station.query_by_name(name)
        if station:
            return station
        else:
            db.insert("stations", name=name)
            return Station.query_by_name(name)

    @classmethod
    def query_by_name(self, name):
        rst = db.select("stations", where=("name=\"%s\"" % name))
        for i in rst:
            return i
        return None

    @classmethod
    def query_by_id(self, id):
        rst = db.select("stations", where=("id=%s" % id))
        for i in rst:
            return i
        return None

if __name__ == "__main__":
    Station.get_or_create("Lujiabang")
    Station.get_or_create("Shangchen Road")
    Station.get_or_create("Renming Square")
    Station.get_or_create("Hongqiao Huochezhan")
    Station.get_or_create("Longyang Lu")
    Station.get_or_create("Songjiang Xinchen")
    pprint(Station.get_or_create("Lujiabang"))
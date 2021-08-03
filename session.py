from datetime import datetime as dt


class Session:
    def __init__(self, date):
        self.table_name = "sessions"

        date = (int(date[0]), date[2:].split(".")[1], date[2:].split(".")[0])
        today = f"2021-{date[1]}-{date[2]}"

        if int(date[0]) == 1:
            self.start_date = today + " 8:00:00"
            self.end_date = today + " 14:00:00"
        elif int(date[0]) == 2:
            self.start_date = today + " 18:30:00"
            self.end_date = today + " 23:30:00"
        else:
            pass

    def make_insert_query(self, table_name=""):
        if table_name:
            self.table_name = table_name
        return f"INSERT INTO {self.table_name} (`start_date`, `end_date`) " \
               f"VALUES ('{self.start_date}', '{self.end_date}')"

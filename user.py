class User:
    def __init__(self, number, money, session_id):
        self.table_name = "users"

        self.number = number
        self.money = money
        self.session_id = session_id

    def make_insert_query(self, table_name=""):
        if table_name:
            self.table_name = table_name
        return f"INSERT INTO {self.table_name} (`number`, `money`, `session_id`) " \
               f"VALUES ({self.number}, {self.money}, {self.session_id})"

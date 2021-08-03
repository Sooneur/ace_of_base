class Share:
    def __init__(self, user_number, share_type_id, amount):
        self.table_name = "shares"

        self.user_number = user_number
        self.share_type_id = share_type_id
        self.amount = amount

    def make_insert_query(self, table_name=""):
        if table_name:
            self.table_name = table_name
        return f"INSERT INTO {self.table_name} (`user_number`, `share_type_id`, `amount`) " \
               f"VALUES ({self.user_number}, {self.share_type_id}, {self.amount})"

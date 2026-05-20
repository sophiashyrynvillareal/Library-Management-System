class Member:
    def __init__(self, member_id, name, email):
        self._member_id = member_id
        self._name = name
        self._email = email

    @property
    def member_id(self):
        return self._member_id

    @property
    def name(self):
        return self._name

    @property
    def email(self):
        return self._email

    def display_info(self):
        print(f"{self._member_id} | {self._name} | {self._email}")
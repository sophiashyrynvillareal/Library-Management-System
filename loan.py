class Loan:
    def __init__(self, loan_id, book, member):
        self.loan_id = loan_id
        self.book = book
        self.member = member

    def display(self):
        print(f"{self.loan_id} | {self.book._title} | {self.member._name}")
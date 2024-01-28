class Task:
    def __init__(self, name, due_date):
        self.name = name
        self.due_date = due_date
        self.comments = []
        self.completed = False

    def change_name(self, new_name: str):
        if self.name == new_name:
            return f"Name cannot be the same."
        else:
            self.name = new_name
            return self.name

    def change_due_date(self, new_date: str):
        if self.due_date == new_date:
            return f"Date cannot be the same."
        else:
            self.due_date = new_date
            return self.due_date

    def add_comment(self, comment: str):
        self.comments.append(comment)

    def edit_comment(self, comment_number: int, new_comment: str):
        if comment_number < len(self.comments):
            self.comments[comment_number] = new_comment
            return ', '.join(self.comments)
        else:
            return f"Cannot find comment."

    def details(self):
        return f"Name: {self.name} - Due Date: {self.due_date}"












import sqlite3

class PublicationModel:
    def __init__(self, title, id, content):
        self.title = title
        self.id = id
        self.content = content

    def json(self):
        return {'title': self.title, 'id': self.id, 'content': self.content}

    @classmethod
    def find_by_title(cls, title):
        connection = sqlite3.connect('data.db')
        cursor = connection.cursor()

        query = "SELECT * FROM publications WHERE title=?"
        result = cursor.execute(query, (title,))
        row = result.fetchone()
        connection.close()

        if row:
            return cls(row[0], row[1], row[2])

    def insert(self):
        connection = sqlite3.connect('data.db')
        cursor = connection.cursor()

        query = "INSERT INTO publications VALUES (?, ?, ?)"
        cursor.execute(query, (self.title, self.id, self.content))

        connection.commit()
        connection.close()

    def update(self):
        connection = sqlite3.connect('data.db')
        cursor = connection.cursor()

        query = "UPDATE publications SET id=?, content=? WHERE title=?"
        cursor.execute(query, (self.title, self.id, self.content))

        connection.commit()
        connection.close()

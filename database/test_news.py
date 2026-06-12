import sqlite3

conn = sqlite3.connect("database/school.db")

cursor = conn.cursor()

cursor.execute("""

INSERT INTO news
(title, description)

VALUES
(
'ग्रीष्मकालीन अवकाश सूचना',
'विद्यालय 15 जून तक अवकाश रहेगा।'
)

""")

conn.commit()

conn.close()

print("News Added")
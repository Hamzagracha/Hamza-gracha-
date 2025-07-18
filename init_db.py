import sqlite3

connection = sqlite3.connect('database.db')
cursor = connection.cursor()

# إنشاء جدول المستخدمين
cursor.execute('''
CREATE TABLE IF NOT EXISTS users (
    id INTEGER PRIMARY KEY AUTOINCREMENT,
    username TEXT UNIQUE NOT NULL,
    password TEXT NOT NULL
)
''')

# مثال: إنشاء مستخدم افتراضي (اختياري)
cursor.execute('''
INSERT OR IGNORE INTO users (username, password) VALUES (?, ?)
''', ('admin', 'admin123'))  # ⚠️ غيّر كلمة السر لاحقًا

connection.commit()
connection.close()

print("✅ تم إنشاء قاعدة البيانات بنجاح.")
# مدیریت دانش‌آموزان با SQLAlchemy

پروژه‌ای ساده برای کار با پایگاه‌داده SQLite و SQLAlchemy شامل دو مثال:

1. **CRUD ساده** روی جدول دانش‌آموزان (`student_crud.py`)
2. **رابطه یک‌به‌چند** بین دانش‌آموز و درس (`students_courses.py`)

---

## ساختار فایل‌ها

```
.
├── student_crud.py        # عملیات Create / Read / Update / Delete روی دانش‌آموزان
├── students_courses.py    # مدل رابطه یک‌به‌چند (Student → Courses)
├── requirements.txt       # وابستگی‌ها
└── README.md
```

فایل‌های دیتابیس که به‌صورت خودکار ساخته می‌شوند:
- `students.db`  → مربوط به `student_crud.py`
- `school.db`    → مربوط به `students_courses.py`

---

## نصب وابستگی‌ها

ابتدا فایل `requirements.txt` را بسازید (یا نام فعلی `requirements.text` را اصلاح کنید):

```bash
pip install -r requirements.txt
```

محتوای پیشنهادی:

```
SQLAlchemy>=2.0
typing_extensions>=4.0
```

> نکته: نسخه نوشته‌شده در فایل فعلی (`SQLAlchemy==2.1.6`) ممکن است موجود نباشد. بهتر است از نسخه پایدار ۲.۰ به بالا استفاده کنید.

---

## ۱. CRUD ساده — `student_crud.py`

### مدل

| ستون | نوع     | توضیح              |
|------|---------|---------------------|
| id   | Integer | کلید اصلی (خودکار)  |
| name | String  | نام دانش‌آموز       |
| score| Float   | نمره                |

### توابع موجود

| تابع | کار |
|------|-----|
| `add_student(name, score)` | اضافه کردن دانش‌آموز جدید و برگرداندن `id` |
| `get_all_students()` | دریافت لیست تمام دانش‌آموزان |
| `update_student(student_id, name=None, score=None)` | ویرایش نام یا نمره |
| `delete_student(student_id)` | حذف دانش‌آموز |

### اجرای نمونه

```bash
python student_crud.py
```

خروجی تقریبی:

```
همه دانش‌آموزان: [<Student id=1 name=Ali score=18.5>, <Student id=2 name=Sara score=19>]
بعد از ویرایش: [<Student id=1 name=Ali score=20>, <Student id=2 name=Sara Ahmadi score=19>]
بعد از حذف: [<Student id=2 name=Sara Ahmadi score=19>]
```

---

## ۲. رابطه یک‌به‌چند — `students_courses.py`

### مدل‌ها

**Student**
- `id`, `name`
- رابطه: `courses` (لیست درس‌ها)

**Course**
- `id`, `title`, `unit`
- `student_id` (کلید خارجی به `students.id`)
- با `cascade="all, delete-orphan"`: حذف دانش‌آموز → حذف خودکار درس‌هایش

### اجرای نمونه

```bash
python students_courses.py
```

با اجرای این فایل یک دانش‌آموز به نام «Ali Ahmadi» همراه با دو درس Math و Physics در دیتابیس `school.db` ذخیره می‌شود.

---

## نکات مهم

1. **نام فایل وابستگی‌ها**  
   فایل فعلی `requirements.text` است. بهتر است به `requirements.txt` تغییر نام دهید.

2. **نسخه SQLAlchemy**  
   نسخه `2.1.6` ممکن است در PyPI موجود نباشد. پیشنهاد:
   ```bash
   pip install "SQLAlchemy>=2.0.0"
   ```

3. **echo=True** در `students_courses.py`  
   این گزینه تمام دستورات SQL را در ترمینال چاپ می‌کند. برای محیط واقعی می‌توانید آن را حذف کنید.

4. **کلید اصلی Course**  
   در نمونه، `id` درس‌ها به‌صورت دستی تنظیم شده (`id=1`, `id=2`). در کاربرد واقعی بهتر است `autoincrement=True` باشد.

---

## مثال استفاده سریع

```python
from student_crud import add_student, get_all_students, update_student, delete_student

# اضافه کردن
sid = add_student("رضا", 17.5)

# خواندن
print(get_all_students())

# ویرایش
update_student(sid, score=18)

# حذف
delete_student(sid)
```

---

## مجوز

این کد برای اهداف آموزشی ارائه شده است.

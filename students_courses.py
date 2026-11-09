from sqlalchemy import create_engine, Column, Integer, String, ForeignKey
from sqlalchemy.orm import declarative_base, relationship, sessionmaker

Base = declarative_base()


class Student(Base):
    __tablename__ = "students"

    id = Column(Integer, primary_key=True, autoincrement=True)
    name = Column(String(100), nullable=False)

    # یک دانشجو ← چند درس
    courses = relationship(
        "Course",
        back_populates="student",
        cascade="all, delete-orphan",  # حذف دانشجو => حذف درس‌هایش
    )


class Course(Base):
    __tablename__ = "courses"

    id = Column(Integer, primary_key=True)
    title = Column(String(100), nullable=False)
    unit = Column(Integer, nullable=False)
    student_id = Column(
        Integer,
        ForeignKey("students.id", ondelete="CASCADE"),
        nullable=False,
    )

    student = relationship("Student", back_populates="courses")


# ساخت دیتابیس و جدول‌ها
engine = create_engine("sqlite:///school.db", echo=True)
Base.metadata.create_all(engine)

# نمونه استفاده
Session = sessionmaker(bind=engine)
session = Session()

s1 = Student(name="Ali Ahmadi")
s1.courses = [
    Course(id=1, title="Math", unit=3),
    Course(id=2, title="Physics", unit=4),
]
session.add(s1)
session.commit()

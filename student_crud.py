from sqlalchemy import create_engine, Column, Integer, String, Float
from sqlalchemy.orm import declarative_base, sessionmaker

Base = declarative_base()


class Student(Base):
    __tablename__ = "student"

    id = Column(Integer, primary_key=True, autoincrement=True)
    name = Column(String(100), nullable=False)
    score = Column(Float, nullable=False)

    def __repr__(self):
        return f"<Student id={self.id} name={self.name} score={self.score}>"


engine = create_engine("sqlite:///students.db")
Base.metadata.create_all(engine)
Session = sessionmaker(bind=engine)


# Create
def add_student(name, score):
    with Session() as session:
        student = Student(name=name, score=score)
        session.add(student)
        session.commit()
        return student.id


# Read
def get_all_students():
    with Session() as session:
        return session.query(Student).all()


# Update
def update_student(student_id, name=None, score=None):
    with Session() as session:
        student = session.get(Student, student_id)
        if student is None:
            return False
        if name is not None:
            student.name = name
        if score is not None:
            student.score = score
        session.commit()
        return True


# Delete
def delete_student(student_id):
    with Session() as session:
        student = session.get(Student, student_id)
        if student is None:
            return False
        session.delete(student)
        session.commit()
        return True


if __name__ == "__main__":
    add_student("Ali", 18.5)
    add_student("Sara", 19)

    print("همه دانش‌آموزان:", get_all_students())

    update_student(1, score=20)
    update_student(2, name="Sara Ahmadi")
    print("بعد از ویرایش:", get_all_students())

    delete_student(1)
    print("بعد از حذف:", get_all_students())

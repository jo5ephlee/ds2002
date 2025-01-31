-- SQL Exercises (With Answers)
-- 1. Retrieve all students who enrolled in 2023.
SELECT * FROM students 
WHERE YEAR(EnrollmentDate) = 2023;
-- 2. Find students whose email contains 'gmail.com'.
SELECT * FROM students
WHERE email like '%gmail.com';
-- 3. Count how many students are enrolled in the database.
select count(*) as total_students from students;
-- 4. Find students born between 2000 and 2005.
select * from students
where year(DateOfBirth) between 2000 and 2005;
-- 5. List students sorted by last name in descending order.
select * from students
order by lastname desc;
-- 6. Find the names of students and the courses they are enrolled in.
select students.StudentID, students.FirstName, students.Lastname, courses.CourseName from students
inner join enrollments on students.StudentID = enrollments.StudentID
inner join courses on enrollments.CourseID = courses.CourseID;

-- 7. List all students and their courses, ensuring students without courses are included (LEFT JOIN).
select students.StudentID, students.FirstName, students.Lastname, courses.CourseName from students
left join enrollments on students.StudentID = enrollments.StudentID
left join courses on enrollments.CourseID = courses.CourseID;
-- 8. Find all courses with no students enrolled (LEFT JOIN).
select courses.CourseName
from courses
left join enrollments on courses.CourseID = enrollments.courseID
where enrollments.StudentID is null;
-- 10. List courses and show the number of students enrolled in each course.
select courses.CourseName, count(enrollments.studentID) as enrolled_students
from courses
left join enrollments on courses.courseID = enrollments.courseID
group by courses.CourseName;
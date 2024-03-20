-- SELECT * FROM students

COPY students(f_name, l_name,birthdate) 
TO 'C:\Users\julia\Desktop\Repositories\DI-Bootcamp-TTA11\week4\exported_students.csv' DELIMITER ',' CSV HEADER;

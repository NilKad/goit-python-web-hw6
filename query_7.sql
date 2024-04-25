select s.id as student_id, s."name" as student_name, g.grade as student_grade
from grades g 
join students s on s.id = g.student_id 
where g.subject_id  = 20 and s.group_id = 61;
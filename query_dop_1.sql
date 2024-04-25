select AVG(g.grade) as averge_grade
from grades g 
join subjects s ON s.id = g.subject_id 
where s.teacher_id = 22 and g.student_id = 35

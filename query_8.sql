select s.id as subject_id, s.name as subject_name, AVG(g.grade) as averge_grade
from subjects s 
join grades g on g.subject_id = s.id
where s.teacher_id = 23
group by s.id
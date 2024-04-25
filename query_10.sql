select s.id, s.name
from subjects s 
join grades g on g.student_id  = 33
where s.teacher_id = 22
group by s.id;
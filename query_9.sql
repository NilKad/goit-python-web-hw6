select s.id as subject_id, s."name" as subject_name 
from grades g 
join subjects s on s.id = g.subject_id 
where g.student_id  = 32
group by s.id;

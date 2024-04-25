--select t.id as teacher_id, t."name" as teacher_name, s."name" as subject_name
select s.id as subject_id, s."name" as subject_name
from subjects s 
--join teachers t on s.teacher_id = t.id 
where s.teacher_id  = 25;

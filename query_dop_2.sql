select s.id as student_id, s.name as student_name, g.grade, g.date as grade_date 
from grades g 
join students s on s.id = g.student_id 
where s.group_id = 61 and g.subject_id = 23 
and g.date = (
	select max(g.date)
	from grades g 
	join students s on s.id = g.student_id 
	where s.group_id = 61 and g.subject_id = 23
);

--select *
--from grades g 
--join students s on s.id = g.student_id 
--where s.group_id = 61 and g.subject_id = 23 
--order by g.date desc

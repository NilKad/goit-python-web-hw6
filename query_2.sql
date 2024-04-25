select s.id as student_id , s.name as student_name, AVG(g.grade) as averge_grade
from students s 
join grades g on s.id = g.student_id 
where g.subject_id = 22
group by s.id
order by averge_grade desc 
limit 1;
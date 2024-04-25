select s.id as student_id , s.name as student_name, AVG(g.grade) as averge_grade
from students s
join grades g on s.id = g.student_id 
group by s.id, s.name
order by averge_grade desc	
limit 5;


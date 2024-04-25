select gr.id as group_id, gr.name as group_name, AVG(g.grade) as averge_grade
from "groups" gr
join students s on s.group_id = gr.id  
join grades g on g.student_id = s.id
where g.subject_id  = 17
group by gr.id;


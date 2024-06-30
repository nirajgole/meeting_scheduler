
"""
select
username,
title,
meet_from,
meet_to,
case
when ('2024-06-29 18:08:50' between meet_from and meet_to) or ('2024-06-29 18:08:50' between meet_from and meet_to) then 0
else 1
end
as available
from calendar.schedule cs
left join calendar."user" ON "user".id = cs.user_id
left join calendar.meeting ON meeting.id = cs.meeting_id
"""

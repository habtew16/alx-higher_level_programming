-- 9-cities_by_state_join.sql
SELECT c.id, c.name, s.name FROM cities c, states s
WHERE c.state_id = s.id
GROUP BY c.id ASC;

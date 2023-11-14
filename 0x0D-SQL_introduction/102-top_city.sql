-- average by city with limit of 3
SELECT city, AVG(value) AS avg_temp FROM
(SELECT city, month, value FROM temperatures
WHERE month=7 OR month=8) AS A
GROUP BY city ORDER BY avg_temp DESC LIMIT 3;

-- max tempertaure of each stated
SELECT state, MAX(value) AS max_temp FROM temperatures GROUP BY state ASC

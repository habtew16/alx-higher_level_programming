-- 14-my_genres.sqlSELECT tgg.name FROM tv_genres AS tgg
JOIN tv_show_genres AS name
ON name.genre_id = tgg.id
JOIN tv_shows AS ts
ON ts.id = name.show_id
WHERE ts.title='Dexter'
GROUP BY tgg.name ASC;

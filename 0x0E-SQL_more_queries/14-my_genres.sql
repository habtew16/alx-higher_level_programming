-- 14-my_genres.sqlSELECT tgg.name FROM tv_genres AS tgg
SELECT tv_genres.name
FROM hbtn_0d_tvshows.tv_shows
JOIN hbtn_0d_tvshows.tv_genres ON tv_shows.id = tv_genres.show_id
WHERE tv_shows.title = 'Dexter'
ORDER BY tv_genres.name ASC;


/*Number of movies per year and genre*/

SELECT COUNT(*), g.name,EXTRACT (YEAR FROM release_date) AS NYEAR FROM movie
JOIN movie_genres 
ON movie_id = id
JOIN genre g
ON genre_id = g.id
WHERE EXTRACT (YEAR FROM release_date) IS NOT NULL
GROUP BY g.name, EXTRACT (YEAR FROM release_date)
HAVING COUNT(*) IS NOT NULL
ORDER BY g.name
LIMIT 20;
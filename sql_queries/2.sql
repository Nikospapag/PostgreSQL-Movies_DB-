/*Number of movies per genre*/

SELECT COUNT(*), g.name FROM movie
JOIN movie_genres 
ON movie_id = id
JOIN genre g
ON genre_id = g.id
GROUP BY g.name
HAVING COUNT(*) IS NOT NULL
ORDER BY g.name
LIMIT 20;
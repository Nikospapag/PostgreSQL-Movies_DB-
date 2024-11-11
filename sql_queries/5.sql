/*Favourite actor movie revenue per year*/

SELECT SUM(revenue), EXTRACT (YEAR FROM release_date) AS year FROM movie m
JOIN movie_cast
ON movie_id = m.id
JOIN person p
ON person_id = p.id 
WHERE p.name='Will Smith'  
GROUP BY year
LIMIT 20;
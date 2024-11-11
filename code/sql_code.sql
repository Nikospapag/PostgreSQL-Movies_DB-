
/*Number of movies per year*/

SELECT COUNT(*), EXTRACT (YEAR FROM release_date)AS YEAR FROM movie
GROUP BY EXTRACT(YEAR FROM release_date )
ORDER BY YEAR;

/*Number of movies per genre*/

SELECT COUNT(*), g.name FROM movie
JOIN movie_genres 
ON movie_id = id
JOIN genre g
ON genre_id = g.id
GROUP BY g.name
HAVING COUNT(*) IS NOT NULL
ORDER BY g.name;

/*Number of movies per year and genre*/

SELECT COUNT(*), g.name,EXTRACT (YEAR FROM release_date) AS NYEAR FROM movie
JOIN movie_genres 
ON movie_id = id
JOIN genre g
ON genre_id = g.id
WHERE EXTRACT (YEAR FROM release_date) IS NOT NULL
GROUP BY g.name, EXTRACT (YEAR FROM release_date)
HAVING COUNT(*) IS NOT NULL
ORDER BY g.name;

/*Max Movie budget per year*/

SELECT MAX(budget), EXTRACT (YEAR FROM release_date)AS YEAR FROM movie
GROUP BY YEAR
ORDER BY YEAR;

/*Favourite actor movie revenue per year*/

SELECT SUM(revenue), EXTRACT (YEAR FROM release_date) AS year FROM movie m
JOIN movie_cast
ON movie_id = m.id
JOIN person p
ON person_id = p.id 
WHERE p.name='Will Smith'  
GROUP BY year;

/*User Average Rating*/

SELECT user_id, AVG(rating) from ratings
GROUP BY user_id
ORDER BY user_id;

/*User Number of ratings*/
SELECT user_id, COUNT(rating) from ratings
GROUP BY user_id
ORDER BY user_id;

/*Number of ratings and Average Ratings*/
SELECT user_id, COUNT(rating), AVG(rating) from ratings
GROUP BY user_id
ORDER BY user_id;

/*Average Rating per Genre*/
SELECT AVG(rating), g.name FROM ratings r 
JOIN movie_genres m
ON m.movie_id = r.movie_id
JOIN genre g
ON m.genre_id = g.id
GROUP BY g.name;
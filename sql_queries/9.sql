/*Average Rating per Genre*/
SELECT AVG(rating), g.name FROM ratings r 
JOIN movie_genres m
ON m.movie_id = r.movie_id
JOIN genre g
ON m.genre_id = g.id
GROUP BY g.name;
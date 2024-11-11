/*User Average Rating*/

SELECT user_id, AVG(rating) from ratings
GROUP BY user_id
ORDER BY user_id
LIMIT 20;
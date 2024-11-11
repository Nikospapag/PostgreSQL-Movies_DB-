/*Number of ratings and Average Ratings*/
SELECT user_id, COUNT(rating), AVG(rating) from ratings
GROUP BY user_id
ORDER BY user_id
LIMIT 20;
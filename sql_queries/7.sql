/*User Number of ratings*/
SELECT user_id, COUNT(rating) from ratings
GROUP BY user_id
ORDER BY user_id
LIMIT 20;
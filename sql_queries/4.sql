/*Max Movie budget per year*/

SELECT MAX(budget), EXTRACT (YEAR FROM release_date)AS YEAR FROM movie
GROUP BY YEAR
ORDER BY YEAR
LIMIT 20;
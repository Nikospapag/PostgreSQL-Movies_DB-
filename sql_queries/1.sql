/*Number of movies per year*/

SELECT COUNT(*), EXTRACT (YEAR FROM release_date)AS YEAR FROM movie
GROUP BY EXTRACT(YEAR FROM release_date )
ORDER BY YEAR
LIMIT 20;
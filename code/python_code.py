import matplotlib.pyplot as plt
import numpy as np
import psycopg2
from mpl_toolkits.mplot3d import axes3d



host = "localhost"
port="5432"
dbname = "movies_db"
user = "postgres"
password = "admin"

conn_string = "host={0} port={1} dbname={2} user={3} password={4}".format(host, port, dbname, user, password)
conn = psycopg2.connect(conn_string)
print("Connection established")

cursor = conn.cursor()


#Number of movies per year

cursor.execute('''SELECT COUNT(*), EXTRACT (YEAR FROM release_date)AS YEAR FROM movie
GROUP BY EXTRACT(YEAR FROM release_date )
ORDER BY YEAR;''')
rows = cursor.fetchall()



data = np.transpose(rows)


plt.plot(data[1],data[0])
plt.ylabel('Number of movies')
plt.xlabel('Year')
plt.title('Number of movies per year')
plt.show()

#Number of movies per genre


cursor.execute('''SELECT COUNT(*), g.name FROM movie
JOIN movie_genres 
ON movie_id = id
JOIN genre g
ON genre_id = g.id
GROUP BY g.name
HAVING COUNT(*) IS NOT NULL
ORDER BY g.name;''')
rows = cursor.fetchall()



data = np.transpose(rows)

genres =[]
number_movies=[]

for row in rows:
    number_movies.append(int(row[0]))
    genres.append(row[1])



plt.bar(genres,number_movies)



plt.ylabel('Number of movies')
plt.xlabel('Genre')
plt.title('Number of movies per genre')
plt.show()

#Number of movies per year and genre

cursor.execute('''SELECT COUNT(*), g.name,EXTRACT (YEAR FROM release_date) AS NYEAR FROM movie
JOIN movie_genres 
ON movie_id = id
JOIN genre g
ON genre_id = g.id
WHERE EXTRACT (YEAR FROM release_date) IS NOT NULL
GROUP BY g.name, EXTRACT (YEAR FROM release_date)
HAVING COUNT(*) IS NOT NULL
ORDER BY g.name;''')
rows = cursor.fetchall()

number_movies=[]
year=[]
genres=[]

for row in rows:
    number_movies.append(int(row[0]))
    genres.append(row[1])
    year.append(int(row[2]))
    

fig = plt.figure()
ax1 = fig.add_subplot(111, projection='3d')
ax1.set_facecolor((1.0, 1.0, 1.0))

xCategories = genres
i=0
xDict = {}
x=[]

for category in xCategories:
  if category not in xDict:
    xDict[category]=i
    x.append(i)
    i+=1
  else:
    x.append(xDict[category])

z = np.zeros(len(x))

dx = np.ones(len(x))*0.1
dy = np.ones(len(x))
dz = number_movies
ax1.bar3d(x, year, z, dx, dy, dz)
ax1.set_zlim([0, max(number_movies)])
plt.xticks(range(len(xDict.values())), xDict.keys())
ax1.set_title('Number of movies per year and genre')
plt.show()



#Max Movie budget per year

cursor.execute('''SELECT MAX(budget), EXTRACT (YEAR FROM release_date)AS YEAR FROM movie
GROUP BY YEAR
ORDER BY YEAR;''')
rows = cursor.fetchall()


year=[]
budget=[]

for row in rows:
    budget.append(float(row[0])/10**6)
    year.append(row[1])







plt.plot(year,budget)




plt.ylabel('Budget(millions)')
plt.xlabel('Year')
plt.title('Highest movie budget per year')
plt.show()


year.clear()
budget.clear()


#Favourite actor movie revenue per year

cursor.execute('''SELECT SUM(revenue), EXTRACT (YEAR FROM release_date) AS year FROM movie m
JOIN movie_cast
ON movie_id = m.id
JOIN person p
ON person_id = p.id 
WHERE p.name='Will Smith'  
GROUP BY year;''')
rows = cursor.fetchall()


year=[]
revenue=[]

for row in rows:
    revenue.append(row[0]/10**6)
    year.append(row[1])





plt.plot(year,revenue)




plt.ylabel('Revenue(millions)')
plt.xlabel('Year')
plt.title('Will Smith Movies Revenue per Year')
plt.show()

year.clear()
revenue.clear()
#User Average Rating

cursor.execute('''SELECT user_id, AVG(rating) from ratings
GROUP BY user_id
ORDER BY user_id;''')
rows = cursor.fetchall()



data = np.transpose(rows)




plt.scatter(data[1],data[0])




plt.ylabel('User id')
plt.xlabel('Average Rating')
plt.title('Average Rating per User')
plt.show()

#User Number of ratings

cursor.execute('''SELECT user_id, COUNT(rating) from ratings
GROUP BY user_id
ORDER BY user_id;''')
rows = cursor.fetchall()



data = np.transpose(rows)




plt.scatter(data[1],data[0])




plt.ylabel('User id')
plt.xlabel('Number of ratings')
plt.title('Number of Ratings per User')
plt.show()


#Number of ratings and Average Ratings

cursor.execute('''SELECT user_id, COUNT(rating), AVG(rating) from ratings
GROUP BY user_id
ORDER BY user_id;''')
rows = cursor.fetchall()



data = np.transpose(rows)




plt.scatter(data[1],data[2])




plt.ylabel('Average Rating')
plt.xlabel('Number of ratings')
plt.title('Average Rating and Number of Ratings per User')
plt.show()



#Average Rating per Genre
cursor.execute('''SELECT AVG(rating), g.name FROM ratings r 
JOIN movie_genres m
ON m.movie_id = r.movie_id
JOIN genre g
ON m.genre_id = g.id
GROUP BY g.name;''')
rows = cursor.fetchall()


genres=[]
ratings=[]
for row in rows:
    ratings.append(row[0])
    genres.append(row[1])
    


plt.bar(genres,ratings)




plt.ylabel('Average Rating ')
plt.xlabel('Genre')
plt.title('Average Rating of movies per genre')
plt.show()

conn.commit()
cursor.close()
conn.close()
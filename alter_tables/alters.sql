ALTER TABLE movie_keywords
ADD FOREIGN KEY (keyword) REFERENCES keyword(id);

ALTER TABLE movie_cast
ADD FOREIGN KEY (movie_id) REFERENCES movie(id);

ALTER TABLE movie_collection
ADD FOREIGN KEY (movie_id) REFERENCES movie(id);

ALTER TABLE movie_crew
ADD FOREIGN KEY (movie_id) REFERENCES movie(id);

ALTER TABLE movie_genres
ADD FOREIGN KEY (movie_id) REFERENCES movie(id);

ALTER TABLE movie_productioncompanies
ADD FOREIGN KEY (movie_id) REFERENCES movie(id);

ALTER TABLE ratings
ADD FOREIGN KEY (movie_id) REFERENCES movie(id);
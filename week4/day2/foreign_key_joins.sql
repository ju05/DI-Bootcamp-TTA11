-- CREATE TABLE movies(
-- movie_id SERIAL,
-- movie_title VARCHAR (50) NOT NULL,
-- movie_story TEXT,
-- actor_playing_id INTEGER,
-- PRIMARY KEY (movie_id),
-- FOREIGN KEY (actor_playing_id)
-- REFERENCES actors (actor_id)
-- );
-- INSERT INTO movies (movie_title, movie_story, actor_playing_id) VALUES
--     ( 'Good Will Hunting', 
--     'Written by Affleck and Damon, the film follows 20-year-old South Boston janitor Will Hunting',
--     (SELECT actor_id from actors WHERE first_name='Matt' AND last_name='Damon')),
--     ( 'Oceans Eleven', 
--     'American heist film directed by Steven Soderbergh and written by Ted Griffin.', 
--     (SELECT actor_id from actors WHERE first_name='Matt' AND last_name='Damon'));
	
-- SELECT * FROM MOVIES


-- INSERT INTO movies (movie_title, movie_story)
-- VALUES
-- ('Harry Potter and the goblet of fire', 'Harry retorna para seu quarto ano na Escola de Magia e Bruxaria de Hogwarts, junto com os seus amigos Ron e Hermione.');

-- SELECT * FROM MOVIES
-- INNER JOIN: JUST DATA/ROWS THAT I HAVE IN BOTH TABLES
-- SELECT actors.first_name, actors.last_name, movies.movie_title
-- FROM movies 
-- INNER JOIN actors
-- ON movies.actor_playing_id = actors.actor_id 

-- LEFT JOIN: ALL THE DATA IN THE LEFT TABLE AND DATA FROM THE RIGHT TABLE
-- SELECT actors.first_name, actors.last_name, movies.movie_title
-- FROM actors
-- LEFT OUTER JOIN movies
-- ON actors.actor_id = movies.actor_playing_id

-- RIGHT JOIN: ALL THE DATA FROM THE RIGHT TABLE
-- SELECT actors.first_name, actors.last_name, movies.movie_title
-- FROM actors
-- RIGHT OUTER JOIN movies
-- ON actors.actor_id = movies.actor_playing_id

-- full join: gives everything from both tables, creating null values if needed

SELECT actors.first_name, actors.last_name, movies.movie_title
FROM actors
FULL JOIN movies
ON actors.actor_id = movies.actor_playing_id


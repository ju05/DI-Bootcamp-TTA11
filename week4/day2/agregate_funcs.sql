-- SELECT * FROM actors

-- SELECT number_oscars AS oscars
-- FROM actors;


-- SELECT avg(number_oscars)
-- AS average_oscars_per_actor
-- FROM actors

-- INSERT INTO actors (first_name, last_name, age, number_oscars)
-- VALUES
-- ('George', 'Clooney', '05/06/1961', 1);

-- SELECT * FROM actors

-- SELECT count(first_name)
-- AS total_actor
-- FROM actors
-- WHERE first_name = 'George'

-- SELECT count(*) FROM actors
-- SELECT * FROM actors

-- SELECT first_name, last_name, sum(number_oscars)
-- AS best_actor
-- FROM actors
-- GROUP BY first_name, last_name

-- INSERT INTO actors (first_name, last_name, age, number_oscars)
-- VALUES('Matt','Ross','03/01/1970', 0);

-- SELECT DISTINCT first_name FROM actors;
-- SELECT * FROM actors

-- SELECT * FROM actors 
-- WHERE first_name not in ('Gal', 'Brad', 'George')

-- SELECT * FROM actors 
-- WHERE number_oscars between '1961-01-01' and '1962-01-01'


-- CLASS EXERCISE
-- SELECT avg(number_oscars) as avg_oscars
-- FROM actors

-- SELECT DISTINCT first_name FROM actors WHERE number_oscars BETWEEN 0 AND 5
SELECT DISTINCT number_oscars FROM actors ORDER BY number_oscars

-- SELECT * 
-- FROM actors
-- WHERE age > '01/01/1970'

-- SELECT * FROM actors WHERE first_name in ('David', 'Morgan', 'Will')
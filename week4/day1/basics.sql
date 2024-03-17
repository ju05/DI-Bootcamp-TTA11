-- CREATE TABLE actors (
--     actor_id SERIAL PRIMARY KEY,PG
--     first_name VARCHAR(50) NOT NULL,
--     last_name VARCHAR(100) NOT NULL,
--     age DATE NOT NULL,
--     number_oscars SMALLINT NOT NULL
-- )

-- INSERT INTO actors (first_name, last_name, age, number_oscars)
-- VALUES ('Matt', 'Damon', '08/10/1970', 5)

-- INSERT INTO actors (first_name, last_name, age, number_oscars)
-- VALUES 
-- ('George', 'Clooney', '06/05/1961', 2),
-- ('Gal', 'Gadot', '04/30/1985', 2)
-- ('Brad', 'Pitt', '12/18/1963', 2)

-- SELECT number_oscar FROM actors WHERE first_name = 'Gal'

-- SELECT first_name, last_name FROM actors WHERE NUMBER_OSCARS >= 2
-- AND age '08/10/1970'

-- LIKE = case sensitive
-- ILIKE + not case sensitive
SELECT * FROM actors WHERE last_name LIKE '%mon%'
SELECT * FROM actors WHERE last_name LIKE '%y'
SELECT * FROM actors WHERE last_name ILIKE 'ga%'


-- LIMIT
-- OFFSET (skips the number of rows written right after the keyword)
SELECT * FROM actors LIMIT 1;
SELECT * FROM actors WHERE age > '1960-01-01' LIMIT 3 OFFSET 2;

-- ORDER BY
SELECT * FROM actors WHERE age > '1960-01-01' ORDER BY first_name ASC

-- 
UPDATE actors
SET first_name = 'Angelina',
last_name = 'Jolie'
WHERE first_name = "Brad"

DELETE FROM actors 
WHERE first_name = 'Angelina'

ALTER TABLE actors RENAME COLUMN fisrt_name to first_name

INSERT INTO actors (first_name, last_name, age, number_oscars)
VALUES 
('George', 'Clooney', '06/05/1961', 2),

DROP TABLE IF EXISTS actors
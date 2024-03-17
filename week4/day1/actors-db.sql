CREATE TABLE actors (
    actor_id SERIAL PRIMARY KEY,
    first_name VARCHAR(50) NOT NULL,
    last_name VARCHAR(100) NOT NULL,
    age DATE NOT NULL,
    number_oscars SMALLINT NOT NULL
);

INSERT INTO actors (first_name, last_name, age, number_oscars)
VALUES ('Matt', 'Damon', '08/10/1970', 5);

INSERT INTO actors (first_name, last_name, age, number_oscars)
VALUES 
('George', 'Clooney', '06/05/1961', 2),
('Gal', 'Gadot', '30/04/1985', 2),
('Brad', 'Pitt', '18/12/1963', 2)
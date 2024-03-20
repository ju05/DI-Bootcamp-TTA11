-- CREATE TABLE FirstTab (
--      id integer, 
--      name VARCHAR(10)
-- )

-- INSERT INTO FirstTab VALUES
-- (5,'Pawan'),
-- (6,'Sharlee'),
-- (7,'Krish'),
-- (NULL,'Avtaar');

-- SELECT * FROM FirstTab

-- CREATE TABLE SecondTab (
--     id integer 
-- )

-- INSERT INTO SecondTab VALUES
-- (5),
-- (NULL)


-- SELECT * FROM SecondTab

-- SELECT COUNT(*) 
-- FROM FirstTab AS ft 
-- WHERE ft.id NOT IN (SELECT id FROM SecondTab WHERE id IS NULL)

-- output: 1
-- output: 0: the only value found is a NULL, so it is 0

SELECT COUNT(*) 
FROM FirstTab AS ft WHERE ft.id NOT IN (SELECT id FROM SecondTab)
-- output = 2
-- output is 0
--  List all the cities of California in the selected database
SELECT * FROM cities WHERE state_id = (
	SELECT id FROM states WHERE name = "California"
) ORDER BY cities.id;

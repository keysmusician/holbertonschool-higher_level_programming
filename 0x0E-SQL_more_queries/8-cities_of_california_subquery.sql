--  List all the cities of California in the selected database
SELECT * from cities WHERE state_id = (
	SELECT id from states where name = "California"
);

CREATE TABLE towns(
	id SERIAL PRIMARY KEY,
	name VARCHAR(45) NOT NULL
);

CREATE TABLE stadiums(
	id SERIAL PRIMARY KEY,
	name VARCHAR(45) NOT NULL,
	capacity INT NOT NULL,
	town_id INT NOT NULL,
	CONSTRAINT stadiums_capacity CHECK (capacity > 0),
	CONSTRAINT fk_stadiums_towns
	FOREIGN KEY (town_id)
	REFERENCES towns(id)
	ON DELETE CASCADE
	ON UPDATE CASCADE
);

CREATE TABLE teams(
	id SERIAL PRIMARY KEY,
	name VARCHAR(45) NOT NULL,
	established DATE NOT NULL,
	fan_base INT DEFAULT 0 NOT NULL,
	stadium_id INT NOT NULL,
	CONSTRAINT teams_fan_base CHECK (fan_base >= 0),
	CONSTRAINT fk_teams_stadiums
	FOREIGN KEY (stadium_id)
	REFERENCES stadiums(id)
	ON DELETE CASCADE
	ON UPDATE CASCADE
);

CREATE TABLE coaches(
	id SERIAL PRIMARY KEY,
	first_name VARCHAR(10) NOT NULL,
	last_name VARCHAR(20) NOT NULL,
	salary NUMERIC(10, 2) DEFAULT 0 NOT NULL,
	coach_level INT DEFAULT 0 NOT NULL,
	CONSTRAINT coaches_salary CHECK (salary >= 0),
	CONSTRAINT coaches_coach_level CHECK (coach_level >= 0)
);

CREATE TABLE skills_data(
	id SERIAL PRIMARY KEY,
	dribbling INT DEFAULT 0,
	pace INT DEFAULT 0,
	"passing" INT DEFAULT 0,
	shooting INT DEFAULT 0,
	speed INT DEFAULT 0,
	strength INT DEFAULT 0,
	CONSTRAINT skills_data_dribbling CHECK (dribbling >= 0),
	CONSTRAINT skills_data_pace CHECK (pace >= 0),
	CONSTRAINT skills_data_passing CHECK ("passing" >= 0),
	CONSTRAINT skills_data_shooting CHECK (shooting >= 0),
	CONSTRAINT skills_data_speed CHECK (speed >= 0),
	CONSTRAINT skills_data_strength CHECK (strength >= 0)
);

CREATE TABLE players(
	id SERIAL PRIMARY KEY,
	first_name VARCHAR(10) NOT NULL,
	last_name VARCHAR(20) NOT NULL,
	age INT DEFAULT 0 NOT NULL,
	"position" CHAR(1) NOT NULL,
	salary NUMERIC(10, 2) DEFAULT 0 NOT NULL,
	hire_date TIMESTAMP,
	skills_data_id INT NOT NULL,
	team_id INT,
	CONSTRAINT players_age CHECK (age >= 0),
	CONSTRAINT players_salary CHECK (salary >= 0),
	CONSTRAINT fk_players_skills_data
	FOREIGN KEY (skills_data_id)
	REFERENCES skills_data(id)
	ON DELETE CASCADE
	ON UPDATE CASCADE,
	CONSTRAINT fk_players_teams
	FOREIGN KEY (team_id)
	REFERENCES teams(id)
	ON DELETE CASCADE
	ON UPDATE CASCADE	
);

CREATE TABLE players_coaches(
	player_id INT,
	coach_id INT,
	CONSTRAINT fk_players_coaches_players
	FOREIGN KEY(player_id)
	REFERENCES players(id)
	ON DELETE CASCADE
	ON UPDATE CASCADE,
	CONSTRAINT fk_players_coaches_coaches
	FOREIGN KEY(coach_id)
	REFERENCES coaches(id)
	ON DELETE CASCADE
	ON UPDATE CASCADE
);


INSERT INTO coaches(first_name, last_name, salary, coach_level)
SELECT first_name, last_name, salary * 2 AS salary, LENGTH(first_name) AS coach_level
FROM players


UPDATE coaches
SET salary = salary * coach_level
WHERE first_name LIKE 'C%' AND id IN (
    SELECT DISTINCT coach_id
    FROM players_coaches
    WHERE coach_id IS NOT NULL
);


DELETE FROM players_coaches
WHERE player_id IN (
SELECT id FROM players
WHERE hire_date < '2013-12-13 07:18:46'
);

DELETE FROM players
WHERE hire_date < '2013-12-13 07:18:46';


SELECT CONCAT(first_name, ' ', last_name) AS full_name,
age, hire_date
FROM players p
WHERE p.first_name LIKE 'M%'
ORDER BY age DESC, full_name;


SELECT p.id, CONCAT(p.first_name, ' ', p.last_name) AS full_name,
p.age, p.position, p.salary, sd.pace, sd.shooting
FROM players p
JOIN skills_data sd ON p.skills_data_id = sd.id
WHERE p.position LIKE '%A%' AND sd.pace + sd.shooting > 130 AND p.team_id IS NULL;


SELECT t.id AS team_id, 
t.name AS team_name,
COUNT(p.id) AS player_count,
t.fan_base
FROM teams AS t
LEFT JOIN players AS p ON p.team_id = t.id
GROUP BY t.id, t.name, t.fan_base
HAVING t.fan_base > 30000
ORDER BY player_count DESC, t.fan_base DESC;


SELECT CONCAT(c.first_name, ' ', c.last_name) AS coach_full_name,
CONCAT(p.first_name, ' ', p.last_name) AS player_full_name,
t.name AS team_name,
sd.passing, sd.shooting, sd.speed
FROM coaches c
JOIN players_coaches pc ON pc.coach_id = c.id
JOIN players p ON pc.player_id = p.id
JOIN teams t ON p.team_id = t.id
JOIN skills_data sd ON p.skills_data_id = sd.id
ORDER BY coach_full_name, player_full_name DESC;


CREATE OR REPLACE FUNCTION fn_stadium_team_name(
stadium_name VARCHAR(30)
)
RETURNS TABLE(
	team_name VARCHAR(45)
)
AS $$
BEGIN
	RETURN QUERY
	SELECT t.name AS team_name
	FROM teams AS t
	JOIN stadiums AS s ON t.stadium_id = s.id
	WHERE s.name = stadium_name
	ORDER BY t.name;
END;
$$
LANGUAGE plpgsql;


CREATE PROCEDURE sp_players_team_name(
IN player_name VARCHAR(50),
OUT team_name VARCHAR(45)
)
LANGUAGE plpgsql
AS $$
BEGIN
	SELECT COALESCE(t.name, 'The player currently has no team')
	INTO team_name
	FROM players p
	LEFT JOIN teams t ON p.team_id = t.id
	WHERE CONCAT(p.first_name, ' ', p.last_name) = player_name;
END;
$$;



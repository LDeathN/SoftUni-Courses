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



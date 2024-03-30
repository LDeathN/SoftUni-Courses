CREATE FUNCTION fn_full_name(first_name VARCHAR, last_name VARCHAR)
RETURNS VARCHAR AS $$
BEGIN
    IF first_name IS NULL AND last_name IS NULL THEN
        RETURN NULL;
    ELSE
        RETURN INITCAP(COALESCE(first_name, '') || ' ' || COALESCE(last_name, ''));
    END IF;
END;
$$ LANGUAGE plpgsql;


CREATE OR REPLACE FUNCTION fn_calculate_future_value(
    initial_sum DECIMAL,
    yearly_interest_rate DECIMAL,
    number_of_years INT
)
RETURNS DECIMAL AS $$
BEGIN
    RETURN TRUNC(
		initial_sum * POWER(1 + yearly_interest_rate, number_of_years),
		4
	);
END;
$$ LANGUAGE plpgsql


CREATE OR REPLACE FUNCTION fn_is_word_comprised(
    set_of_letters VARCHAR(50),
    word VARCHAR(50)
)
RETURNS BOOLEAN AS $$
DECLARE
    i INTEGER := 1;
    current_char CHAR(1);
BEGIN
    
    set_of_letters := LOWER(set_of_letters);
    word := LOWER(word);

    
    WHILE i <= LENGTH(word) LOOP
        
        current_char := SUBSTRING(word FROM i FOR 1);

       
        IF POSITION(current_char IN set_of_letters) = 0 THEN
            RETURN FALSE;
        END IF;

       
        i := i + 1;
    END LOOP;

   
    RETURN TRUE;
END;
$$ LANGUAGE plpgsql;


CREATE OR REPLACE FUNCTION fn_is_game_over(
    is_game_over BOOLEAN
)
RETURNS TABLE (
    name VARCHAR(50),
    game_type_id INT,
    is_finished BOOLEAN
) AS $$
BEGIN
    RETURN QUERY 
    SELECT g.name, g.game_type_id, g.is_finished
    FROM games AS g
    WHERE g.is_finished = is_game_over;
END;
$$ LANGUAGE plpgsql;


CREATE OR REPLACE FUNCTION fn_difficulty_level(level INT)
RETURNS VARCHAR(50) AS $$
BEGIN
    IF level <= 40 THEN
        RETURN 'Normal Difficulty';
    ELSIF level BETWEEN 41 AND 60 THEN
        RETURN 'Nightmare Difficulty';
    ELSE
        RETURN 'Hell Difficulty';
    END IF;
END;
$$ LANGUAGE plpgsql;

SELECT
    user_id,
    level,
    cash,
    fn_difficulty_level(level) AS difficulty_level
FROM
    users_games
ORDER BY
    user_id ASC;


CREATE OR REPLACE FUNCTION fn_cash_in_users_games(game_name VARCHAR(50))
RETURNS TABLE (total_cash NUMERIC) AS $$
BEGIN
    RETURN QUERY 
    WITH ranked_games AS (
	SELECT cash, ROW_NUMBER() OVER (ORDER BY cash DESC) AS row_num
	FROM users_games AS ug
	JOIN games AS g ON ug.game_id = g.id
	WHERE g.name = game_name
	)
	
	SELECT ROUND(SUM(cash), 2) AS total_cash
	FROM ranked_games
	WHERE row_num % 2 <> 0;
END;
$$ LANGUAGE plpgsql;


CREATE OR REPLACE PROCEDURE sp_deposit_money(
    IN account_id INTEGER,
    IN money_amount NUMERIC(10, 4)
)
LANGUAGE plpgsql AS $$
BEGIN
    UPDATE accounts
    SET balance = balance + money_amount
    WHERE id = account_id;

    COMMIT;
END;
$$;


CREATE OR REPLACE PROCEDURE sp_withdraw_money(
    account_id INTEGER,
    money_amount NUMERIC(10, 4)
) AS 
$$
DECLARE
    current_balance NUMERIC;
BEGIN
    current_balance := (SELECT balance FROM accounts WHERE id = account_id);
	
	IF (current_balance - money_amount) >= 0 THEN
		UPDATE accounts
		SET balance = balance - money_amount
		WHERE id = account_id;
	ELSE
		RAISE NOTICE 'Insufficient balance to withdraw %', money_amount;
	END IF;
END;
$$
LANGUAGE plpgsql;


CREATE OR REPLACE PROCEDURE sp_transfer_money(
    sender_id INTEGER,
    receiver_id INTEGER,
    amount NUMERIC(10, 4)
)
LANGUAGE plpgsql AS $$
DECLARE
    current_balance NUMERIC;
BEGIN
    CALL sp_withdraw_money(sender_id, amount);
	CALL sp_deposit_money(receiver_id, amount);
	
	SELECT balance INTO current_balance FROM accounts WHERE id = sender_id;
	
	IF (current_balance < 0) THEN
		ROLLBACK;
	END IF;
END;
$$;

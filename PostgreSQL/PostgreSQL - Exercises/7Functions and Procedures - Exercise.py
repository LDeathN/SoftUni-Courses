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

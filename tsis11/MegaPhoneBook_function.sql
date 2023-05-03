
CREATE OR REPLACE PROCEDURE delete_user(who_is_del text)
LANGUAGE plpgsql
AS $$
BEGIN
    DELETE FROM MegaPhoneBook WHERE user_name = who_is_del OR user_surname = who_is_del OR phone_number = who_is_del;
END;
$$;


DROP FUNCTION add_many_users;
CREATE OR REPLACE FUNCTION add_many_users(add_names text[], add_surnames text[], add_numbers text[])
RETURNS text[]
LANGUAGE plpgsql
AS $$
DECLARE
    incor_number text[];
    i integer;
BEGIN
    FOR i IN 1..array_length(add_names, 1) LOOP
        IF ((SUBSTRING(add_numbers[i], 1, 1) = '8' AND LENGTH(add_numbers[i]) = 11) OR (SUBSTRING(add_numbers[i], 1, 2) = '+7' AND LENGTH(add_numbers[i]) = 12)) AND SUBSTRING(add_numbers[i], 2) ~ '^[0-9]+$' THEN
             INSERT INTO MegaPhoneBook VALUES (add_names[i], add_surnames[i], add_numbers[i]);
        ELSE
             incor_number = array_append(incor_number, add_numbers[i]);
        END IF;
    END LOOP;
	return(incor_number);

END;
$$;

CREATE OR REPLACE FUNCTION return_all_same_user(same_res text)
RETURNS TABLE(name_user character varying, surname_user character varying, phone_user character varying) AS $$
BEGIN
    RETURN QUERY SELECT *
                 FROM MegaPhoneBook
                 WHERE user_name ~ same_res OR
                 user_surname ~ same_res OR
                 phone_number ~ same_res;

END;
$$ LANGUAGE plpgsql;

CREATE OR REPLACE PROCEDURE add_or_update_user(new_user text, new_surname text, new_number text)
LANGUAGE plpgsql
AS $$
BEGIN
    IF EXISTS(SELECT * FROM MegaPhoneBook WHERE user_name = new_user AND user_surname = new_surname) THEN
        UPDATE MegaPhoneBook SET phone_number =  new_number WHERE user_name = new_user AND user_surname = new_surname;
    ELSE
        INSERT INTO MegaPhoneBook VALUES (new_user, new_surname, new_number);
    END IF;

END;
$$;

CREATE OR REPLACE FUNCTION get_users_between_rows(start_row integer, number_row integer)
RETURNS TABLE(user_names character varying, user_surnames character varying, phone_numbers character varying) AS $$
BEGIN
    RETURN QUERY SELECT *
                 FROM MegaPhoneBook
                 ORDER BY user_name
                 LIMIT number_row
                 OFFSET start_row - 1;
END;
$$ LANGUAGE plpgsql;

SELECT * FROM MegaPhoneBook;


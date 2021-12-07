DO $$
DECLARE
    country_name country.country_name%type;
BEGIN
    country_name := 'Italy';
    FOR counter IN 111..112
        LOOP
		   INSERT INTO country(country_id, country_name) 
		   VALUES (counter, country_name);
		   country_name := 'Poland';
        END LOOP;
END;
$$
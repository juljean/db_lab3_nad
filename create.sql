CREATE TABLE GeneralType (
  	TYPE_ID char(10)  NOT NULL PRIMARY KEY,
	TYPE_NAME char(256)  NOT NULL
);

CREATE TABLE Country (
  	COUNTRY_ID char(10)  NOT NULL PRIMARY KEY,
	COUNTRY_NAME char(256)  NOT NULL
);


CREATE TABLE Place (
  	PLACE_ID char(10) NOT NULL PRIMARY KEY,
	PLACE_NAME char(256) NOT NULL,
	COUNTRY_ID char(10) NOT NULL,
	CONSTRAINT FK_Country FOREIGN KEY (COUNTRY_ID) 
		REFERENCES Country(COUNTRY_ID)
);


CREATE TABLE AttackPlace (
  	ATTACK_ID char(10) NOT NULL PRIMARY KEY,
	PLACE_NAME char(256) NOT NULL,
	CONSTRAINT FK_PlaceName FOREIGN KEY (PLACE_NAME) 
		REFERENCES Place(PLACE_ID)
);


CREATE TABLE AttackType (
  	ATTACK_ID char(10) NOT NULL PRIMARY KEY,
	TYPE_NAME char(256) NOT NULL,
	CONSTRAINT FK_TypeName FOREIGN KEY (TYPE_NAME) 
		REFERENCES GeneralType(TYPE_ID),
	CONSTRAINT FK_AttackID FOREIGN KEY (ATTACK_ID) 
		REFERENCES AttackPlace(ATTACK_ID)
);


CREATE TABLE AttackDate (
  	ATTACK_ID char(10) NOT NULL PRIMARY KEY,
	ATTACK_DATE date NOT NULL,
	CONSTRAINT FK_AttackID FOREIGN KEY (ATTACK_ID) 
		REFERENCES AttackPlace(ATTACK_ID)
);

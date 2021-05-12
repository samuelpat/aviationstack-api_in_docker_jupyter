#!/bin/bash
set -e
export PGPASSWORD=$POSTGRES_PASSWORD;
psql -v ON_ERROR_STOP=1 --username "$POSTGRES_USER" --dbname "$POSTGRES_DB" <<-EOSQL
  CREATE USER $APP_DB_USER WITH PASSWORD '$APP_DB_PASS';
  CREATE DATABASE $APP_DB_NAME;
  GRANT ALL PRIVILEGES ON DATABASE $APP_DB_NAME TO $APP_DB_USER;
  \connect $APP_DB_NAME $APP_DB_USER
  BEGIN;
    CREATE TABLE IF NOT EXISTS testdata (
	    flightDate date,
	    flightStatus varchar(100),
	    departureAirport varchar(100),
	    departureTimezone varchar(100),
	    arrivalAirport varchar(100),
	    arrivalTimezone varchar(100),
	    arrivalTerminal varchar(100),
	    airlineName varchar(100),
	    flightNumber varchar(100)
	);
	CREATE INDEX idx_flight_date ON testdata (flightDate);
  COMMIT;
EOSQL

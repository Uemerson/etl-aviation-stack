"""
    Module providing a migrate function that
    performs database schema migration.
"""

import psycopg2


def migrate(conn):
    """Perform database schema migration."""
    try:
        conn.autocommit = False
        with conn.cursor() as cursor:
            cursor.execute(
                """
                CREATE TABLE IF NOT EXISTS flights (
                    id UUID PRIMARY KEY DEFAULT gen_random_uuid(),
                    created_at TIMESTAMP DEFAULT NOW(),
                    flight_date DATE,
                    flight_status VARCHAR(50),
                    -- Departure Information
                    departure_airport VARCHAR(100),
                    departure_iata VARCHAR(10),
                    departure_icao VARCHAR(10),
                    departure_delay INT,
                    departure_scheduled TIMESTAMP WITH TIME ZONE,
                    departure_estimated TIMESTAMP WITH TIME ZONE,
                    departure_actual TIMESTAMP WITH TIME ZONE,
                    departure_estimated_runway TIMESTAMP WITH TIME ZONE,
                    departure_actual_runway TIMESTAMP WITH TIME ZONE,
                    -- Arrival Information
                    arrival_airport VARCHAR(100),
                    arrival_iata VARCHAR(10),
                    arrival_icao VARCHAR(10),
                    arrival_delay INT,
                    arrival_scheduled TIMESTAMP WITH TIME ZONE,
                    arrival_estimated TIMESTAMP WITH TIME ZONE,
                    arrival_actual TIMESTAMP WITH TIME ZONE,
                    arrival_estimated_runway TIMESTAMP WITH TIME ZONE,
                    arrival_actual_runway TIMESTAMP WITH TIME ZONE,
                    -- Airline Information
                    airline_name VARCHAR(100),
                    airline_iata VARCHAR(10),
                    airline_icao VARCHAR(10),
                    -- Flight Information
                    flight_number VARCHAR(20),
                    flight_iata VARCHAR(10),
                    flight_icao VARCHAR(10),
                    -- Live Information
                    live_updated TIMESTAMP WITH TIME ZONE,
                    live_latitude FLOAT,
                    live_longitude FLOAT,
                    live_altitude FLOAT,
                    live_direction FLOAT,
                    live_speed_horizontal FLOAT,
                    live_speed_vertical FLOAT,
                    live_is_ground BOOLEAN
                );"""
            )

            conn.commit()
    except psycopg2.Error as err:
        print(err)

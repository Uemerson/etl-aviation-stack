"""Module providing an transformer function for the AviationStack API."""

import psycopg2
import psycopg2.extras
from psycopg2 import sql


def load(conn, transformed_data):
    """The function that runs the AviationStack API transformer."""

    insert_query = sql.SQL(
        """
        INSERT INTO flights (
            flight_date, flight_status,
            departure_airport, departure_iata, departure_icao, 
            departure_delay, departure_scheduled, departure_estimated, 
            departure_actual, departure_estimated_runway,
            departure_actual_runway,

            arrival_airport, arrival_iata, arrival_icao, 
            arrival_delay, arrival_scheduled, arrival_estimated, 
            arrival_actual, arrival_estimated_runway, arrival_actual_runway,
            airline_name, airline_iata, airline_icao,
            flight_number, flight_iata, flight_icao,
            live_updated, live_latitude, live_longitude,
            live_altitude, live_direction, live_speed_horizontal,
            live_speed_vertical, live_is_ground
        ) VALUES (%s, %s, %s, %s, %s, %s, %s, %s, %s, %s, %s, %s, 
                  %s, %s, %s, %s, %s, %s, %s, %s, %s, %s, %s, %s, 
                  %s, %s, %s, %s, %s, %s, %s, %s, %s, %s)
    """
    )
    try:
        conn.autocommit = False
        with conn.cursor() as cursor:
            psycopg2.extras.execute_batch(
                cursor, insert_query, transformed_data
            )
            conn.commit()
    except psycopg2.Error as err:
        print(err)

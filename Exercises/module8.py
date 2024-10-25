import mysql.connector
connection=mysql.connector.connect(
    host='127.0.0.1',
    port=3306,
    database='Relational_database',
    user='olgachit',
    password='OLga123!',
    autocommit=True,
    charset='utf8mb4',
    collation='utf8mb4_general_ci'
    )

# 1 Write a program that asks the user to enter the ICAO code of an airport. The program fetches and prints out the corresponding airport name and location (town) from the airport database used on this course. The ICAO codes are stored in the ident column of the airport table.
def fetch_airport_info(icao_code):
    cursor=connection.cursor()
    query = "SELECT name, municipality FROM airport WHERE ident=%s"
    cursor.execute(query, (icao_code,))
    result = cursor.fetchone()
    cursor.close()
    connection.close()
    return result

icao_code=input("Enter ICAO code: ")
RESULT=fetch_airport_info(icao_code)
print("Airport Name:", RESULT[0])
print("Location:", RESULT[1])

# 2 Write a program that asks the user to enter the area code (for example FI) and prints out the airports located in that country ordered by airport type. For example, Finland has 65 small airports, 15 helicopter airports and so on.
connection=mysql.connector.connect(
    host='127.0.0.1',
    port=3306,
    database='Relational_database',
    user='olgachit',
    password='OLga123!',
    autocommit=True,
    charset='utf8mb4',
    collation='utf8mb4_general_ci'
    )
def fetch_airport_by_local_code(local_code):
    cursor=connection.cursor()
    query = "SELECT name from airport where iso_country=%s order by type"
    cursor.execute(query, (local_code,))
    result = cursor.fetchall()
    cursor.close()
    connection.close()
    return result

local_code=input("Enter area code: ")
RESULT=fetch_airport_by_local_code(local_code)
print("Airports in", local_code)
for result in RESULT:
    print(result)

# 3 Write a program that asks the user to enter the ICAO codes of two airports. The program prints out the distance between the two airports in kilometers. The calculation is based on the airport coordinates fetched from the database. Calculate the distance using the geopy library: https://geopy.readthedocs.io/en/stable/. Install the library by selecting View / Tool Windows / Python Packages in your PyCharm IDE, write geopy into the search field and finish the installation.
import geopy.distance
connection=mysql.connector.connect(
    host='127.0.0.1',
    port=3306,
    database='Relational_database',
    user='olgachit',
    password='OLga123!',
    autocommit=True,
    charset='utf8mb4',
    collation='utf8mb4_general_ci'
    )

dist = None
def fetch_coordinates(icao_code1, icao_code2):
    cursor=connection.cursor()
    query = "SELECT latitude_deg, longitude_deg FROM airport WHERE ident=%s OR ident=%s"
    codes = (icao_code1, icao_code2)
    cursor.execute(query, codes)
    result = cursor.fetchall()
    if len(result) >= 2:
        coord1 = (result[0][0], result[0][1])
        coord2 = (result[1][0], result[1][1])
        dist = geopy.distance.distance(coord1, coord2).kilometers
        print("Distance:", dist, "kilometers")
    else:
        print("Error: Not enough data in result:", result)
    cursor.close()
    connection.close()
    return dist

icao_code1=input("Enter first ICAO code: ")
icao_code2=input("Enter second ICAO code: ")
RESULT=fetch_coordinates(icao_code1, icao_code2)

import psycopg2
from psycopg2 import Error


# -----------------------------------------------------------------------------
# OPEN DATABASE CONNECTION
# -----------------------------------------------------------------------------
def open_connection():
    global connection
    connection = psycopg2.connect(user = "postgres",
                                    password = "example",
                                    host = "db",
                                    port = "5432",
                                    database = "postgres")
    return connection


# -----------------------------------------------------------------------------
# CLOSE DATABASE CONNECTION
# -----------------------------------------------------------------------------
def close_connection(connection, cursor):
    if(connection):
        cursor.close()
        connection.close()
        print("PostgreSQL connection is closed")


# -----------------------------------------------------------------------------
# CREATE DATA OPERATION
# -----------------------------------------------------------------------------
def insert_data(metrics):
    #TODO: This code is vulnerable to SQL Injection OR XSS
    connection = open_connection()
    cursor = connection.cursor()
    print(metrics.tags.time, metrics.tags.host_name)
    cursor.execute("insert into Tags (timestam, hostname) values (%s, %s)", (metrics.tags.time, metrics.tags.host_name))
    cursor.execute("insert into Categories (bots, crypto_mining, ip_scan, ip_dynamic, malware, anonymization, botnets_command_center, spam) values (%s, %s, %s, %s, %s, %s, %s, %s)", (metrics.categories.bots, metrics.categories.crypto_mining, metrics.categories.ip_scan, metrics.categories.ip_dynamic, metrics.categories.malware, metrics.categories.anonymization, metrics.categories.command_center_botnets, metrics.categories.spam))
    cursor.execute("insert into Analysis (ip, score, country) values (%s,%s,%s)", (metrics.ip, metrics.score, metrics.country))
    connection.commit()
    close_connection(connection, cursor)


# -----------------------------------------------------------------------------
# READ DATA OPERATION
# -----------------------------------------------------------------------------
def get_data(ip):
    #TODO: This code is vulnerable to SQL Injection
    query = 'SELECT Analysis.ip, Analysis.score, Analysis.country, Categories.bots, Categories.crypto_mining, Categories.ip_scan, Categories.ip_dynamic, Categories.malware, Categories.anonymization, Categories.botnets_command_center, Categories.spam \
            FROM Analysis \
            LEFT JOIN Categories \
            ON Categories.id_categories=Analysis.id_categories \
            WHERE Analysis.ip = %s;'

    connection = open_connection()
    cursor = connection.cursor()
    cursor.execute(query, (ip,))
    result = cursor.fetchall()
    connection.commit()
    close_connection(connection, cursor)
    return result
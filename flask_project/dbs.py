# import psycopg2
# from psycopg2 import pool
# import os
# try:
#     threaded_pool = psycopg2.pool.ThreadedConnectionPool(5, 20, user=os.environ['DB_USERNAME'],
#                                                                     password=os.environ['DB_PASSWORD'],
#                                                                     host="127.0.0.1",
#                                                                     port="5432",
#                                                                     database="dvdrental")
#     if (threaded_pool):
#         print("Connection pool created successfully using ThreadedConnectionPool")

#     ps_connection = threaded_pool.getconn()

#     if (ps_connection):

#         print("successfully recived connection from connection pool ")
#         ps_cursor = ps_connection.cursor()
#         ps_cursor.execute("***")
#         ps_cursor.close()
#         threaded_pool.putconn(ps_connection)
#         print("Put away a PostgreSQL connection")

# except (Exception, psycopg2.DatabaseError) as error:
#     print("Error while connecting to PostgreSQL", error)

# finally:
#     # closing database connection.
#     # use closeall() method to close all the active connection if you want to turn of the application
#     if threaded_postgreSQL_pool:
#         threaded_postgreSQL_pool.closeall
#     print("Threaded PostgreSQL connection pool is closed")

import psycopg2
from psycopg2 import pool

import os
class Dbconnection:
    
    db_connection=''

    @staticmethod
    def getInstance():
        if not Dbconnection.db_connection:
            db_configuration = {"user":os.environ['DB_USERNAME'],
                "password":os.environ['DB_PASSWORD'],
                "host":"127.0.0.1",
                "port":"5432",
                "database":"dvdrental"
            }
            connection_pool=psycopg2.pool.ThreadedConnectionPool(3, 10, **db_configuration)
            Dbconnection.db_connection=connection_pool
            print("New conn is success", Dbconnection.db_connection)
        else:
            print("Old connection is success", Dbconnection.db_connection)
            # app.logger.info('%s logged in successfully', Dbconnection.db_connection)
        return Dbconnection.db_connection
        

import psycopg2
import config


try: 

    conn = psycopg2.connect(
        dbname = config.DATABASE,
        user = config.USERNAME,
        password = config.PASSWORD,
        host = config.HOSTNAME,
        port = config.PORT
    )

    cursor = conn.cursor()

    # query = '''INSERT INTO actors (first_name, last_name, age, number_oscars)
    #         VALUES ('Hugh', 'Laurie', '1959/06/11', 3)'''

    # cursor.execute(query)
    conn.commit() #adding/changing data in the db
    cursor.execute('SELECT * FROM actors')

    #two method to fetch the data:
    # fetchall() or fetchone()

    # print(cursor.fetchone())

    all_rows = cursor.fetchall() #getting data from db
    for row in all_rows:
        print(row)

except psycopg2.Error as e:
    print('Error connecting', e)

finally:
    if conn:
        cursor.close()
        conn.close()


# EXERCISE:
        # insert into actors table 2 new actors
        # select from table movies all the movies from director Steven Spielberg
        # create a table named movie_reviews (one movie can get many reviews and a review is for one movie) and insert 3 reviews 
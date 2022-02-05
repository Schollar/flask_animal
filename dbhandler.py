import dbcreds
import mariadb as db


class dbInteraction:
    # Connect function that starts a DB connection and creates a cursor
    def db_connect(self):
        conn = None
        cursor = None
        try:
            conn = db.connect(user=dbcreds.user, password=dbcreds.password,
                              host=dbcreds.host, port=dbcreds.port, database=dbcreds.database)
            cursor = conn.cursor()
        except db.OperationalError:
            print('Something is wrong with the DB')
        except:
            print('Something went wrong connecting to the DB')
        return conn, cursor
# Disconnect function that takes in the conn and cursor and attempts to close both

    def db_disconnect(self, conn, cursor):
        try:
            cursor.close()
        except:
            print('Error closing cursor')
        try:
            conn.close()
        except:
            print('Error closing connection')
# Get animal function gets the animal name and description from animals table in DB

    def get_animals(self):
        animals = []
        conn, cursor = self.db_connect()
        try:
            cursor.execute(
                "SELECT name, description FROM animals")
            animals = cursor.fetchall()
        except db.OperationalError:
            print('Something is wrong with the db!')
        except db.ProgrammingError:
            print('Error running DB query')
        self.db_disconnect(conn, cursor)

        return animals
# Add animal runs an INSERT query to insert animal into DB, using the args passed to it through prepared statment.

    def add_animal(self, animal_name, animal_desc):
        conn, cursor = self.db_connect()
        try:
            cursor.execute(
                "INSERT INTO animals (name, description) VALUES (?, ?)", [animal_name, animal_desc])

        except db.OperationalError:
            print('Something is wrong with the db!')
        except db.ProgrammingError:
            print('Error running DB query')
        conn.commit()
        self.db_disconnect(conn, cursor)
        return True
# Change animal runs an UPDATE query to update an animal in the DB, using the args passed to it through prepared statment.

    def change_animal(self, animal_name, new_name, new_description):
        conn, cursor = self.db_connect()
        try:
            cursor.execute(
                "UPDATE animals SET name = ?, description = ? WHERE name = ?", [new_name, new_description, animal_name])
        except db.OperationalError:
            print('Something is wrong with the db!')
            return False
        except db.ProgrammingError:
            print('Error running DB query')
        conn.commit()
        self.db_disconnect(conn, cursor)
        return True
# Delete animal runs an DELETE query to delete an animal from the DB, using the arg passed to it through prepared statment.

    def delete_animal(self, animal_name):
        conn, cursor = self.db_connect()
        try:
            cursor.execute(
                "DELETE FROM animals WHERE name = ?", [animal_name, ])
        except db.OperationalError:
            print('Something is wrong with the db!')
        except db.ProgrammingError:
            print('Error running DB query')
        conn.commit()
        self.db_disconnect(conn, cursor)
        return True

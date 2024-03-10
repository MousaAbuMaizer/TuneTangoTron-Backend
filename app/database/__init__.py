from database.database import SqlAlchemyDatabaseConnection
from database.models import *
from database.cruds.user_crud import UserCRUD
from database.cruds.saved_files_crud import SavedFileCRUD

# Initialize the database connection
database_url = "mysql+mysqlconnector://user:password@localhost:3306/tunetangotron"
sql_database_connection = SqlAlchemyDatabaseConnection(database_url)

# Create the database tables
sql_database_connection.Base.metadata.create_all(sql_database_connection.engine)
sql_database_connection.metadata.reflect(bind=sql_database_connection.engine)


user_crud_sql_instance = UserCRUD(sql_database_connection)
saved_file_crud_sql_instance = SavedFileCRUD(sql_database_connection)


# Check if there are no users in the database
if (sql_database_connection.get_session().query(User).count() == 0):
    # Create a UserCRUD instance
    USER_CRUD = UserCRUD(sql_database_connection)
    
    # Add a user to the database
    # hash password to ease testing ( password is '1234' )
    USER_CRUD.add("hamza","03ac674216f3e15c761ee1a5e255f067953623c8b388b4459e13f978d7c846f4")

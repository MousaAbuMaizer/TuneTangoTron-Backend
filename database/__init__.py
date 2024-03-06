from database.database import SqlAlchemyDatabaseConnection
from database.models import *
from database.cruds.user_crud import UserCRUD

# Initialize the database connection
database_url = "mysql+mysqlconnector://user:password@localhost:3306/tunetangotron"
sql_database_connection = SqlAlchemyDatabaseConnection(database_url)

# Create the database tables
sql_database_connection.Base.metadata.create_all(sql_database_connection.engine)
sql_database_connection.metadata.reflect(bind=sql_database_connection.engine)

# Check if there are no users in the database
if (sql_database_connection.get_session().query(User).count() == 0):
    # Create a UserCRUD instance
    USER_CRUD = UserCRUD(sql_database_connection)
    
    # Add a user to the database
    USER_CRUD.add("hamza","1234")

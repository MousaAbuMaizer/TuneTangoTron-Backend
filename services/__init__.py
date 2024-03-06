from services.login_service import LoginService
from database import user_crud_sql_instance 

login_service_instance = LoginService(user_crud_sql_instance)

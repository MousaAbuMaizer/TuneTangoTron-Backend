from services.login_service import LoginService
from services.uploading_file_service import AzureBlobUploader
from database import user_crud_sql_instance 

login_service_instance = LoginService(user_crud_sql_instance)
azure_blob_uloader_instance = AzureBlobUploader()
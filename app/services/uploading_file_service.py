import io
from azure.storage.blob import BlobServiceClient
from config import AZURE_BLOB_CONN, AZURE_BLOB_CONTAINER_NAME

class AzureBlobUploader:
    def __init__(self):
        connect_str = AZURE_BLOB_CONN
        if not connect_str:
            raise ValueError("Azure Storage connection string not found in environment variables.")

        self.blob_service_client = BlobServiceClient.from_connection_string(connect_str)
        self.container_name = AZURE_BLOB_CONTAINER_NAME

    def upload_files(self, path, content):
        blob_client = self.blob_service_client.get_blob_client(container=self.container_name, blob=path)
        blob_client.upload_blob(io.BytesIO(content))
        print(f"File '{path}' uploaded to container '{self.container_name}'.")
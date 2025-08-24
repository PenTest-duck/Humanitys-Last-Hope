import weaviate
from weaviate.classes.init import Auth
import os
from dotenv import load_dotenv

load_dotenv()

WEAVIATE_URL = os.getenv("WEAVIATE_URL")
WEAVIATE_KEY = os.getenv("WEAVIATE_KEY")

client = weaviate.connect_to_weaviate_cloud(
    cluster_url=WEAVIATE_URL,
    auth_credentials=Auth.api_key(WEAVIATE_KEY),
    skip_init_checks=True,
)

print(f"Weaviate client is ready: {client.is_ready()}")

client.close()
# Import necessary modules from Elasticsearch and Requests for authentication
from elasticsearch import Elasticsearch
from requests.auth import HTTPBasicAuth

# Define Elasticsearch connection details
es_host = 'https://:9200'  # The Elasticsearch host URL (replace with actual URL)
es_user = ''               # Elasticsearch username (replace with actual user)
es_password = ''           # Elasticsearch password (replace with actual password)
repository_name = ''       # The name of the snapshot repository

# Initialize the Elasticsearch client with the provided credentials and settings
es = Elasticsearch(
    [es_host],
    basic_auth=(es_user, es_password),
    verify_certs=False,     # Disables certificate verification (not recommended for production)
    request_timeout=120     # Sets a timeout of 120 seconds for requests
)

# Retrieve all snapshots from the specified repository
snapshots = es.snapshot.get(repository=repository_name, snapshot='_all')
snapshot_names = [snapshot['snapshot'] for snapshot in snapshots['snapshots']]

# Loop through each snapshot and attempt to delete it
for snapshot_name in snapshot_names:
    try:
        # Delete the current snapshot
        es.snapshot.delete(repository=repository_name, snapshot=snapshot_name)
        print(f"Snapshot '{snapshot_name}' deleted successfully.")
    except Exception as e:
        # Handle errors that occur during deletion
        print(f"Error deleting snapshot '{snapshot_name}': {e}")

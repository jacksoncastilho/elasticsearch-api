# Elasticsearch Snapshot Deletion Script

This script is designed to connect to an Elasticsearch cluster, retrieve all snapshots from a specified repository, and delete them. It's useful for managing storage and maintaining your Elasticsearch repository by removing old or unnecessary snapshots.

## Requirements

- Python 3.6+
- Elasticsearch Python client
- Requests module for HTTP authentication

## Installation

1. Clone the repository:

   ```bash
   git clone https://github.com/yourusername/elasticsearch-api.git
   ```

2. Navigate to the project directory:

   ```bash
   cd elasticsearch-api
   ```

3. Install the required Python packages:

   ```bash
   pip install elasticsearch requests
   ```

## Configuration

Before running the script, you need to configure your Elasticsearch connection details:

1. Open the script file (`deleteallsnapshots.py`).
2. Update the following variables with your Elasticsearch information:
   - `es_host`: The Elasticsearch host URL (e.g., `https://your-elasticsearch-host:9200`).
   - `es_user`: Your Elasticsearch username.
   - `es_password`: Your Elasticsearch password.
   - `repository_name`: The name of the snapshot repository you want to manage.

## Usage

Run the script using the following command:

```bash
python deleteallsnapshots.py
```

## Important Notes

- The script disables SSL certificate verification (`verify_certs=False`). This is convenient for testing or non-production environments but **not recommended** for production use.
- Ensure you have sufficient permissions to access and delete snapshots in the specified repository.

## License

This project is licensed under the MIT License - see the [LICENSE](LICENSE) file for details.

from elasticsearch import Elasticsearch
from requests.auth import HTTPBasicAuth

es_host = 'https://:9200'
es_user = ''
es_password = ''
repository_name = ''

es = Elasticsearch(
    [es_host],
    basic_auth=(es_user, es_password),
    verify_certs=False,
    request_timeout=120
)

snapshots = es.snapshot.get(repository=repository_name, snapshot='_all')
snapshot_names = [snapshot['snapshot'] for snapshot in snapshots['snapshots']]

for snapshot_name in snapshot_names:
    try:
        es.snapshot.delete(repository=repository_name, snapshot=snapshot_name)
        print(f"Snapshot '{snapshot_name}' deletada com sucesso.")
    except Exception as e:
        print(f"Erro ao deletar a snapshot '{snapshot_name}': {e}")

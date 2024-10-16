SIMPLE_SETTINGS = {
    'OVERRIDE_BY_ENV': True,
    'CONFIGURE_LOGGING': True,
    'REQUIRED_SETTINGS': ('KAFKA_BOOTSTRAP_SERVER','MEMGRAPH_URL', 'INPUT_TOPIC'),
}

KAFKA_BOOTSTRAP_SERVER = "kafka:29092"
MEMGRAPH_URL = "bolt://memgraph:7687"

INPUT_TOPIC = "input_topic"
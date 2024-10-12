from faust import Record, App, Stream
from simple_settings import settings
from neo4j import GraphDatabase
from typing import List

class GraphUpdate(Record, serializer='json'):
    nodes: List
    edges: List

app = App(
    'graph-streaming-framework',
    broker=settings.KAFKA_BOOTSTRAP_SERVER,
    value_serializer='json',
)

input_topic = app.topic(settings.INPUT_TOPIC, value_type=GraphUpdate)

@app.agent(input_topic)
async def graph_controller(graph_data_source : Stream[GraphUpdate]):
    async for graph_data in graph_data_source:
        with GraphDatabase.driver(settings.MEMGRAPH_URL, auth=("", "")) as client:
            client.verify_connectivity()

            records, summary, keys = client.execute_query(
                "CREATE (n:Nodes {id: $id}) RETURN n.id AS id;",
                id=graph_data.nodes[0],
                database_="memgraph",
            )
            
            print(records, summary, keys)
            
            records, summary, keys = client.execute_query(
                "CREATE (n:Nodes {id: $id}) RETURN n.id AS id;",
                id=graph_data.nodes[1],
                database_="memgraph",
            )
            
            print(records, summary, keys)
            
            records, summary, keys = client.execute_query(
                f"MATCH (k:Nodes),(t:Nodes) WHERE k.id = {graph_data.nodes[0]} AND t.id = {graph_data.nodes[1]} CREATE (k)-[:IS_IN]->(t);",
                database_="memgraph",
            )
            
            print(records, summary, keys)

if __name__ == "__main__":
    app.main()
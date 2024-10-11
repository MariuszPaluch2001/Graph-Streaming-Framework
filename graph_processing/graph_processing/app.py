import faust
from simple_settings import settings

app = faust.App(
    'hello-world',
    broker=settings.KAFKA_BOOTSTRAP_SERVER,
    value_serializer='raw',
)

greetings_topic = app.topic('greetings')

@app.agent(greetings_topic)
async def greet(greetings):
    async for greeting in greetings:
        print(greeting)

if __name__ == "__main__":
    print("RUN")
    app.main()
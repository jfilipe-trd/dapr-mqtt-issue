from uvicorn import Config, Server
from fastapi import FastAPI

app = FastAPI()


@app.get("/dapr/subscribe")
async def subscribe():
    subscriptions = [
        {
            "pubsubname": "mqtt-pubsub",
            "topic": "device/endpoint1",
            "route": "/device/endpoint1",
        },
        {
            "pubsubname": "mqtt-pubsub",
            "topic": "device/endpoint2",
            "route": "/device/endpoint2",
        },
    ]
    return subscriptions


@app.post(
    "/device/endpoint1",
    status_code=201,
)
async def endpoint1():
    print("Started endpoint1")


@app.post(
    "/device/endpoint2",
    status_code=201,
)
async def endpoint2():
    print("Started endpoint2")


if __name__ == "__main__":
    config = Config(app=app, port=3003, host="0.0.0.0")
    server = Server(config)
    server.run()

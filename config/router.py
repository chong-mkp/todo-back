import channels
from channels.auth import AuthMiddlewareStack
from django.urls import path
from todo.schemas import schema
from channels.routing import ProtocolTypeRouter, URLRouter
from channels_graphql_ws import GraphqlWsConsumer


def demo_middleware(next_middleware, root, info, *args, **kwds):
	if (
		info.operation.name is not None
		and info.operation.name.value != "IntrospectionQuery"
	):
		print("Demo middleware report")
		print("    operation :", info.operation.operation)
		print("    name      :", info.operation.name.value)

	return next_middleware(root, info, *args, **kwds)


class MyGraphqlWsConsumer(GraphqlWsConsumer):
	async def on_connect(self, payload):
		print('\n****on connecting...')
		self.scope["user"] = await channels.auth.get_user(self.scope)

	schema =schema
	middleware = [demo_middleware]


application = ProtocolTypeRouter({
    "websocket":AuthMiddlewareStack(URLRouter([
        path("graphql/", MyGraphqlWsConsumer.as_asgi()),
    ]))
})

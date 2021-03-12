#-*- coding:utf-8 -*-

from graphene import ObjectType, String, Schema
from fastapi import FastAPI
from starlette.graphql import GraphQLApp


class Query(ObjectType):
    hello = String(name=String(default_value="stranger"))
    goodbye = String()

    def resolve_hello(self, info,name):
        return "Hello " + name + " !"

    def resolve_goodbye(self, info):
        return 'See ya!!'


app = FastAPI(title='ContactQL', description='GraphQL Contact APIs', version='0.1')

@app.get("/")
async def root():
    return {"message": "Contact Applications!"}

app.add_route("/graphql", GraphQLApp(schema=Schema(query=Query)))

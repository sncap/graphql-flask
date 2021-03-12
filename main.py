#-*- coding:utf-8 -*-

from graphene import ObjectType, String, Schema, Field
from fastapi import FastAPI
from starlette.graphql import GraphQLApp

class Person(ObjectType):
    first_name = String()
    last_name = String()
    full_name = String()

    def resolve_full_name(self, info):
        return f"{self.first_name} {self.last_name}"


class Query(ObjectType):
    hello = String(name=String(default_value="stranger"))
    goodbye = String()
    me = Field(Person)

    def resolve_hello(self, info,name):
        return "Hello " + name + " !"

    def resolve_goodbye(self, info):
        return 'See ya!!'

    def resolve_me(self, info):
        # returns an object that represents a Person
        return {"first_name": "Luke", "last_name": "Skywalker"}

app = FastAPI(title='ContactQL', description='GraphQL Contact APIs', version='0.1', debug=True)

@app.get("/")
async def root():
    return {"message": "Contact Applications!"}

app.add_route("/graphql", GraphQLApp(schema=Schema(query=Query)))

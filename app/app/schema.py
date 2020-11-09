import graphene
from graphene import ObjectType, Field, List, String
from graphene_sqlalchemy import SQLAlchemyObjectType, SQLAlchemyConnectionField
from .models.user import User as UserModel


class User(SQLAlchemyObjectType):
    class Meta:
        model = UserModel


class Query(ObjectType):
    login = Field(User,
                  user_id=String(),
                  user_pw=String())
    users = List(User)

    @staticmethod
    def resolve_login(self, info, **kwargs):
        uid = kwargs.get('user_id')
        upw = kwargs.get('user_pw')
        query = User.get_query(info)
        return query.all()

    @staticmethod
    def resolve_users(self, info):
        query = User.get_query(info)
        return query.all()


schema = graphene.Schema(query=Query)

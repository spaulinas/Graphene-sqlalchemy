from models import Department as DepartmentModel
from models import Employee as EmployeeModel
from models import Role as RoleModel

import graphene
from graphene import relay
from graphene_sqlalchemy import SQLAlchemyConnectionField, SQLAlchemyObjectType


class Department(SQLAlchemyObjectType):
    class Meta:
        model = ClassModel
        interfaces = (relay.Node, )


class Student(SQLAlchemyObjectType):
    class Meta:
        model = StudentModel
        interfaces = (relay.Node, )


class Role(SQLAlchemyObjectType):
    class Meta:
        model = RoleModel
        interfaces = (relay.Node, )


class Query(graphene.ObjectType):
    node = relay.Node.Field()
    # Allow only single column sorting
    all_students = SQLAlchemyConnectionField(
        Student.connection, sort=Student.sort_argument())
    # Allows sorting over multiple columns, by default over the primary key
    all_roles = SQLAlchemyConnectionField(Role.connection)
    # Disable sorting over this field
    all_class = SQLAlchemyConnectionField(Class.connection, sort=None)


schema = graphene.Schema(query=Query)

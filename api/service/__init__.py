from ariadne import load_schema_from_path, make_executable_schema
from ariadne import QueryType, MutationType
from .queries import get_leads_resolver
from .mutations import create_leadgenForm_resolver

type_defs = load_schema_from_path('./schema.graphql')

query = QueryType()
query.set_field('get_leads', get_leads_resolver)
mutation = MutationType()
query.set_field('create_leadgenForm', create_leadgenForm_resolver)

schema = make_executable_schema(type_defs, query, mutation)

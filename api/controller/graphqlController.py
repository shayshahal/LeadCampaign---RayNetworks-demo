from flask import request, jsonify, Blueprint
from ariadne import graphql_sync
from ariadne.explorer import ExplorerGraphiQL
from api.service import schema

explorer_html = ExplorerGraphiQL().html(None)
graphql_blueprint = Blueprint('graphql', __name__)


@graphql_blueprint.route("/graphql", methods=["GET"])
def graphql_explorer():
    # On GET request serve the GraphQL explorer.
    # You don't have to provide the explorer if you don't want to
    # but keep on mind this will not prohibit clients from
    # exploring your API using desktop GraphQL explorer app.
    return explorer_html, 200


@graphql_blueprint.route("/graphql", methods=["POST"])
def graphql_server():
    # GraphQL queries are always sent as POST
    data = request.get_json()

    # Note: Passing the request to the context is optional.
    # In Flask, the current request is always accessible as flask.request
    success, result = graphql_sync(
        schema,
        data,
        context_value={"request": request})

    status_code = 200 if success else 400
    return jsonify(result), status_code

from GraphQLCompiler import GraphQLCompiler
from django.test.client import MULTIPART_CONTENT
from graphene_django.utils.testing import GraphQLTestCase
import json

class GraphQLFileTestCase(GraphQLTestCase):
    def query(self, query, input_data=None, op_name=None):
        """
        Args:
            query (string)    - GraphQL query to run
            op_name (string)  - If the query is a mutation or named query, you must
                                supply the op_name.  For annon queries ("{ ... }"),
                                should be None (default).
            input_data (dict) - If provided, the $input variable in GraphQL will be set
                                to this value
        Returns:
            Response object from client
        """
        aggregator = GraphQLCompiler(input_data)
        data = {}
        body = {
            "query": query,
            "variables": aggregator.get_variables(),
        }

        if op_name:
            body["operation_name"] = op_name

        if aggregator.converters:
            data['map'] = json.dumps(aggregator.get_map())
            data.update(aggregator.get_file_data())
            data['operations'] = json.dumps(body)
            resp = self._client.post(self.GRAPHQL_URL, data, content_type=MULTIPART_CONTENT)
        else:
            resp = self._client.post(self.GRAPHQL_URL, 
                json.dumps(body), 
                content_type='application/json'
            )

        return resp


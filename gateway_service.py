import json

from nameko.web.handlers import http
from werkzeug.wrappers import Response
from nameko.rpc import RpcProxy

from itertools import permutations
from itertools import combinations

from session import SessionProvider

class GatewayService:

    name = "gateway_service"

    user_access_rpc = RpcProxy('user_access_service')

    session_provider = SessionProvider()

    @http('POST', '/register')
    def add_user(self, request):
        data = request.json
        result = self.user_access_rpc.add_user(data['userAccount'], data['userPassword'])
        return result
    
    @http('POST', '/login')
    def get_user(self, request):
        data = request.json
        result = self.user_access_rpc.get_user(data['userAccount'], data['userPassword'])
        response = ""
        if result:
            session_id = self.session_provider.set_session(result)
            response = Response(str(result))
            response.set_cookie('sessionId', session_id)
            return response
        else:
            return response + "Invalid Login"

    @http('POST', '/logout')
    def logout(self, request):
        cookies = request.cookies
        if cookies:
            session_data = self.session_provider.delete_session(cookies['sessionId'])
            response = Response('Logged Out Successfully')
            return response
        else:
            response = Response('Bad Request')
            return response

    @http('POST', '/combinations')
    def combinations(self, request):
        cookies = request.cookies
        if cookies:
            data = request.json
            storeCombinations = combinations(data['input'], data['size']) 
            result = [' '.join(i) for i in storeCombinations]
            return json.dumps(result)
        else:
            response = Response('You Will Need To Login First')
            return response

    @http('POST', '/permutations')
    def permutations(self, request):
        cookies = request.cookies
        if cookies:
            data = request.json
            storePermutations = permutations(data['input'])
            result = [', '.join(i) for i in storePermutations]
            return json.dumps(result)
        else:
            response = Response('You Will Need To Login First')
            return response
            
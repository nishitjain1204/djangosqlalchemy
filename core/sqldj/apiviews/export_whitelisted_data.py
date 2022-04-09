from rest_framework.views import APIView
from rest_framework.response import Response
from sqldj.helpers.function_helpers import export_whitelisted_data , write_whitelisted_data

class FetchWhiteListedData(APIView):
    
    def get(self, request):
        print(request.query_params)
        id = request.query_params.get('id')
        code = request.query_params.get('code')
        pan_number = request.query_params.get('pan_number')
        is_active = request.query_params.get('is_active') 
        response = export_whitelisted_data(id=id , code=code , pan_number=pan_number,is_active=is_active)
        return response
    
    

class PostWhiteListedData(APIView):
    def post(self,request):
            # print(request.query_params)
            code = request.query_params.get('code')
            print(code)
            pan_number = request.query_params.get('pan_number')
            is_active = request.query_params.get('is_active') 
            response  = write_whitelisted_data(code=code ,pan_number=pan_number,is_active=is_active)
            return response
        
    
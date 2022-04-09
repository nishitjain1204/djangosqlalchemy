from rest_framework import status
from rest_framework.response import Response
from sqldj.helpers.query_helper import fetch_whitelisted_data , create_whitelisted_data

def export_whitelisted_data(
    id = None,
    code = None,
    pan_number = None,
    is_active = None 
):
    try:
        whitelisted_data = fetch_whitelisted_data(
            id = id,
            code = code,
            pan_number = pan_number,
            is_active = is_active 
        )
        if not whitelisted_data:
            return Response(
                {
                    "success" : False,
                    "status_code":status.HTTP_400_BAD_REQUEST,
                    "message" : 'data not found'
                },
                status=status.HTTP_400_BAD_REQUEST
            )
        else:
            return Response(
                {
                    "success" : True,
                    "status_code":status.HTTP_200_OK,
                    "data" : whitelisted_data
                },
                status=status.HTTP_200_OK
            ) 
    except Exception as e :
        logger.error('export whitelisted data - ' , e)

def write_whitelisted_data(code = None , pan_number= None , is_active =None):
    data = {}
    if  code and pan_number and is_active :
        data['code'] = code
        data['pan_number'] = pan_number
        data['is_active'] = is_active
        is_data_written = create_whitelisted_data(data)
        if is_data_written:
            return Response(
                {
                    "success" : True,
                    "status_code":status.HTTP_200_OK,
                },
                status=status.HTTP_200_OK
            ) 
        else:
            return Response (
                {
                    "success" : False,
                    "status_code":status.HTTP_400_BAD_REQUEST,
                    "message" : 'Bad data'
                },
                status=status.HTTP_400_BAD_REQUEST
            )
    else:
        return Response (
                {
                    "success" : False,
                    "status_code":status.HTTP_400_BAD_REQUEST,
                    "message" : 'Data incomplete'
                },
                status=status.HTTP_400_BAD_REQUEST
                )
        
            
            
            
        
        
            
        
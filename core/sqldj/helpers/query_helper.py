from sqlalchemy import exc, update
from sqldj.models import (GqInternalWhitelistedPan , GqInternalBlacklistedPan)
import logging

from django.conf import settings

session = settings.DB_SESSION


def fetch_whitelisted_data(
    id = None,
    code = None,
    pan_number = None,
    is_active = None 
):
    try:
        request_data = session.query(
            GqInternalWhitelistedPan.id,
            GqInternalWhitelistedPan.code,
            GqInternalWhitelistedPan.pan_number,
            GqInternalWhitelistedPan.is_active,
            GqInternalWhitelistedPan.created_on,
            GqInternalWhitelistedPan.updated_on,
            GqInternalWhitelistedPan.deleted_on)
        
        if id:
            request_data = request_data.filter(
                GqInternalWhitelistedPan.id == id
            )
        if code:
            request_data = request_data.filter(
                GqInternalWhitelistedPan.code == code
            )
        if pan_number:
            request_data = request_data.filter(
                GqInternalWhitelistedPan.pan_number == pan_number
            )
        if is_active:
            request_data = request_data.filter(
                GqInternalWhitelistedPan.is_active == is_active
            )
        
        request_data = request_data.all()
        session.commit()
        serializer = [ row._asdict() for row in request_data ]
    except Exception as e:
        logger.error('Fetch whitelisted data - ' , e)
        session.rollback()
        serializer = None
    
    return serializer

def create_whitelisted_data(data=None):
    try:
        if data:
            print(data)
            add_white_listed_data = GqInternalWhitelistedPan(**data)
            session.add(add_white_listed_data)
            session.commit()
            return True
        else:
            return False
    
    except Exception as e:
        session.rollback()
        logger.error('create whitelisted data - ' , e)
        return False
    
    
    
    
        
        
        
        
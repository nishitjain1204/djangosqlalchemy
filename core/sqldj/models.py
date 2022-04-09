from sqlalchemy import Column, Integer, String, TIMESTAMP, text
from sqlalchemy.ext.declarative import declarative_base

Base = declarative_base()
metadata = Base.metadata


class GqInternalBlacklistedPan(Base):
    __tablename__ = 'gq_internal_blacklisted_pan'

    id = Column(Integer, primary_key=True)
    code = Column(String(200), nullable=False, index=True)
    pan_number = Column(String(200), nullable=False, index=True)
    is_active = Column(Integer, nullable=False, index=True)
    created_on = Column(TIMESTAMP, nullable=False, server_default=text("CURRENT_TIMESTAMP"))
    updated_on = Column(TIMESTAMP, nullable=False, server_default=text("CURRENT_TIMESTAMP ON UPDATE CURRENT_TIMESTAMP"))
    deleted_on = Column(TIMESTAMP)


class GqInternalWhitelistedPan(Base):
    __tablename__ = 'gq_internal_whitelisted_pan'

    id = Column(Integer, primary_key=True)
    code = Column(String(200), nullable=False, index=True)
    pan_number = Column(String(200), nullable=False, index=True)
    is_active = Column(Integer, nullable=False, index=True)
    created_on = Column(TIMESTAMP, nullable=False, server_default=text("CURRENT_TIMESTAMP"))
    updated_on = Column(TIMESTAMP, nullable=False, server_default=text("CURRENT_TIMESTAMP ON UPDATE CURRENT_TIMESTAMP"))
    deleted_on = Column(TIMESTAMP)





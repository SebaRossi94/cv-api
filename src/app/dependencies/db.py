from fastapi import Depends
from app.db import get_session, get_session_no_transaction

session_dependency = Depends(get_session)
session_no_transaction_dependency = Depends(get_session_no_transaction)

from app.dao.base import BaseDAO
from app.authors.models import Author



class AuthorDAO(BaseDAO):
    model = Author
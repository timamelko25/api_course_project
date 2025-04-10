from fastapi import HTTPException, status, Depends

from app.auth_users.models import User
from app.auth_users.dependencies import get_current_user
from app.roles import Role


async def is_authorized_student(user: User = Depends(get_current_user)) -> User:
    if not user.user_role == Role.STUDENT:
        raise HTTPException(status_code=status.HTTP_401_UNAUTHORIZED, 
                            detail='User is not a student')
    return user
    
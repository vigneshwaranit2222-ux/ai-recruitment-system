from datetime import UTC, datetime, timedelta
from uuid import UUID

import jwt
from pwdlib import PasswordHash

from app.core.config import get_settings

password_hash = PasswordHash.recommended()


def hash_password(password: str) -> str:
    return password_hash.hash(password)


def verify_password(password: str, encoded: str) -> bool:
    return password_hash.verify(password, encoded)


def create_token(subject: UUID, tenant_id: UUID | None, token_type: str, expires: timedelta) -> str:
    now = datetime.now(UTC)
    settings = get_settings()
    return jwt.encode({"sub": str(subject), "tenant_id": str(tenant_id) if tenant_id else None, "type": token_type, "iat": now, "exp": now + expires}, settings.jwt_secret_key, algorithm=settings.jwt_algorithm)

"""Production data model. Every business aggregate is tenant scoped."""
from __future__ import annotations
from datetime import datetime
from enum import StrEnum
from uuid import UUID, uuid4
from sqlalchemy import Boolean, DateTime, Float, ForeignKey, Integer, JSON, MetaData, String, Text, UniqueConstraint, Uuid, func
from sqlalchemy.orm import DeclarativeBase, Mapped, mapped_column


class Base(DeclarativeBase):
    metadata = MetaData(naming_convention={"ix": "ix_%(column_0_label)s", "uq": "uq_%(table_name)s_%(column_0_name)s", "fk": "fk_%(table_name)s_%(column_0_name)s_%(referred_table_name)s"})


class Audit:
    id: Mapped[UUID] = mapped_column(Uuid, primary_key=True, default=uuid4)
    created_at: Mapped[datetime] = mapped_column(DateTime(timezone=True), server_default=func.now())
    updated_at: Mapped[datetime] = mapped_column(DateTime(timezone=True), server_default=func.now(), onupdate=func.now())
    deleted_at: Mapped[datetime | None] = mapped_column(DateTime(timezone=True))
    created_by: Mapped[UUID | None] = mapped_column(Uuid)


class Scoped(Audit):
    tenant_id: Mapped[UUID] = mapped_column(ForeignKey("tenants.id"), index=True)


class RoleName(StrEnum):
    SUPER_ADMIN="SUPER_ADMIN"; TENANT_ADMIN="TENANT_ADMIN"; HR="HR"; INTERVIEWER="INTERVIEWER"; STUDENT="STUDENT"; FRESHER="FRESHER"; INTERN="INTERN"; EXPERIENCED_CANDIDATE="EXPERIENCED_CANDIDATE"


class Tenant(Base, Audit):
    __tablename__="tenants"; slug: Mapped[str]=mapped_column(String(80), unique=True, index=True); name: Mapped[str]=mapped_column(String(200)); is_active: Mapped[bool]=mapped_column(Boolean, default=True)
class User(Base, Scoped):
    __tablename__="users"; email: Mapped[str]=mapped_column(String(320), unique=True, index=True); password_hash: Mapped[str]=mapped_column(String(255)); full_name: Mapped[str]=mapped_column(String(200)); is_active: Mapped[bool]=mapped_column(Boolean, default=True); email_verified_at: Mapped[datetime|None]=mapped_column(DateTime(timezone=True))
class Role(Base, Audit):
    __tablename__="roles"; name: Mapped[str]=mapped_column(String(64), unique=True)
class Permission(Base, Audit):
    __tablename__="permissions"; code: Mapped[str]=mapped_column(String(100), unique=True)
class UserRole(Base, Audit):
    __tablename__="user_roles"; __table_args__=(UniqueConstraint("user_id","role_id"),); user_id: Mapped[UUID]=mapped_column(ForeignKey("users.id"), index=True); role_id: Mapped[UUID]=mapped_column(ForeignKey("roles.id"), index=True)
class Company(Base, Scoped):
    __tablename__="companies"; name: Mapped[str]=mapped_column(String(200)); website: Mapped[str|None]=mapped_column(String(500))
class CandidateProfile(Base, Scoped):
    __tablename__="candidate_profiles"; user_id: Mapped[UUID|None]=mapped_column(ForeignKey("users.id"), unique=True); candidate_type: Mapped[str]=mapped_column(String(40)); skills: Mapped[list[str]]=mapped_column(JSON, default=list); years_experience: Mapped[float]=mapped_column(Float, default=0); location: Mapped[str|None]=mapped_column(String(120)); salary_expectation: Mapped[int|None]=mapped_column(Integer); availability_date: Mapped[datetime|None]=mapped_column(DateTime(timezone=True))
class Resume(Base, Scoped):
    __tablename__="resumes"; candidate_id: Mapped[UUID]=mapped_column(ForeignKey("candidate_profiles.id"), index=True); storage_key: Mapped[str]=mapped_column(String(500)); raw_text: Mapped[str|None]=mapped_column(Text); parsed_data: Mapped[dict]=mapped_column(JSON, default=dict); processing_status: Mapped[str]=mapped_column(String(30), default="PENDING")
class Job(Base, Scoped):
    __tablename__="jobs"; company_id: Mapped[UUID]=mapped_column(ForeignKey("companies.id"), index=True); title: Mapped[str]=mapped_column(String(200)); description: Mapped[str]=mapped_column(Text); min_experience: Mapped[float]=mapped_column(Float, default=0); employment_type: Mapped[str]=mapped_column(String(50)); location: Mapped[str|None]=mapped_column(String(120)); max_salary: Mapped[int|None]=mapped_column(Integer)
class JobSkill(Base, Scoped):
    __tablename__="job_skills"; __table_args__=(UniqueConstraint("job_id","name"),); job_id: Mapped[UUID]=mapped_column(ForeignKey("jobs.id"), index=True); name: Mapped[str]=mapped_column(String(100)); required: Mapped[bool]=mapped_column(Boolean, default=True)
class Application(Base, Scoped):
    __tablename__="applications"; __table_args__=(UniqueConstraint("job_id","candidate_id"),); job_id: Mapped[UUID]=mapped_column(ForeignKey("jobs.id")); candidate_id: Mapped[UUID]=mapped_column(ForeignKey("candidate_profiles.id")); status: Mapped[str]=mapped_column(String(40), default="APPLIED")
class Interview(Base, Scoped):
    __tablename__="interviews"; application_id: Mapped[UUID]=mapped_column(ForeignKey("applications.id")); interviewer_id: Mapped[UUID]=mapped_column(ForeignKey("users.id")); scheduled_at: Mapped[datetime]=mapped_column(DateTime(timezone=True)); status: Mapped[str]=mapped_column(String(40))
class InterviewFeedback(Base, Scoped):
    __tablename__="interview_feedback"; interview_id: Mapped[UUID]=mapped_column(ForeignKey("interviews.id")); score: Mapped[float]=mapped_column(Float); communication_score: Mapped[float]=mapped_column(Float); feedback: Mapped[str]=mapped_column(Text)
class Recommendation(Base, Scoped):
    __tablename__="recommendations"; __table_args__=(UniqueConstraint("job_id","candidate_id"),); job_id: Mapped[UUID]=mapped_column(ForeignKey("jobs.id")); candidate_id: Mapped[UUID]=mapped_column(ForeignKey("candidate_profiles.id")); final_score: Mapped[float]=mapped_column(Float); explanation: Mapped[str|None]=mapped_column(Text); score_breakdown: Mapped[dict]=mapped_column(JSON, default=dict)
class VectorEmbedding(Base, Scoped):
    __tablename__="vector_embeddings"; __table_args__=(UniqueConstraint("entity_type","entity_id"),); entity_type: Mapped[str]=mapped_column(String(50)); entity_id: Mapped[UUID]=mapped_column(Uuid); chroma_document_id: Mapped[str]=mapped_column(String(100)); model: Mapped[str]=mapped_column(String(100))
class AuditLog(Base, Scoped):
    __tablename__="audit_logs"; actor_id: Mapped[UUID|None]=mapped_column(ForeignKey("users.id")); action: Mapped[str]=mapped_column(String(100)); resource_type: Mapped[str]=mapped_column(String(100)); resource_id: Mapped[UUID|None]=mapped_column(Uuid); metadata_json: Mapped[dict]=mapped_column(JSON, default=dict)
class Notification(Base, Scoped):
    __tablename__="notifications"; user_id: Mapped[UUID]=mapped_column(ForeignKey("users.id")); type: Mapped[str]=mapped_column(String(60)); payload: Mapped[dict]=mapped_column(JSON, default=dict); read_at: Mapped[datetime|None]=mapped_column(DateTime(timezone=True))
class Session(Base, Scoped):
    __tablename__="sessions"; user_id: Mapped[UUID]=mapped_column(ForeignKey("users.id"), index=True); refresh_token_hash: Mapped[str]=mapped_column(String(255), unique=True); expires_at: Mapped[datetime]=mapped_column(DateTime(timezone=True)); revoked_at: Mapped[datetime|None]=mapped_column(DateTime(timezone=True))

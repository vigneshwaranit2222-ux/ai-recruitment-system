from sqlalchemy.orm import Session

from app.models.company import Company


class CompanyRepository:

    @staticmethod
    def create_company(
        db: Session,
        company_data
    ):

        company = Company(
            company_name=company_data.company_name,
            role_name=company_data.role_name,
            required_skills=company_data.required_skills,
            required_experience=company_data.required_experience,
            job_description=company_data.job_description
        )

        db.add(company)
        db.commit()
        db.refresh(company)

        return company

    @staticmethod
    def get_all_companies(db: Session):

        return db.query(Company).all()

    @staticmethod
    def get_company_by_id(
        db: Session,
        company_id: int
    ):

        return (
            db.query(Company)
            .filter(Company.id == company_id)
            .first()
        )
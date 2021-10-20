from fastapi import APIRouter, HTTPException
from fastapi_pagination import Page, paginate
from sqlmodel import Session, select

from api.db import engine
from identity.models import Profile

router = APIRouter()


@router.get("/profiles", response_model=Page[Profile])
async def list_profiles():
    with Session(engine) as session:
        profiles = session.exec(select(Profile)).all()
        return paginate(profiles)


@router.post("/profiles", response_model=Profile)
def create_profile(profile: Profile):
    with Session(engine) as session:
        session.add(profile)
        session.commit()
        session.refresh(profile)
        return profile


@router.get("/profiles/{sub}", response_model=Profile)
def get_profile(sub: str):
    with Session(engine) as session:
        profile = session.get(Profile, sub)
        if not profile:
            raise HTTPException(status_code=404, detail="Profile not found")
        return profile

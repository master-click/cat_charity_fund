from datetime import datetime

from sqlalchemy import select

from app.core.db import AsyncSessionLocal
from app.models.charity_project import CharityProject
from app.models.donation import Donation


def close_object(obj):
    obj.invested_amount = obj.full_amount
    obj.fully_invested = True
    obj.close_date = datetime.now()


async def investment(
    session: AsyncSessionLocal,
):
    projects = await session.execute(
        select(CharityProject).where(
            ~CharityProject.fully_invested).order_by(
            CharityProject.create_date
        )
    )
    projects = projects.scalars().all()
    donations = await session.execute(
        select(Donation).where(
            ~Donation.fully_invested).order_by(
            Donation.create_date
        )
    )
    donations = donations.scalars().all()
    for project in projects:
        for donation in donations:
            project_need_money = project.full_amount - project.invested_amount
            donation_free_money = donation.full_amount - donation.invested_amount
            if project_need_money > donation_free_money:
                project.invested_amount += donation_free_money
                close_object(donation)
            elif project_need_money < donation_free_money:
                donation.invested_amount += project_need_money
                close_object(project)
            elif project_need_money == donation_free_money:
                close_object(project)
                close_object(donation)
            session.add(project)
            session.add(donation)
    await session.commit()

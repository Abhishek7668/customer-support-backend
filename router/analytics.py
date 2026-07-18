from fastapi import APIRouter

from services.analytic_services import AnalyticsService

router = APIRouter(
    prefix="/analytics",
    tags=["Analytics"]
)


@router.get("/overview")
async def overview():

    data = await AnalyticsService.overview()

    return {

        "success": True,

        "data": data

    }
@router.get("/agents")
async def agents():

    data = await AnalyticsService.agent_usage()

    return {

        "success": True,

        "data": data

    }

@router.get("/intents")
async def intents():

    data = await AnalyticsService.intent_usage()

    return {

        "success": True,

        "data": data

    }

@router.get("/sessions")
async def sessions():

    data = await AnalyticsService.session_usage()

    return {

        "success": True,

        "data": data

    }

@router.get("/escalations")
async def escalations():

    data = await AnalyticsService.escalation_summary()

    return {

        "success": True,

        "data": data

    }
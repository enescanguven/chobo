from fastapi import APIRouter
from helpers.settings import settings

from api.v1.endpoints.recipe import router as recipe_router

api_router = APIRouter()

# api_router.include_router(auth, prefix="/auth", tags=["Authentication"])
# api_router.include_router(essay, prefix="/essays", tags=["Essay"])
# api_router.include_router(user, prefix="/user", tags=["User"])
api_router.include_router(recipe_router, prefix="/recipe", tags=["Recipe"])


@api_router.get("/_healthcheck", tags=["Status"])
def status_check():
    return {"status": "ok", "build_date": settings.BUILD_DATE}

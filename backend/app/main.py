from fastapi import FastAPI

from app.api.v1.organization import router as organization_router
from app.core.exception_handler import register_exception_handlers


from app.core.config import settings

print(settings.DATABASE_HOST)
print(settings.DATABASE_NAME)

app = FastAPI()
register_exception_handlers(app)

@app.get("/health")
def health():
    return {
        "Status":"healthy"
    }

app.include_router(organization_router)
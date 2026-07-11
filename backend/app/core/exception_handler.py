from fastapi import FastAPI, Request
from fastapi.responses import JSONResponse

from app.exceptions.organization_exceptions import (
    OrganizationAlreadyExistsException
)


def register_exception_handlers(app: FastAPI):

    @app.exception_handler(OrganizationAlreadyExistsException)
    async def organization_exists_exception_handler(
        request: Request,
        exc: OrganizationAlreadyExistsException
    ):

        return JSONResponse(
            status_code=409,
            content={
                "success": False,
                "message": str(exc)
            }
        )
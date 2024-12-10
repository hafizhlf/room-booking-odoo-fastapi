from typing import Annotated
from fastapi import APIRouter, HTTPException, Depends, status
from fastapi.responses import JSONResponse
from fastapi.security import APIKeyHeader
from odoo import fields, models
from odoo.api import Environment
from odoo.addons.fastapi.dependencies import odoo_env

class FastapiEndpoint(models.Model):
    _inherit = "fastapi.endpoint"

    app: str = fields.Selection(
        selection_add=[("room_booking", "Room Booking Management")], ondelete={"room_booking": "cascade"}
    )

    def _get_fastapi_routers(self) -> list[APIRouter]:
        if self.app == "room_booking":
            return [rb_api_router]
        return super()._get_fastapi_routers()

# room booking router
rb_api_router = APIRouter()

@rb_api_router.post("/room_booking/booking_status")
def get_booking_status(
    id: int,
    api_key: Annotated[
        str,
        Depends(
            APIKeyHeader(
                name="api-key",
                description="API Key is required to authenticate with Odoo. Use the API key generated for the corresponding user in Odoo.",
            )
        ),
    ],
    env: Annotated[Environment, Depends(odoo_env)]):

    user_id = env["res.users.apikeys"]._check_credentials(scope='rpc', key=api_key)
    if not user_id:
        raise HTTPException(
            status_code=status.HTTP_401_UNAUTHORIZED, detail="Incorrect API Key"
        )

    user = env["res.users"].sudo().search([('id', '=', user_id)])
    booking = user.env['room.booking'].search([('id', '=', id)])
    if not booking:
        return JSONResponse(status_code=404, content={"message": "Booking not found"})

    return {
        'booking_number': booking.name,
        'status': booking.state,
    }

from typing import Annotated
from fastapi import APIRouter, HTTPException, Depends
from fastapi.responses import JSONResponse
from odoo import fields, models
from odoo.api import Environment
from odoo.addons.fastapi.dependencies import odoo_env

class FastapiEndpoint(models.Model):
    _inherit = "fastapi.endpoint"

    app: str = fields.Selection(
        selection_add=[("room_booking", "Room Booking Management")], ondelete={"room_booking": "cascade"}
    )

    def _get_fastapi_routers(self):
        if self.app == "room_booking":
            return [rb_api_router]
        return super()._get_fastapi_routers()

# room booking router
rb_api_router = APIRouter()

@rb_api_router.post("/room_booking/booking_status")
def get_booking_status(id: int, env: Annotated[Environment, Depends(odoo_env)]):
    booking = env['room.booking'].sudo().search([('id', '=', id)])
    if not booking:
        return JSONResponse(status_code=404, content={"message": "Booking not found"})

    return {
        'booking_number': booking.name,
        'status': booking.state,
    }

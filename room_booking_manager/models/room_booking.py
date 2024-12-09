from odoo import _, models, fields, api
from odoo.exceptions import ValidationError

class RoomBooking(models.Model):
    _name = 'room.booking'
    _description = 'Room Booking'

    name = fields.Char(string='Name', required=True, default='New')
    room_id = fields.Many2one('room.master', string='Room', required=True)
    booking_name = fields.Char(string='Booking Name', required=True)
    booking_date = fields.Date(string='Booking Date', required=True)
    state = fields.Selection(
        [('draft', 'Draft'), 
         ('ongoing', 'On Going'), 
         ('done', 'Done')],
        string='Status', default='draft')
    notes = fields.Text(string='Booking Notes')

    _sql_constraints = [
        ('name_unique', 'UNIQUE(name)', 'Booking Number must be unique.'),
        ('booking_name_unique', 'UNIQUE(booking_name)', 'Booking Name must be unique.')
    ]

    @api.constrains('room_id', 'booking_date')
    def _check_unique_booking(self):
        for record in self:
            overlapping_bookings = self.search([
                ('room_id', '=', record.room_id.id),
                ('booking_date', '=', record.booking_date),
                ('id', '!=', record.id)
            ])
            if overlapping_bookings:
                raise ValidationError('The room is already booked for this date.')

    def action_set_ongoing(self):
        for record in self:
            if record.state == 'draft':
                record.state = 'ongoing'
                if record.room_id:
                    location = f"{record.room_id.location}/"
                    room_type = f"{record.room_id.room_type}/"
                record.name = f"{location or ''}{room_type or ''}{self.env['ir.sequence'].next_by_code('room.booking') or ''}".upper()

    def action_set_done(self):
        for record in self:
            if record.state == 'ongoing':
                record.state = 'done'

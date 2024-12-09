from odoo import models, fields, api

class RoomMaster(models.Model):
    _name = 'room.master'
    _description = 'Room Master'

    name = fields.Char(string='Room Name', required=True)
    room_type = fields.Selection(
        [('small', 'Small Meeting Room'), 
         ('large', 'Large Meeting Room'), 
         ('hall', 'Hall')], 
        string='Room Type', required=True)
    location = fields.Selection(
        [('1A', '1A'), ('1B', '1B'), ('1C', '1C'), 
         ('2A', '2A'), ('2B', '2B'), ('2C', '2C')],
        string='Room Location', required=True)
    photo = fields.Binary(string='Room Photo', required=True)
    capacity = fields.Integer(string='Room Capacity', required=True)
    description = fields.Text(string='Description')

    _sql_constraints = [
        ('name_unique', 'UNIQUE(name)', 'Room Name must be unique.'),
    ]

{
    'name': 'Room Booking Manager',
    'version': '17.0.1.0.0',
    'summary': 'Manage room details and reservations efficiently',
    'description': """
        This module allows users to manage room information and bookings. 
        Features include room management, booking processing, validation handling, and API tracking.
    """,
    'author': 'Hafizh Ibnu Syam',
    'website': 'https://github.com/hafizhlf/',
    'category': 'Management',
    'depends': ['base', 'fastapi', 'endpoint_route_handler'],
    'data': [
        'security/room_security.xml',
        'security/ir.model.access.csv',
        'data/room_booking_sequence.xml',
        'views/room_master_view.xml',
        'views/room_booking_view.xml',
        'views/room_booking_menu_views.xml',
    ],
    'installable': True,
    'application': True,
    'license': 'LGPL-3',
}

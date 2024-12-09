# Room Booking API

## Overview

This module demonstrating the integration of Odoo and FastAPI to provide a RESTful API for room booking management.

## Features

- Retrieve the status of a room booking by id.
- Designed for easy integration and extension.
- Secure and efficient use of Odoo's ORM for data access.

## Prerequisites

- Odoo version 17.0
- `fastapi` should be installed as it is a dependency for this module.

## Installation

1. Clone or download this repository into your Odoo `addons` directory.

    ```bash
    git clone https://github.com/yourusername/room_booking_api.git
    ```

2. Activate the module through the Odoo Apps interface.

## Usage

### Available Endpoints

1. **Get Booking Status**

   - **Endpoint:** `/room_booking/status`
   - **Method:** POST
   - **Description:** Retrieve booking status using the booking number.
   - **Parameters:** 

     ```json
     {
       "booking_number": "RB123456"
     }
     ```

   - **Response:**

     ```json
     {
       "booking_number": "RB123456",
       "status": "ongoing"
     }
     ```

### Authentication

- This module is set to be publicly accessible for simplicity, but you can integrate Odoo's authentication mechanisms for added security.

## Contributing

Contributions are welcome! Please adhere to the following guidelines:

- Fork the repository.
- Create a new branch for your feature or bug fix.
- Write clear, concise commit messages.
- Open a pull request against the main branch with a detailed description of your changes.

## License

This module is licensed under the LGPL-3.0 License. See the [LICENSE](LICENSE) file for more information.

## Support

For any questions or support, please reach out to [hafizhlf@outlook.com](mailto:hafizhlf@outlook.com) or open an issue in the repository.

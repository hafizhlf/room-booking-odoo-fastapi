# Room Booking API

## Overview

This module demonstrates the integration of Odoo and FastAPI to provide a RESTful API for room booking management.

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
    git clone https://github.com/hafizhlf/room-booking-odoo-fastapi
    ```

2. Build the Docker image using the provided `Dockerfile`:

    ```bash
    docker build -t room-booking-api .
    ```

3. For convenience, a `docker-compose.yml` file is provided to easily set up the environment. Simply run:

    ```bash
    docker-compose up
    ```

4. Activate the module through the Odoo Apps interface.

## Usage

For usage details, please refer to the [USAGE.md](USAGE.md) file.

## Support

For any questions or support, please reach out to [hafizhlf@outlook.com](mailto:hafizhlf@outlook.com) or open an issue in the repository.

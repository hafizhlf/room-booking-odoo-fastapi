FROM odoo:17.0

SHELL ["/bin/bash", "-xo", "pipefail", "-c"]

USER root

RUN pip install fastapi python-multipart ujson a2wsgi parse-accept-language

COPY ./endpoint_route_handler /mnt/extra-addons/endpoint_route_handler/
COPY ./fastapi /mnt/extra-addons/fastapi/
COPY ./room_booking_api /mnt/extra-addons/room_booking_api/
COPY ./room_booking_manager /mnt/extra-addons/room_booking_manager/

# Generate locale C.UTF-8 for postgres and general locale data
ENV LANG=en_US.UTF-8

# Retrieve the target architecture to install the correct wkhtmltopdf package
ARG TARGETARCH

VOLUME ["/var/lib/odoo"]

# Expose Odoo services
EXPOSE 8069 8071 8072

# Set the default config file
ENV ODOO_RC=/etc/odoo/odoo.conf

# Set default user when running the container
USER odoo

ENTRYPOINT ["/entrypoint.sh"]
CMD ["odoo"]
# Usage Guide for Room Booking Manager Integration with FastAPI

## Steps to Use:

1. **Install the Room Booking Manager Module**  
   - Navigate to the **Apps** menu in your Odoo instance.  
   - Search for **Room Booking Manager**.  
   - Click the **Install** button to add the module.

2. **Enable Access Rights**  
   - Go to the **Settings** menu in Odoo.  
   - Open the **Users & Companies > Users** section.  
   - Select the user who needs access and enable the required permissions for the **Room Booking Manager** module.

3. **Sync Booking Data via FastAPI**  
   - Navigate to the **FastAPI** menu in Odoo.  
   - Select the **Track Booking** data.  
   - Click the **Sync Registry** button to synchronize booking data with the FastAPI backend.

4. **Use API Key for External Access**  
   - To interact with the API, you must use an **API Key**.  
   - Refer to the [Odoo API Key Documentation](https://www.odoo.com/documentation/17.0/developer/reference/external_api.html#api-keys) to generate and configure your API Key.  
   - Include the **API Key** in the `api-key` header when making requests to FastAPI endpoints.  
     ```http
     POST /room_booking/booking_status HTTP/1.1
     Host: your-odoo-instance.com
     api-key: your_api_key
     ```

5. **Access API Documentation**  
   - You can explore and interact with the available endpoints by accessing the **API Docs** in the **FastAPI Form Views** section of Odoo.

You're all set to use the Room Booking Manager module with FastAPI!

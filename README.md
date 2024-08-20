# IoT Device Tracker

## Overview

The IoT Device Tracker is a Django-based web application that allows you to manage IoT devices that record temperature and humidity data. The application provides APIs to create, retrieve, delete, and list devices, as well as to fetch temperature and humidity readings for a specified time period. Additionally, the project includes a UI to visualize temperature and humidity trends over time using Chart.js.

## Features

- **Device Management**: Create, retrieve, delete, and list IoT devices.
- **Data Recording**: Store temperature and humidity readings for each device.
- **Data Visualization**: Graphical representation of temperature and humidity trends over time.
- **RESTful APIs**: Fully functional REST APIs to interact with the devices and readings.

## Table of Contents

- [Installation](#installation)
- [API Endpoints](#api-endpoints)
- [Device Graph UI](#device-graph-ui)
- [Usage](#usage)
- [Dependencies](#dependencies)

## Installation

### Prerequisites

- Python 3.x
- Django 3.x or later
- pip (Python package manager)

### Steps

1. **Clone the Repository**:
   ```bash
   git clone https://github.com/your-username/IoT-Device-Tracker.git
   cd IoT-Device-Tracker
   ```

2. **Create and Activate a Virtual Environment**:
   ```bash
   python -m venv myenv
   source myenv/bin/activate  # On Windows use: myenv\Scripts\activate
   ```

3. **Install Dependencies**:
   ```bash
   pip install -r requirements.txt
   ```

4. **Run Migrations**:
   ```bash
   python manage.py migrate
   ```

5. **Run the Development Server**:
   ```bash
   python manage.py runserver
   ```

   The application will be available at `http://127.0.0.1:8000/`.

## API Endpoints

### 1. Create a Device

- **Endpoint**: `POST /api/devices/`
- **Content-Type**: `application/json`
- **Request Payload**:
  ```json
  {
      "uid": "device-uid-1234",
      "name": "Device Name"
  }
  ```
- **Response**: `201 Created` with the device details.

### 2. Delete a Device

- **Endpoint**: `DELETE /api/devices/{device-uid}/`
- **Parameters**: 
  - `device-uid` (string): The UID of the device to delete.
- **Response**: `204 No Content` on successful deletion.

### 3. Retrieve a Device

- **Endpoint**: `GET /api/devices/{device-uid}/`
- **Parameters**: 
  - `device-uid` (string): The UID of the device to retrieve.
- **Response**: `200 OK` with the device details in JSON format.

### 4. List All Devices

- **Endpoint**: `GET /api/devices/`
- **Response**: `200 OK` with a JSON list of all devices.

### 5. Retrieve Readings for a Given Device

- **Endpoint**: `GET /api/devices/{device-uid}/readings/{parameter}/`
- **Parameters**:
  - `device-uid` (string): The UID of the device.
  - `parameter` (string): Either `temperature` or `humidity`.
  - Query Parameters:
    - `start_on` (string): Start time in `yyyy-mm-ddTHH:MM:SS` format.
    - `end_on` (string): End time in `yyyy-mm-ddTHH:MM:SS` format.
- **Response**: `200 OK` with the readings in JSON format.

## Device Graph UI

- **Endpoint**: `GET /devices-graph/`
- **Query Parameters**:
  - `device_uid` (string): The UID of the device.
- **Response**: An HTML page with graphs displaying the temperature and humidity data over time.

### Example Usage

To view the temperature and humidity graphs for a specific device, navigate to:

```
http://127.0.0.1:8000/devices-graph/?device_uid=device-uid-1234
```

## Dependencies

- **Django**: Python web framework.
- **Chart.js**: JavaScript library for creating charts.

### requirements.txt

```txt
Django>=3.x.x
django-json>=2.1.1
```
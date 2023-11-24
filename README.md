# Location-Based Service API (LBS)

## Project Overview

This project is a Location-Based Service (LBS) API developed using FastAPI, Python, and MongoDB. It focuses on handling
and querying geo-spatial data to offer functionalities like managing Points of Interest (POIs), finding nearby POIs, and
tracking user locations.

## Features

- CRUD operations for Points of Interest (POIs).
- Geo-spatial querying to find POIs near the user.
- User location tracking and history.
- Basic geo-fencing functionalities.
- Recommendations based on user location and preferences.

## Getting Started

### Prerequisites

- Python 3.11+
- MongoDB
- Poetry for dependency management

### Installation

1. Clone the repository:
   ```
   git clone https://github.com/njnur/LBS.git
   ```

2. Install dependencies using Poetry:
   ```
   poetry install
   ```

3. Set up MongoDB and ensure it is running on your local machine.

### Running the Application

1. Activate the Poetry shell:
   ```
   poetry shell
   ```

2. Start the FastAPI server:
   ```
   uvicorn main:app --reload
   ```

3. The API will be available at `http://localhost:8000`.

## API Endpoints

### POI Management

- `POST /pois`: Add a new POI.
- `GET /pois`: List all POIs.
- `GET /pois/{poi_id}`: Get details of a specific POI.
- `PUT /pois/{poi_id}`: Update a POI.
- `DELETE /pois/{poi_id}`: Delete a POI.

### Geo-Spatial Queries

- `GET /pois/nearby`: Find POIs within a specified radius of the user's location.

### User Location

- `POST /users/{user_id}/location`: Update user's current location.
- `GET /users/{user_id}/history`: Retrieve user's location history.

### Documentation

The API documentation is available at `http://localhost:8000/docs`.

## Testing

Run the tests using:

```
pytest
```

## Contributing

Contributions to this project are welcome. Please ensure to follow the code guidelines and add tests for new features.

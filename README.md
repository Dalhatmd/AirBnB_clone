# AirBnB clone - The console

The first part of cloning [Airbnb](https://www.airbnb.com/)

This project is an implementation of a simplified Airbnb clone, focusing on the development of a command-line interface (CLI) and backend logic for managing various entities such as users, places, reviews, and more.

## Project Structure

The project is organized into the following structure:

```
├── models
│   ├── __init__.py
│   ├── base_model.py
│   ├── user.py
│   ├── state.py
│   ├── review.py
│   ├── place.py
│   ├── city.py
│   └── amenity.py
├── tests
│   ├── __init__.py
│   ├── test_models
│   │   ├── __init__.py
│   │   ├── test_base_model.py
│   │   ├── test_user.py
│   │   ├── test_state.py
│   │   ├── test_review.py
│   │   ├── test_place.py
│   │   ├── test_city.py
│   │   └── test_amenity.py
│   └── test_engine
│       └── __init__.py
│       └── test_file_storage.py
├── models
│   └── engine
│       └── file_storage.py
├── console.py
└── README.md
```

## How to Use

### Running the Console

To start the command-line interface, run the following command:

```bash
./console.py
```

### Available Commands

- **create \<class name\>**: Creates a new instance of the specified class.
- **show \<class name\> \<id\>**: Prints the string representation of an instance.
- **destroy \<class name\> \<id\>**: Deletes an instance based on the class name and id.
- **all [\<class name\>]**: Prints all string representations of instances.
- **update \<class name\> \<id\> \<attribute name\> \<attribute value\>**: Updates an instance based on the class name and id.

### Models

- **BaseModel**: Base class for other models, providing common functionality.
- **User**: Class for handling system users.
- **State**: Class for handling system states.
- **Review**: Class for handling system reviews.
- **Place**: Class for handling system places.
- **City**: Class for handling system cities.
- **Amenity**: Class for handling system amenities.

### File Storage

The project includes a `FileStorage` class that serializes instances to a JSON file and deserializes JSON files to instances.

## Unit Tests

The `tests` directory contains unit tests for the various model classes and the file storage functionality.

## Web static

The 'web_static' directory contains web pages for the project

## Dependencies

- Python 3.x

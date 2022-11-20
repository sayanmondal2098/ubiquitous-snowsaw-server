# Fast API
_FastAPI framework, high performance, easy to learn, fast to code, ready for production_
FastAPI is a modern, fast (high-performance), web framework for building APIs with Python 3.7+ based on standard Python type hints.

The key features are:

-   **Fast**: Very high performance, on par with  **NodeJS**  and  **Go**  (thanks to Starlette and Pydantic).  [One of the fastest Python frameworks available](https://fastapi.tiangolo.com/#performance).
-   **Fast to code**: Increase the speed to develop features by about 200% to 300%. *
-   **Fewer bugs**: Reduce about 40% of human (developer) induced errors. *
-   **Intuitive**: Great editor support.  Completion  everywhere. Less time debugging.
-   **Easy**: Designed to be easy to use and learn. Less time reading docs.
-   **Short**: Minimize code duplication. Multiple features from each parameter declaration. Fewer bugs.
-   **Robust**: Get production-ready code. With automatic interactive documentation.
-   **Standards-based**: Based on (and fully compatible with) the open standards for APIs:  [OpenAPI](https://github.com/OAI/OpenAPI-Specification)  (previously known as Swagger) and  [JSON Schema](https://json-schema.org/).


To create a virtua env, follow the command -
```bash
python3 -m venv venv (in mac)
or
py -3 -m venv venv (windows)
```
The activate the venv with 
```bash
source venv/bin/activate (mac)
or
venv/Scripts/activate.bat (windows)
```
To install fastAPI
```bash
pip install fastapi[all]
```

You will also need an ASGI server, for production such as [Uvicorn](https://www.uvicorn.org/) or [Hypercorn](https://github.com/pgjones/hypercorn).

```bash
pip install "uvicorn[standard]"
```

Run the server with 
```
uvicorn main:app --reload
```


The API DOCUMENTATION is available on : http://localhost:8000/docs
The Redabale API Documentation is available on : http://localhost:8000/redoc 
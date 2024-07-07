import http

from fastapi import FastAPI, Response

app = FastAPI()


@app.get("/health-check")
async def health_check():
    return Response(status_code=http.HTTPStatus.OK)

from fastapi import FastAPI,APIRouter
from fastapi.responses import FileResponse
from fastapi.openapi.docs import get_swagger_ui_html as get_swagger
from fastapi.middleware.cors import CORSMiddleware
from app.controllers import router as controllers_router
from app.database import dynamo as database

app = FastAPI(title='Social Media',version="0.8",docs_url=None,description="")
app_auth = APIRouter()

app.include_router(router=controllers_router)
app.add_middleware(CORSMiddleware,allow_origins=["*"],allow_credentials=True,allow_methods=["*"],allow_headers=["*"])

@app.on_event("startup")
async def stratup_table():
    database.create_users_table()

@app.get("/docs", include_in_schema=True)
def swagger():
    return get_swagger(openapi_url="/openapi.json", title="Socail Media", swagger_favicon_url="/icon")

@app.get(path="/icon", description="icon", include_in_schema=True)
def icon():
    return FileResponse("app/icon.png")
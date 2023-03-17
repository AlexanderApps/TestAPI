from fastapi import FastAPI
from fastapi.middleware.cors import CORSMiddleware

from db_actions.manage_tables import create_tables, drop_tables, init_tables
from routers import login_router, product_router, \
    transaction_router, user_router, product_category_router

origins = [
    "http://localhost",
    "http://localhost:8080",
    "http://localhost:3000",
]


###############################################

# create_tables()
# init_tables()


##################
# drop_tables()
###############################################


app = FastAPI()

app.add_middleware(
    CORSMiddleware,
    allow_origins=origins,
    allow_credentials=True,
    allow_methods=["*"],
    allow_headers=["*"],
)


@app.get("/")
async def root():
    return {"message": "Hello World"}


app.include_router(login_router.router)
app.include_router(user_router.router)
app.include_router(product_router.router)
app.include_router(product_category_router.router)
app.include_router(transaction_router.router)

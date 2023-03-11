from fastapi import FastAPI

from db_actions.manage_tables import create_tables, drop_tables, init_tables
from routers import login_router, product_router, \
      transaction_router, user_router, product_category_router


###############################################

# create_tables()
# init_tables()



##################
# drop_tables()
###############################################


app = FastAPI()

@app.get("/")
async def root():
    return {"message": "Hello World"}


app.include_router(login_router.router)
app.include_router(user_router.router)
app.include_router(product_router.router)
app.include_router(product_category_router.router)
app.include_router(transaction_router.router)



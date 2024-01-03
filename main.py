from fastapi import FastAPI


app = FastAPI()

@app.get("/")
async def root():
    return {"message":"speer assignment"}

@app.get("/test")
async def test():
    return {"test":"vimeo"}
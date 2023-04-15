from app import create_app

import uvicorn

app = create_app()

if __name__ == "__main__":
    uvicorn.run("main:app", host="192.168.1.15" , port=8000, reload=True, log_level="info")
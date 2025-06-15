from fastapi import FastAPI
from fastapi.middleware.cors import CORSMiddleware
from app.routes.prompt_route import router as prompt_router

app = FastAPI(title="FastAPI LLM Prompt API")

# 添加CORS中间件
app.add_middleware(
    CORSMiddleware,
    allow_origins=["http://localhost:8080"],  # 明确指定前端地址
    allow_credentials=True,
    allow_methods=["GET", "POST", "OPTIONS"],  # 明确允许的方法
    allow_headers=["*"],
    expose_headers=["*"]  # 暴露所有头信息
)

# 注册路由
app.include_router(prompt_router)


@app.get("/")
def read_root():
    return {"message": "欢迎使用基于 FastAPI 的大模型提示词接口"}

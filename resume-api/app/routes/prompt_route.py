from fastapi import APIRouter, HTTPException
from pydantic import BaseModel
from app.services.llm_service import call_llm, polish_content
from app.constants import *
from string import Template

router = APIRouter(prefix="/prompt", tags=["Prompt"])


class PromptRequest(BaseModel):
    job_description: str              # 岗位介绍
    project_list: list[str]     # 项目经历


class PolishRequest(BaseModel):
    job_description: str  # 岗位介绍
    project_content: str  # 项目内容


@router.post("/process")
async def process_prompt(request: PromptRequest):
    try:
        # 替换提示词中的 {} 占位符
        template = Template(PROMPT)
        filled_prompt = template.substitute(
            jd=request.job_description, project=request.project_list)
        result = call_llm(filled_prompt)
        return {"filled_prompt": filled_prompt, "result": result}
    except IndexError:
        raise HTTPException(
            status_code=400, detail="提示词中的占位符数量与 data_list 不匹配")


@router.post("/polish")
async def polish_resume_content(request: PolishRequest):
    try:
        result = polish_content(
            job_description=request.job_description,
            project_content=request.project_content
        )
        return result
    except Exception as e:
        raise HTTPException(
            status_code=500,
            detail=f"润色失败: {str(e)}"
        )

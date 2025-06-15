import json
import logging
import requests
from app.constants import MODEL_ACCESS_KEY

# 配置基础logging
logging.basicConfig(
    level=logging.INFO,
    format='%(asctime)s - %(name)s - %(levelname)s - %(message)s',
    handlers=[logging.StreamHandler()]
)


def polish_content(job_description: str, project_content: str) -> dict:
    """
    调用大模型润色项目内容
    返回格式: {
        "polished_content": "润色后的内容",
        "polish_reason": "润色依据"
    }
    """
    url = "https://qianfan.baidubce.com/v2/chat/completions"

    system_prompt = """你是一个专业的简历优化助手，请根据岗位要求优化项目经历描述。
    返回JSON格式，包含两个字段：
    - polished_content: 优化后的内容
    - polish_reason: 优化依据，说明做了哪些改进"""

    user_prompt = f"""岗位要求：{job_description}
    
    需要优化的项目经历：
    {project_content}
    
    请按照以下要求优化：
    1. 使用更专业的表达方式
    2. 量化工作成果
    3. 使用行业术语
    4. 调整句式结构
    5. 突出技术细节和业务价值"""

    payload = json.dumps({
        "model": "ernie-speed-128k",
        "messages": [
            {
                "role": "system",
                "content": system_prompt
            },
            {
                "role": "user",
                "content": user_prompt
            }
        ],
        "temperature": 0.1,
        "top_p": 0.7,
    })

    headers = {
        'Content-Type': 'application/json',
        'Authorization': f'Bearer {MODEL_ACCESS_KEY}'
    }

    response = requests.request("POST", url, headers=headers, data=payload)
    logging.info(response.text)
    try:
        return json.loads(response.json()['choices'][0]['message']['content'].replace(
            "```json", "").replace("```", "").strip("{").strip("\n"))
    except json.JSONDecodeError:
        return {
            "polished_content": project_content,
            "polish_reason": "润色失败，请稍后重试"
        }


def call_llm(prompt: str) -> str:
    """
    模拟调用大模型并返回结果。
    实际中可以替换成调用 OpenAI、LangChain 或本地模型等。
    """
    url = "https://qianfan.baidubce.com/v2/chat/completions"

    payload = json.dumps({
        "model": "ernie-speed-128k",
        "messages": [
            {
                "role": "system",
                "content": "平台助手"
            },
            {
                "role": "user",
                "content": prompt
            }
        ]
    })
    headers = {
        'Content-Type': 'application/json',
        'Authorization': f'Bearer {MODEL_ACCESS_KEY}'
    }

    response = requests.request("POST", url, headers=headers, data=payload)

    return f"LLM 处理后的结果：{response.text}"

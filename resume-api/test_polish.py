import requests
import json

# 测试端点
url = "http://localhost:8000/prompt/polish"

# 请求头
headers = {
    "Content-Type": "application/json",
    "Origin": "http://localhost:8080"  # 必须与CORS配置匹配
}

# 请求体
data = {
    "job_description": "Python开发工程师，要求3年以上经验",
    "project_content": "开发了一个基于FastAPI的简历优化系统"
}

try:
    # 发送POST请求
    response = requests.post(url, headers=headers, data=json.dumps(data))

    # 打印响应
    print(f"状态码: {response.status_code}")
    print("响应内容:")
    res = response.json()
    print("---")
    print(res)
    # res = res['choices'][0]['message']['content'].replace(
    #     "```json", "").replace("```", "").strip("{").strip("\n")
    # print(res)
    # final_res = json.loads(res)
    # print(final_res)


except requests.exceptions.RequestException as e:
    print(f"请求失败: {str(e)}")

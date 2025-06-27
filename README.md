# Summer-Project

## 快速启动
1. 打开 Codespaces（或本地）
2. 安装依赖：
   ```bash
   pip install --no-cache-dir -r requirements.txt
3. 启动服务：
uvicorn app.main:app --reload --host 0.0.0.0 --port 8000
4. 在浏览器访问：
文档： http://localhost:8000/docs
推荐： GET  /attractions?destination=北京&days=2&preferences=文化,美食
详情： GET  /attractions/{id}
行程： POST /itinerary (JSON body)

## 协作开发
1. Fork 或 Clone 仓库
2. 点击 **Code → Open with Codespaces**
3. 等待容器启动并安装依赖
4. 运行 Uvicorn 并联调前端，即可开始协作开发

from fastapi import FastAPI, BackgroundTasks, HTTPException
from fastapi.responses import JSONResponse
from celery.result import AsyncResult
from app.worker import celery_app
from app.tasks import sample_task
from app.schemas.task import TaskRequest

app = FastAPI(title="FastAPI Celery")

# 創建一個新的 Celery 任務
@app.post("/tasks", status_code=201)
def create_task(request: TaskRequest):
    task = sample_task.delay(request.param1, request.param2)
    return {"task_id": task.id, "status": "任務建立。"}

# 檢查任務狀態
@app.get("/tasks/{task_id}")
def get_task_status(task_id: str):
    task_result = AsyncResult(task_id, app=celery_app)
    if task_result.state == 'PENDING':
        response = {
            "task_id": task_id,
            "status": task_result.state,
            "message": "任務等待執行。",
        }
    elif task_result.state == 'FAILURE':
        response = {
            "task_id": task_id,
            "status": task_result.state,
            "error": str(task_result.info),
        }
    else:
        response = {
            "task_id": task_id,
            "status": task_result.state,
            "result": task_result.info if task_result.state == 'SUCCESS' else None
        }
    
    return response

# 手動執行排程
@app.post("/schedule_task")
def schedule_adhoc_task(request: TaskRequest, background_tasks: BackgroundTasks):
    task = sample_task.apply_async(
        args=[request.param1],
        kwargs={"param2": request.param2},
        countdown=60  # 60秒後執行
    )
    return {"task_id": task.id, "status": "任務已安排", "execute_at": "1分鐘後"}
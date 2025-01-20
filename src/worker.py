from celery import Celery

celery = Celery(
    'worker',
    broker='redis://redis:6379/0',
    backend='redis://redis:6379/0'
)

@celery.task
def analyze_code_task(code: str):
    # Aqui você implementaria a análise assíncrona
    pass
from celery import shared_task
from celery.utils.log import get_task_logger
import requests
from monitor.models import Url, Requests


logger = get_task_logger(__name__)


@shared_task
def sample_task():
    urls = Url.objects.all()
    for item in urls:
        res = requests.get(url=item.address)
        status = res.status_code
        if not status == 200 : 
            item.failed_times += 1 
        Requests.objects.create(url=item, result=status)
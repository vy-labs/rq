import os

DEFAULT_JOB_CLASS = 'rq.job.Job'
DEFAULT_QUEUE_CLASS = 'rq.Queue'
DEFAULT_WORKER_CLASS = 'rq.Worker'
DEFAULT_CONNECTION_CLASS = 'redis.StrictRedis'
DEFAULT_WORKER_TTL = 420
DEFAULT_RESULT_TTL = 500
namespace = os.getenv('RQ_NAMESPACE') or os.getenv('JOB_ID')
DEFAULT_NAMESPACE = ":{}".format(namespace) if namespace else ''
DEFAULT_QUEUE_TIMEOUT = int(os.getenv('RQ_QUEUE_TIMEOUT', 180))

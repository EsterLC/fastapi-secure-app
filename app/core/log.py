import logging, json, sys
handler = logging.StreamHandler(sys.stdout)
formatter = logging.Formatter('%(message)s')
logger = logging.getLogger("app")
logger.setLevel(logging.INFO)
logger.addHandler(handler)

def log_json(**kwargs):
    logger.info(json.dumps(kwargs, ensure_ascii=False))

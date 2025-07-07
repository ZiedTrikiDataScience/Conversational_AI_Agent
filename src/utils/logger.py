import logging, yaml, logging.config

def get_logger(name: str) -> logging.Logger:
    cfg = yaml.safe_load(open("config/logging_config.yaml"))
    logging.config.dictConfig(cfg)
    return logging.getLogger(name)

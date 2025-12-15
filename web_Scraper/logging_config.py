import logging
import logging.config
from pathlib import Path

base_dir = Path(__file__).resolve().parent
log_dir = base_dir / "logs"
log_file = log_dir / "app.log"
error_log_file = log_dir / "error.log"

log_dir.mkdir(parents=True, exist_ok=True)

logging_config = {
    'version': 1,
    'disable_existing_loggers': False,
    'formatters': {
        'standard': {
            'format': '%(asctime)s - [%(levelname)s] - %(name)s -  - %(message)s',
            'datefmt': '%Y-%m-%d %H:%M:%S'
        },
        'detailed': {
            'format': '%(asctime)s - [%(levelname)s] - %(name)s.%(funcName)s:%(lineno)d - %(message)s', # if you want the thread name to be printed use %(threadName)s
            'datefmt': '%Y-%m-%d %H:%M:%S'
        }
    },
    'handlers':{
        'console': {
            'class': 'logging.StreamHandler',
            'level': 'DEBUG',
            'formatter': 'standard',
            'stream': 'ext://sys.stdout',
        },
        'file': {
            # rotate every hour
            'class': 'logging.handlers.TimedRotatingFileHandler',
            'level': 'INFO',
            'formatter': 'detailed',
            'filename': str(log_file),
            'when': "H",
            'interval' : 1, 
            'backupCount': 168, # keep the logs of 7 days of hourly logs,
            'encoding': 'utf-8'
        },
        'error_file': {
            # rotate every hour
            'class': 'logging.handlers.TimedRotatingFileHandler',
            'level': 'ERROR',
            'formatter': 'detailed',
            'filename': str(error_log_file),
            'when': "H",
            'interval' : 1, 
            'backupCount': 168, # keep the logs of 7 days of hourly logs,
            'encoding': 'utf-8'
        }
    },
    'loggers': {
        # root logger
        '': {
            'level': "DEBUG",
            'handlers': ['console', 'file', 'error_file']
        },
        'main': {
            'level': "DEBUG",
            'handlers': ['console', 'file', 'error_file'],
            'propagate': False
        },

        # configure the log level for third party library
        'boto3':{
            'level': "WARNING"
        }
    }
}

def setup_logging():
    logging.config.dictConfig(logging_config)
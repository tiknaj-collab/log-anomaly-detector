import re

def normalize_log(log_line):
    log_line = re.sub(r"userId=\d+", "userId=<ID>", log_line)
    log_line = re.sub(r"\d{4}-\d{2}-\d{2} \d{2}:\d{2}:\d{2}", "<TIMESTAMP>", log_line)
    log_line = re.sub(r"\d+", "<NUM>", log_line)
    return log_line

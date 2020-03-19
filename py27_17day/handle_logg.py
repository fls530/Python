import logging
from logging.handlers import TimedRotatingFileHandler


def create_log():
    """
    创建日志收集器
    :return: 日志收集器
    """
    # 创建一个日志收集器
    log = logging.getLogger("rourou")
    # 设置收集等级
    log.setLevel("DEBUG")
    # 日志轮转,创建一个按时间轮转的输出渠道
    fh = logging.FileHandler("testlog.log", encoding="utf8")
    fh.setLevel("DEBUG")
    log.addHandler(fh)
    # 输出到控制台
    # sh = logging.StreamHandler()
    # sh.setLevel("ERROR")
    # log.addHandler(sh)

    # 输出渠道的格式
    formats = '%(asctime)s - [%(filename)s-->line:%(lineno)d] - %(levelname)s: %(message)s'
    form = logging.Formatter(formats)
    fh.setFormatter(form)
    return log


log = create_log()

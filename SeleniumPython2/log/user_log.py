#coding=utf-8
import logging
import os
import datetime
class UserLog:
    def __init__(self):
        self.logger = logging.getLogger()
        self.logger.setLevel(logging.DEBUG)
        #self.file_handle.setLevel(logging.INFO)
        #文件名字
        base_dir = os.path.dirname(os.path.abspath(__file__))
        log_dir = os.path.join(base_dir,'logs')
        log_file = datetime.datetime.now().strftime('%Y-%m-%d')+'.log'
        log_name = log_dir+"/"+log_file
        '''
        #控制台输出日志
        console = logging.StreamHandler()
        logger.addHandler(console)
        logger.debug('控制台输出日志')
        console.close()
        logger.removeHandler(console)
        '''
        #文件输出日志
        self.file_handle = logging.FileHandler(log_name,'a',encoding='utf-8')
        #self.file_handle.setLevel(logging.INFO)
        formatter = logging.Formatter('%(asctime)s %(filename)s---> %(funcName)s %(levelno)s---> %(levelname)s ------->%(message)s')
        self.file_handle.setFormatter(formatter)
        self.logger.addHandler(self.file_handle)
        #self.logger.debug("文件输出日志test1234")
        #file_handle.close()
        #self.logger.removeHandler(file_handle)

    def get_log(self):
        return self.logger

    def close_log(self):
        self.file_handle.close()
        self.logger.removeHandler(self.file_handle)

if __name__ =="__main__":
    user = UserLog()
    log = user.get_log()
    log.debug('test')
    user.close_log()
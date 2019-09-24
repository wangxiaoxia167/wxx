#coding=utf-8
import sys
sys.path.append('C:\\Users\\xx\\Desktop\\SeleniumPython2')
from util.opera_excel import OperaExcel
from kwd.actionMethod import actionMethod
from log.user_log import UserLog
class KeyWordCase:
    def run_main(self):
        user = UserLog()
        log = user.get_log()
        log.debug('debug-test')
        #log.info('keyword_case')
        self.action_method = actionMethod()
        handle_excel = OperaExcel('C:/Users/xx/Desktop/SeleniumPython2/config/keyword.xls',0)
        case_lines = handle_excel.get_lines()
        if case_lines:
            for i in range(1,case_lines):
                #is_run是否执行
                is_run = handle_excel.get_cell(i,3)
                if is_run == 'yes':
                    #method:执行方法；send_value:输入的数据；handle_value：操作元素
                    method = handle_excel.get_cell(i,4)
                    send_value = handle_excel.get_cell(i,5)
                    handle_element = handle_excel.get_cell(i,6)
                    except_result_method = handle_excel.get_cell(i,7)
                    except_result = handle_excel.get_cell(i, 8)
                    self.run_method(method, handle_element,send_value)
                    if except_result != '':
                        #将预期结果值根据=划分成list
                        except_value = self.get_except_result_value(except_result)
                        if except_value[0] == 'text':
                            result = self.run_method(except_result_method,handle_element,'')
                            if except_value[1] in result:
                                handle_excel.write_value(i,'pass')
                            else:
                                handle_excel.write_value(i,'fail')
                        elif except_value[0] == 'element':
                            result = self.run_method(except_result_method,except_value[1],'')
                            if result != 'error':
                                handle_excel.write_value(i,'pass')
                            else:
                                handle_excel.write_value(i, 'fail')
                        else:
                            print('没有else')
                    else:
                        print('没有预期结果')


    #获取预期结果值
    def get_except_result_value(self,data):
        return data.split('=')

    def run_method(self,method,handle_element,send_value):
        method_value = getattr(self.action_method,method)
        if send_value:
            result = method_value(handle_element,send_value)
        else:
            result = method_value(handle_element)
        return result

if __name__ =='__main__':
    case = KeyWordCase()
    case.run_main()
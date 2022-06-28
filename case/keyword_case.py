# coding=utf-8
import sys
sys.path.append("F:\\projects\\selenium")

from util.excel_util import ExcelUtil
from keywordTest.action_method import ActionMethod


class KeywordCase(object):
    def run_main(self):
        excel_handler = ExcelUtil("F:\\projects\\selenium\\config\\keyword.xls")
        excel_data = excel_handler.get_data()
        self.am = ActionMethod()
        case_lines = excel_handler.get_lines()
        if case_lines:
            for i in range(1, case_lines):
                line_data = excel_data[i]
                is_excute = line_data[3]
                exc_method = line_data[4]
                send_data = line_data[5]
                key = line_data[6]
                except_result = line_data[7]
                except_result_value = line_data[8]
                if is_excute == "yes":
                    self.run_method(exc_method, key, send_data)
                    except_value = self.get_except_value(except_result_value)
                    if except_result_value:
                        if except_value[0] == "text":
                            result = self.run_method(except_result)
                            print("-------text result:", result)
                            if except_value[1] in result:
                                excel_handler.write_data(i, "pass")
                            else:
                                excel_handler.write_data(i, "fail")
                        elif except_value[0] == "element":
                            result = self.run_method(except_result, except_value[1])
                            print("-------element result:", result)
                            if result:
                                excel_handler.write_data(i, "pass")
                            else:
                                excel_handler.write_data(i, "fail")
                        else:
                            print("except value error")
                    else:
                        print("except result value is none")
                        
    def run_method(self, method, key="", send_data=""):
        method_value = getattr(self.am, method)
        print("method_value: " , method_value)
        if send_data and key:
            return method_value(key, send_data)
        elif send_data == "" and key:
            return method_value(key)
        elif send_data and key == "":
            return method_value(send_data)
        else:
            return method_value()

    def get_except_value(self, value):
        return value.split("=")

if __name__ == '__main__':
    kc = KeywordCase()
    kc.run_main()

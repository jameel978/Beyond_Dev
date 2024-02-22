from infra.Phone_instance import Phoneinstance



class CalculatorApp(Phoneinstance):
    MUL_SIGN = "com.google.android.calculator:id/op_mul"
    ADD_SIGN = "com.google.android.calculator:id/op_add"
    SUB_SIGN = "com.google.android.calculator:id/op_sub"
    DIV_SIGN = "com.google.android.calculator:id/op_div"
    EQ_SIGN = "com.google.android.calculator:id/eq"
    FINAL_RESULT_ELEM = "com.google.android.calculator:id/result_final"
    DIGIT_ELEM = "com.google.android.calculator:id/digit_"

    def __init__(self):        
        super().__init__()
        self.init_elements()

    def init_elements(self):
        self.equal_sign = self.find_elem_by_ID(self.EQ_SIGN)
        self.add_sign = self.find_elem_by_ID(self.ADD_SIGN)
        self.sub_sign = self.find_elem_by_ID(self.SUB_SIGN)
        self.mul_sign = self.find_elem_by_ID(self.MUL_SIGN)
        self.div_sign = self.find_elem_by_ID(self.DIV_SIGN)
        
    def init_final_result(self):
        self.result_elem = self.find_elem_by_ID(self.FINAL_RESULT_ELEM)
        
    def click_on_num(self,num):
        self.find_elem_by_ID(self.DIGIT_ELEM + num).click()
        
    def send_number_flow(self,number):
        for digit in str(number):
            self.click_on_num(digit)
        
    def performe_mul_operation(self,num1,num2):
        self.send_number_flow(num1)
        self.mul_sign.click()
        self.send_number_flow(num2)

    def performe_sub_operation(self,num1,num2):
        self.send_number_flow(num1)
        self.sub_sign.click()
        self.send_number_flow(num2)

    def performe_add_operation(self,num1,num2):
        self.send_number_flow(num1)
        self.add_sign.click()
        self.send_number_flow(num2)

    def performe_div_operation(self,num1,num2):
        self.send_number_flow(num1)
        self.div_sign.click()
        self.send_number_flow(num2)             
        
    def calculate_and_get_result(self):
        self.equal_sign.click()
        self.init_final_result()
        return self.result_elem.text
   
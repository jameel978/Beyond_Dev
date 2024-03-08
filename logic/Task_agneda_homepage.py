from infra.Phone_instance import Phoneinstance
from datetime import datetime, timedelta


class TaskAgenda(Phoneinstance):

    #Homepage elements
    ADD_TASK = "com.claudivan.taskagenda:id/btNovoEvento"
    HAMBURGER_MENU = "com.claudivan.taskagenda:id/hamburguer"
    CALENDAR_BUTTON = '//android.widget.TextView[@text="Calendar"]'
    RIGHT_ARROW = "com.claudivan.taskagenda:id/ibtAvancar"
    LEFT_ARROW = "com.claudivan.taskagenda:id/ibtRetroceder"
    CALENDAR_CURRENT_MONTH = 'com.claudivan.taskagenda:id/tvVisor'
    CALENDAR_DAY = '//android.widget.TextView[@text="'
    NAVIGATE_BACK = '//android.widget.ImageButton[@content-desc="Navigate up"]'

    #1 = sunday , 7 = saturady
    DAY_ELEMENT = '//android.widget.LinearLayout[@resource-id="com.claudivan.taskagenda:id/containerColunasHorarios"]/android.widget.RelativeLayout'

    #hamburger menu elements
    ALL_EVENTS_BUTTON = "com.claudivan.taskagenda:id/btEventos"
    LATE_EVENT_BUTTON = "com.claudivan.taskagenda:id/btEventosAtrasados"
    COLOR_EVENT_TYPES = "com.claudivan.taskagenda:id/btCores"
    SETTING_BUTTON = "com.claudivan.taskagenda:id/btAjustes"

    #Add tasks elements
    SELECT_DAY_BUTTON_XPATH = '//android.widget.TextView[@resource-id="android:id/text1" and @text='

    #NEW event page
    EVENT_NAME_INPUT = 'com.claudivan.taskagenda:id/etTitulo'
    TIME_NAME_INPUT = 'com.claudivan.taskagenda:id/btHora'
    DESCRRIPTION_INPUT = 'com.claudivan.taskagenda:id/etDescricao'
    SAVE_BUTTON = 'com.claudivan.taskagenda:id/item_salvar'
    EDIT_BUTTON = 'com.claudivan.taskagenda:id/item_editar'
    DELETE_BUTTON = 'com.claudivan.taskagenda:id/item_excluir'
    CONFIRM_DELETE_BUTTON = 'android:id/button1'
    CLEAR_NAME_BUTTON = 'com.claudivan.taskagenda:id/btApagarTitulo'
    CURRENT_TASK_CHECKBOX = 'com.claudivan.taskagenda:id/cbEventoConcluido'



    #AFTER ADDING EVENTS
    CURRENT_EVENTS = "com.claudivan.taskagenda:id/btEventosSemana"
    CURRENT_ADDED_EVENT = '//android.widget.ListView[@resource-id="com.claudivan.taskagenda:id/lvListaEventos"]/android.widget.FrameLayout/android.widget.RelativeLayout'
    CURRENT_EVENT_NAME = 'com.claudivan.taskagenda:id/tvTitulo'
    CURRENT_EVENT_DATE = '//android.widget.TextView[@resource-id="com.claudivan.taskagenda:id/tvData"]'

    #CURRENT_EVENTS_PAGE
    COMPLETE_EVENT = 'com.claudivan.taskagenda:id/cbEventoConcluido'


    #After CLICKING ON DAY ELEMENT
    NEW_EVENT_BUTTON = '//android.widget.TextView[@resource-id="android:id/text1" and @text="New event"]'
    VIEW_EVENTS_BUTTON = '//android.widget.TextView[@resource-id="android:id/text1" and @text="View events"]'
    
    
    ##STOCK_MONTH VIEWFINDER BUTTONS
    CURRENT_DATE_AND_YEAR = '//android.view.View[@content-desc="'
    CURRENT_DAY_MONTH = '//android.widget.TextView[@resource-id="android:id/date_picker_header_date"]'
    CURRENT_YEAR = '//android.widget.TextView[@resource-id="android:id/date_picker_header_year"]'
    OK_BUTTON = '//android.widget.Button[@resource-id="android:id/button1"]'
    NEXT_month = '//android.widget.ImageButton[@content-desc="Next month"]'


    def __init__(self):        
        super().__init__()



    def create_new_task_from_homepage_using_add_sign(self,name ='' ,day='Today'):
        self.find_elem_by_ID_and_click(self.ADD_TASK)
        self.find_elem_by_XPATH_and_click(self.SELECT_DAY_BUTTON_XPATH + '"' + day + '"]')
        if day!="Other":
            self.add_name_to_task(name)


    def add_name_to_task(self,name):
        self.find_elem_by_ID_and_sendkeys(self.EVENT_NAME_INPUT, name)
    def add_discription_to_task(self,disc):
        self.find_elem_by_ID_and_sendkeys(self.DESCRRIPTION_INPUT, disc)

    def click_save_button(self):
        self.find_elem_by_ID_and_click(self.SAVE_BUTTON)

    def check_if_event_is_added(self):
        try:
            self.find_elem_by_ID_and_click(self.HAMBURGER_MENU)
            self.find_elem_by_ID_and_click(self.ALL_EVENTS_BUTTON)
        except:
            pass
        try:
            self.find_elem_by_XPATH(self.CURRENT_ADDED_EVENT)
            return True
        except:
            return  False
        
    def get_current_event_name(self):
        self.find_elem_by_ID_and_click(self.CURRENT_EVENTS)
        return self.find_elem_by_ID(self.CURRENT_EVENT_NAME).text
    
    def get_current_event_date(self):
        try:
            self.find_elem_by_ID_and_click(self.HAMBURGER_MENU)
            self.find_elem_by_ID_and_click(self.ALL_EVENTS_BUTTON)
        except:
            pass
        self.find_elem_by_XPATH_and_click(self.CURRENT_ADDED_EVENT)
        return self.find_elem_by_XPATH(self.CURRENT_EVENT_DATE).text[5:]

    def get_current_event_date_from_hamburger_menu(self):
        self.find_elem_by_ID_and_click(self.HAMBURGER_MENU)
        self.find_elem_by_ID_and_click(self.ALL_EVENTS_BUTTON)
        self.find_elem_by_XPATH_and_click(self.CURRENT_ADDED_EVENT)
        return self.find_elem_by_XPATH(self.CURRENT_EVENT_DATE).text[5:]

    def select_date_from_month_stock_view_finder(self, date):
        current_day_month_year = self.find_elem_by_XPATH(self.CURRENT_DAY_MONTH).text[5:] + " "
        current_day_month_year += self.find_elem_by_XPATH(self.CURRENT_YEAR).text
        date1 = datetime.strptime(current_day_month_year, "%b %d %Y")
        date2 = datetime.strptime(date, "%d %b %Y")
        delta_months = (date2.year - date1.year) * 12 + date2.month - date1.month
        for i in range(delta_months):
            self.find_elem_by_XPATH_and_click(self.NEXT_month)
        current_elem = self.CURRENT_DATE_AND_YEAR + date2.strftime('%d %B %Y') + '"]'
        self.find_elem_by_XPATH_and_click(current_elem)
        self.find_elem_by_XPATH_and_click(self.OK_BUTTON)


    def create_new_task_from_homepage_using_calendar_tab(self,name ,date):
        self.find_elem_by_XPATH_and_click(self.CALENDAR_BUTTON)
        current_day_month_year = "1 " + self.find_elem_by_ID(self.CALENDAR_CURRENT_MONTH).text
        date1 = datetime.strptime(current_day_month_year, "%d %B %Y")
        date2 = datetime.strptime(date, "%d %b %Y")
        delta_months = (date2.year - date1.year) * 12 + date2.month - date1.month
        for i in range(delta_months):
            self.find_elem_by_ID_and_click(self.RIGHT_ARROW)
        self.find_elem_by_XPATH_and_click(self.CALENDAR_DAY + date2.strftime('%d"]'))
        self.find_elem_by_ID_and_click(self.ADD_TASK)
        self.add_name_to_task(name)


    def navigate_back(self):
        self.find_elem_by_XPATH_and_click(self.NAVIGATE_BACK)


    def change_event_name(self,name):
        self.find_elem_by_ID_and_click(self.HAMBURGER_MENU)
        self.find_elem_by_ID_and_click(self.ALL_EVENTS_BUTTON)
        self.find_elem_by_XPATH_and_click(self.CURRENT_ADDED_EVENT)
        self.find_elem_by_ID_and_click(self.EDIT_BUTTON)
        self.find_elem_by_ID_and_click(self.CLEAR_NAME_BUTTON)
        self.add_name_to_task(name)
        self.click_save_button()
        self.navigate_back()
        return self.find_elem_by_ID(self.CURRENT_EVENT_NAME).text


    def mark_event_as_complete(self):
        self.find_elem_by_ID_and_click(self.HAMBURGER_MENU)
        self.find_elem_by_ID_and_click(self.ALL_EVENTS_BUTTON)
        self.find_elem_by_ID_and_click(self.CURRENT_TASK_CHECKBOX)

    def check_if_event_is_complete(self):
        self.find_elem_by_XPATH_and_click(self.CURRENT_ADDED_EVENT)
        return self.find_elem_by_ID(self.CURRENT_TASK_CHECKBOX).get_attribute("checked")

    def delete_added_event(self):
        self.find_elem_by_ID_and_click(self.HAMBURGER_MENU)
        self.find_elem_by_ID_and_click(self.ALL_EVENTS_BUTTON)
        self.find_elem_by_XPATH_and_click(self.CURRENT_ADDED_EVENT)
        self.find_elem_by_ID_and_click(self.DELETE_BUTTON)
        self.find_elem_by_ID_and_click(self.CONFIRM_DELETE_BUTTON)

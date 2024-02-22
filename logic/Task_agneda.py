from infra.Phone_instance import Phoneinstance



class TaskAgenda(Phoneinstance):

    #Homepage elements
    ADD_TASK = "com.claudivan.taskagenda:id/btNovoEvento"
    RIGHT_ARROW = "com.claudivan.taskagenda:id/ibtAvancar"
    LEFT_ARROW = "com.claudivan.taskagenda:id/ibtRetroceder"
    HAMBURGER_MENU = "com.claudivan.taskagenda:id/hamburguer"
    #1 = sunday , 7 = saturady
    DAY_ELEMENT = '//android.widget.LinearLayout[@resource-id="com.claudivan.taskagenda:id/containerColunasHorarios"]/android.widget.RelativeLayout'

    #hamburger menu elements
    ALL_EVENTS_BUTTON = "com.claudivan.taskagenda:id/btEventos"
    LATE_EVENT_BUTTON = "com.claudivan.taskagenda:id/btEventosAtrasados"
    COLOR_EVENT_TYPES = "com.claudivan.taskagenda:id/btCores"
    SETTING_BUTTON = "com.claudivan.taskagenda:id/btAjustes"

    #Add tasks elements
    TODAY_BUTTON_XPATH = '//android.widget.TextView[@resource-id="android:id/text1" and @text="Today"]'
    TOMORROW_BUTTON_XPATH = '//android.widget.TextView[@resource-id="android:id/text1" and @text="Tomorrow"]'
    OTHER_BUTTOM_XPATH = '//android.widget.TextView[@resource-id="android:id/text1" and @text="Other"]'

    #NEW event page
    EVENT_NAME_INPUT = 'com.claudivan.taskagenda:id/etTitulo'
    TIME_NAME_INPU = 'com.claudivan.taskagenda:id/btHora'
    DESCRRIPTION_INPU = 'com.claudivan.taskagenda:id/etDescricao'
    SAVE_BUTTON = 'com.claudivan.taskagenda:id/item_salvar'

    #AFTER ADDING EVENTS
    PENDING_EVENTS_BUTTON = 'com.claudivan.taskagenda:id/btEventosSemana'

    #CURRENT_EVENTS_PAGE
    COMPLETE_EVENT = 'com.claudivan.taskagenda:id/cbEventoConcluido'
    
    
    #After CLICKING ON DAY ELEMENT
    NEW_EVENT_BUTTON = '//android.widget.TextView[@resource-id="android:id/text1" and @text="New event"]'
    VIEW_EVENTS_BUTTON = '//android.widget.TextView[@resource-id="android:id/text1" and @text="View events"]'
    
    
    

    def __init__(self):        
        super().__init__()
        self.init_elements()

    def init_elements(self):
        pass

from kivymd.app import MDApp
from kivy.lang import Builder
from kivymd.uix.dialog import MDDialog
from kivymd.uix.boxlayout import MDBoxLayout
from kivymd.uix.pickers import MDDatePicker
from datetime import datetime

class DialogContent(MDBoxLayout):
    def __init__(self,**kwargs):
        super().__init__(**kwargs)   # calling the inherited function that is MDBOXLAYOUT
        self.ids.date_text.text=datetime.now().strftime("%A %d %B %Y")     # strftime format is monday 17 august 2023
    def show_date_picker(self):
        date_dialgog_variable=MDDatePicker()
        date_dialgog_variable.bind(on_save=self.on_save_func)
        date_dialgog_variable.open()

    def on_save_func(self,instance,value,range):
        date=value.strftime("%A %d %B %Y")
        self.ids.date_text.text=str(date)



class MainApp(MDApp):

    task_list_dialog=None  # flag
    def build(self):
        self.theme_cls.primary_palette="Teal"
        return Builder.load_file("My_Kivy_File.kv")
    # agr dialog nae hoga to ye bna dega
    def show_task_function(self):
        if not self.task_list_dialog:
            self.task_list_dialog=MDDialog(
                title="Create Task",
                type="custom",
                content_cls=DialogContent()
            )
            self.task_list_dialog.open()

    def close_dialog(self,*args):
        self.task_list_dialog.dismiss()

    def add_task(self,task,task_date):
        print(task.text,task_date)

if __name__=="__main__":
    MainApp().run()
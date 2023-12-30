from kivymd.app import MDApp
from kivymd.uix.dialog import MDDialog
from kivymd.uix.boxlayout import MDBoxLayout
from kivymd.uix.pickers import MDDatePicker

from kivymd.uix.list import TwoLineAvatarIconListItem, ILeftBody
from kivymd.uix.selectioncontrol import MDCheckbox

from datetime import datetime

class DialogContent(MDBoxLayout):
    # The init Function for class constructor
    def __init__(self, **kwargs):
        super().__init__(**kwargs)
        self.ids.date_text.text = datetime.now().strftime("%A %d %B %Y")
    
    # This Function will show the date picker
    def show_date_picker(self):
        date_dialog = MDDatePicker()
        date_dialog.bind(on_save = self.on_save)
        date_dialog.open()
        
    # This Function will get date and saves 
    def on_save(self, instance, value, date_range):
        date = value.strftime("%A %d %B %Y")
        self.ids.date_text.text = str(date)
        
# Class for marking and deleting the list item
class ListItemWithCheckbox(TwoLineAvatarIconListItem):
    def __init__(self, pk = None, **kwargs):
        super().__init__(**kwargs)
        self.pk = pk
        
    # Marking the item as complete or incomplete
    def mark(self, check, the_list_item):
        if check.active == True:
            the_list_item.text = "[s]" + the_list_item.text + "[/s]"
        else:
            pass
        
    # Deleting the list item
    def delete_item(self, the_list_item):
        self.parent.remove_widget(the_list_item)
        
class LeftCheckbox(ILeftBody, MDCheckbox):
    pass
            
# This is the main App
class MainApp(MDApp):
    # Flag
    task_list_dialog = None
    # This is the bulid Function for setting the theme
    def build(self):
        self.theme_cls.primary_palette = "Orange"
        
    # This is the show task Function
    def show_task_dialog(self):
        if not self.task_list_dialog:
            self.task_list_dialog = MDDialog(
                title = "Create Task",
                type = "custom",
                content_cls = DialogContent()
            )
            self.task_list_dialog.open()
            
    # Adding tasks
    def add_task(self, task, task_date):
        print(task.text, task_date)
        self.root.ids['container'].add_widget(ListItemWithCheckbox(text = '[b]' + task.text + '[/b]', secondary_text = task_date))
        task.text = ''
            
    # This is a dialog closing function
    def close_dialog(self, **args):
        self.task_list_dialog.dismiss()
    
if __name__=="__main__":
    app = MainApp()
    app.run()
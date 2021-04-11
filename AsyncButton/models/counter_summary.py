from datetime import datetime

class CounterSummary():
    name = False
    number_of_updates = 0
    last_execution = None
    current_value = None


    def __init__(self, name):
        self.name = name
        pass

    def update_value(self, new_value):
        
        self.current_value = new_value
        self.last_execution = datetime.now()
        self.number_of_updates += 1

        self._current_on_state = True
        pass
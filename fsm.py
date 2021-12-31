from transitions.extensions import GraphMachine

from utils import send_text_message


class TocMachine(GraphMachine):
    def __init__(self, **machine_configs):
        self.machine = GraphMachine(model=self, **machine_configs)

    def is_going_to_state1(self, event):
        print("is_going_to_state1")
        text = event.message.text
        return text.lower() == "go to state1"

    def is_going_to_state2(self, event):
        text = event.message.text
        return text.lower() == "go to state2"
    #
    def is_going_to_united_state(self, event):
        text = event.message.text
        return text.lower() == "go to united_state"
    #
    def on_enter_state1(self, event):
        print("I'm entering state1")
        reply_token = event.reply_token
        send_text_message(reply_token, "Trigger state1")
        self.go_back()

    def on_exit_state1(self):
        print("Leaving state1")

    def on_enter_state2(self, event):
        print("I'm entering state2")
        reply_token = event.reply_token
        send_text_message(reply_token, "Trigger state2")
        #self.go_back()

    def on_exit_state2(self):
        print("Leaving state2")
    
    #

    def on_enter_united_state(self, event):
        print("I'm entering united_state")
        reply_token = event.reply_token
        send_text_message(reply_token, "Trigger united_state")
        self.go_back()

    def on_exit_united_state(self):
        print("Leaving united_state")
    #
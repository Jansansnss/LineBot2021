from transitions.extensions import GraphMachine
from database import insert_data,print_data,update_data,delete_data
from utils import send_text_message


class TocMachine(GraphMachine):
    def __init__(self, **machine_configs):
        self.machine = GraphMachine(model=self, **machine_configs)
        #self.machine.get_graph().draw("myFSM.png", prog= 'dot')

    def is_going_to_state1(self, event):
        text = event.message.text
        return text.lower() == "go to state1"

    def is_going_to_state2(self, event):
        text = event.message.text
        return text.lower() == "go to state2"
    ##
    def is_going_to_united_state(self, event):
        text = event.message.text
        return text.lower() == "go to united_state"

    def is_going_to_p_name(self, event):
        text = event.message.text
        return text.lower() == "go to p_name"
    ##
    def on_enter_state1(self, event):
        print("I'm entering state1")
        reply_token = event.reply_token
        send_text_message(reply_token, "Trigger state1")
        self.go_back()

    def on_exit_state1(self):
        print("Leaving state1")

    def on_enter_state2(self, event):
        print("I'm entering state2")
        #print_data('pokemon','*')
        reply_token = event.reply_token
        send_text_message(reply_token, "Trigger state2")
        #self.go_back()
    
    ##
    def on_enter_united_state(self, event):
        print("I'm entering united_state")
        reply_token = event.reply_token
        send_text_message(reply_token, "Trigger united_state")
        self.go_back()

    def on_enter_p_name(self, event):
        print("I'm entering p_name")
        reply_token = event.reply_token
        #print_data('pokemon','*')
        send_text_message(reply_token, "Trigger p_name")
    
    def on_enter_search(self, event):
        print("I'm entering search")
        reply_token = event.reply_token
        #print_data('pokemon','*')
        print_data('pokemon',event.message.text)
        send_text_message(reply_token, "Trigger search")
        self.go_back()
    ##
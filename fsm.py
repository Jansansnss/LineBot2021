from transitions.extensions import GraphMachine
from database import *
from utils import send_text_message,send_multiple_text_message


class TocMachine(GraphMachine):
    def __init__(self, **machine_configs):
        self.machine = GraphMachine(model=self, **machine_configs)
        #self.machine.get_graph().draw("myFSM.png", prog= 'dot')


    """def is_going_to_state1(self, event):
        text = event.message.text
        return text.lower() == "go to state1"

    def on_enter_state1(self, event):
        print("I'm entering state1")
        reply_token = event.reply_token
        send_text_message(reply_token, "Trigger state1")
        self.go_back()



    def is_going_to_state2(self, event):
        text = event.message.text
        return text.lower() == "go to state2"

    def on_enter_state2(self, event):
        print("I'm entering state2")
        #print_data('pokemon','*')
        reply_token = event.reply_token
        send_text_message(reply_token, "Trigger state2")
        #self.go_back()



    def is_going_to_united_state(self, event):
        text = event.message.text
        return text.lower() == "go to united_state"

    def on_enter_united_state(self, event):
        print("I'm entering united_state")
        reply_token = event.reply_token
        send_text_message(reply_token, "Trigger united_state")
        self.go_back()"""



    def is_going_to_pokemon_name(self, event):
        text = event.message.text
        return text.lower() == "go to pokemon_name"

    def on_enter_pokemon_name(self, event):
        print("I'm entering pokemon_name")
        reply_token = event.reply_token
        #print_data('pokemon','*')
        send_text_message(reply_token, "Welcome\nPlz enter the pokemon's name\n(ex. Pikachu)")



    def is_going_to_search(self, event):
        return True

    def on_enter_search(self, event):
        print("I'm entering search")
        reply_token = event.reply_token
        #print_data('pokemon','*')
        print_data(event.message.text)
        send_text_message(reply_token,print_data(event.message.text))
        self.go_back()



    def is_going_to_developer(self, event):
        text = event.message.text
        return text.lower() == "jans is handsome"

    def on_enter_developer(self, event):
        print("I'm entering developer")
        reply_token = event.reply_token
        #print_data('pokemon','*')
        send_text_message(reply_token, "Trigger developer\n**WARNING**\nany changes may damage database")



    def is_going_to_sql(self, event):
        return True

    def on_enter_sql(self, event):
        print("I'm entering sql")
        developer_data_mode(event.message.text)
        reply_token = event.reply_token
        send_text_message(reply_token, "Back to user mode")
        self.go_back()


    
    def is_going_to_help(self, event):
        text = event.message.text
        return text.lower() == "help"

    def on_enter_help(self, event):
        print("I'm entering help")
        reply_token = event.reply_token
        send_text_message(reply_token, "\"go to pokemon_name\" and type pokemon's name(should be capitalized) to search")
        self.go_back()

    def is_going_to_demo(self, event):
        text = event.message.text
        return text.lower() == "demo"
    
    def on_enter_demo(self, event):
        print("I'm entering help")
        reply_token = event.reply_token
        send_text_message(reply_token, "Give me 3 points!!")
        self.go_back()
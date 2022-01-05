from fsm import TocMachine

def new_machine():
    machine = TocMachine(
        states=["user","pokemon_name","search","developer","sql","help","demo"],
        transitions=[
            {
                "trigger": "advance",
                "source": "user",
                "dest": "pokemon_name",
                "conditions": "is_going_to_pokemon_name",
            },
            {
                "trigger": "advance",
                "source": "pokemon_name",
                "dest": "search",
                "conditions": "is_going_to_search",
            },
            {
                "trigger": "advance",
                "source": "user",
                "dest": "developer",
                "conditions": "is_going_to_developer",
            },
            {
                "trigger": "advance",
                "source": "developer",
                "dest": "sql",
                "conditions": "is_going_to_sql",
            },
            {
                "trigger": "advance",
                "source": "user",
                "dest": "help",
                "conditions": "is_going_to_help",
            },
            {
                "trigger": "advance",
                "source": "user",
                "dest": "demo",
                "conditions": "is_going_to_demo",
            },
            {"trigger": "go_back", "source": ["search","sql","help","demo"], "dest": "user"},
        ],
        initial="user",
        auto_transitions=False,
        show_conditions=True,
    )

    """
    "state1", "state2","united_state"
            {
                "trigger": "advance",
                "source": "user",
                "dest": "state1",
                "conditions": "is_going_to_state1",
            },
            {
                "trigger": "advance",
                "source": "user",
                "dest": "state2",
                "conditions": "is_going_to_state2",
            },
            {
                "trigger": "advance",
                "source": "state2",
                "dest": "united_state",
                "conditions": "is_going_to_united_state",
            },
    """
    return machine
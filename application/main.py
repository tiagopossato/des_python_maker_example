from supervisor import Events, Event
from handle_event import handle_event
from time import sleep

def on_action(event: Event):
    """
    Action for event on
    """
    print(f"Running event {event.get_name()}")
    # do something like turn on a led

def off_action(event: Event):
    """
    Action for event off
    """
    print(f"Running event {event.get_name()}")
    # do something like turn off a led


# set default action for example
# Events['btn'].set_action(some_action)
Events['on'].set_action(on_action)
Events['off'].set_action(off_action)


if __name__ == '__main__':
    # handle events for teste
    while True:
        handle_event(Events['btn'])
        sleep(1)

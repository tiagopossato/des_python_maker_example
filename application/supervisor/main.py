from Supervisor import Events, Event, trigger_event

def default_action(event: Event):
    """
    Default action for example
    """
    print(f"Default action for event {event.get_name()}")

# set default action for example
Events['s1'].set_action(default_action)
Events['f1'].set_action(default_action)
Events['s2'].set_action(default_action)
Events['f2'].set_action(default_action)
Events['s4'].set_action(default_action)
Events['f4'].set_action(default_action)
Events['s5'].set_action(default_action)
Events['f5'].set_action(default_action)
Events['s3'].set_action(default_action)
Events['f3'].set_action(default_action)


if __name__ == '__main__':
    # handle events for teste
    trigger_event(Events['t1'])
    trigger_event(Events['t2'])
    trigger_event(Events['m6'])
    trigger_event(Events['m7'])
    trigger_event(Events['t5'])
    trigger_event(Events['p6'])
    trigger_event(Events['p7'])
    trigger_event(Events['t3'])
    trigger_event(Events['t4'])


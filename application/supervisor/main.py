from Supervisor import Events, Event, trigger_event

def default_action(event: Event):
    """
    Default action for example
    """
    print(f"Default action for event {event.get_name()}")

# set default action for example
Events['cv1_on'].set_action(default_action)
Events['cv1_off'].set_action(default_action)
Events['cv2_on'].set_action(default_action)
Events['cv2_off'].set_action(default_action)
Events['ppx_on'].set_action(default_action)
Events['ppx_off'].set_action(default_action)
Events['ppg_on'].set_action(default_action)
Events['ppg_off'].set_action(default_action)
Events['ppz_on'].set_action(default_action)
Events['ppz_off'].set_action(default_action)


if __name__ == '__main__':
    # handle events for teste
    trigger_event(Events['s1'])
    trigger_event(Events['s2'])
    trigger_event(Events['ppz_moving'])
    trigger_event(Events['ppx_moving'])
    trigger_event(Events['ppg_item'])
    trigger_event(Events['ppz_stoped'])
    trigger_event(Events['ppx_stoped'])
    trigger_event(Events['start'])
    trigger_event(Events['stop'])


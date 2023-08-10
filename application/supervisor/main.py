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
Events['s1'].set_action(default_action)
Events['s2'].set_action(default_action)
Events['ppx_on'].set_action(default_action)
Events['ppx_off'].set_action(default_action)
Events['ppg_on'].set_action(default_action)
Events['ppg_off'].set_action(default_action)
Events['ppz_on'].set_action(default_action)
Events['ppz_off'].set_action(default_action)
Events['ppz_moving'].set_action(default_action)
Events['ppx_moving'].set_action(default_action)
Events['ppg_item'].set_action(default_action)
Events['ppz_stoped'].set_action(default_action)
Events['ppx_stoped'].set_action(default_action)
Events['start'].set_action(default_action)
Events['stop'].set_action(default_action)


if __name__ == '__main__':
    # handle events for teste
    trigger_event(Events['cv1_on'])
    trigger_event(Events['cv1_off'])
    trigger_event(Events['cv2_on'])
    trigger_event(Events['cv2_off'])
    trigger_event(Events['s1'])
    trigger_event(Events['s2'])
    trigger_event(Events['ppx_on'])
    trigger_event(Events['ppx_off'])
    trigger_event(Events['ppg_on'])
    trigger_event(Events['ppg_off'])
    trigger_event(Events['ppz_on'])
    trigger_event(Events['ppz_off'])
    trigger_event(Events['ppz_moving'])
    trigger_event(Events['ppx_moving'])
    trigger_event(Events['ppg_item'])
    trigger_event(Events['ppz_stoped'])
    trigger_event(Events['ppx_stoped'])
    trigger_event(Events['start'])
    trigger_event(Events['stop'])

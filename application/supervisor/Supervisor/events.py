"""
Events from supremica file
"""
from . import Event, EventKind

# Create events
Events = {
    'cv1_on': Event(EventKind.CONTROLLABLE, 0, 'cv1_on'),
    'cv1_off': Event(EventKind.CONTROLLABLE, 1, 'cv1_off'),
    'cv2_on': Event(EventKind.CONTROLLABLE, 2, 'cv2_on'),
    'cv2_off': Event(EventKind.CONTROLLABLE, 3, 'cv2_off'),
    's1': Event(EventKind.UNCONTROLLABLE, 4, 's1'),
    's2': Event(EventKind.UNCONTROLLABLE, 5, 's2'),
    'ppx_on': Event(EventKind.CONTROLLABLE, 6, 'ppx_on'),
    'ppx_off': Event(EventKind.CONTROLLABLE, 7, 'ppx_off'),
    'ppg_on': Event(EventKind.CONTROLLABLE, 8, 'ppg_on'),
    'ppg_off': Event(EventKind.CONTROLLABLE, 9, 'ppg_off'),
    'ppz_on': Event(EventKind.CONTROLLABLE, 10, 'ppz_on'),
    'ppz_off': Event(EventKind.CONTROLLABLE, 11, 'ppz_off'),
    'ppz_moving': Event(EventKind.UNCONTROLLABLE, 12, 'ppz_moving'),
    'ppx_moving': Event(EventKind.UNCONTROLLABLE, 13, 'ppx_moving'),
    'ppg_item': Event(EventKind.UNCONTROLLABLE, 14, 'ppg_item'),
    'ppz_stoped': Event(EventKind.UNCONTROLLABLE, 15, 'ppz_stoped'),
    'ppx_stoped': Event(EventKind.UNCONTROLLABLE, 16, 'ppx_stoped'),
    'start': Event(EventKind.UNCONTROLLABLE, 17, 'start'),
    'stop': Event(EventKind.UNCONTROLLABLE, 18, 'stop'),
}

def get_event_by_id(event_id: int) -> Event:
    """
    Get event by id
    """
    if not isinstance(event_id, int):
        raise TypeError("event_id must be an integer")

    for event in Events.values():
        if event.get_id() == event_id:
            return event
    return None
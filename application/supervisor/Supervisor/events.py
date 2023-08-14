"""
Events from supremica file
"""
from . import Event, EventKind

# Create events
Events = {
    's1': Event(EventKind.CONTROLLABLE, 0, 's1'),
    'f1': Event(EventKind.CONTROLLABLE, 1, 'f1'),
    's2': Event(EventKind.CONTROLLABLE, 2, 's2'),
    'f2': Event(EventKind.CONTROLLABLE, 3, 'f2'),
    't1': Event(EventKind.UNCONTROLLABLE, 4, 't1'),
    't2': Event(EventKind.UNCONTROLLABLE, 5, 't2'),
    's4': Event(EventKind.CONTROLLABLE, 6, 's4'),
    'f4': Event(EventKind.CONTROLLABLE, 7, 'f4'),
    's5': Event(EventKind.CONTROLLABLE, 8, 's5'),
    'f5': Event(EventKind.CONTROLLABLE, 9, 'f5'),
    's3': Event(EventKind.CONTROLLABLE, 10, 's3'),
    'f3': Event(EventKind.CONTROLLABLE, 11, 'f3'),
    'm6': Event(EventKind.UNCONTROLLABLE, 12, 'm6'),
    'm7': Event(EventKind.UNCONTROLLABLE, 13, 'm7'),
    't5': Event(EventKind.UNCONTROLLABLE, 14, 't5'),
    'p6': Event(EventKind.UNCONTROLLABLE, 15, 'p6'),
    'p7': Event(EventKind.UNCONTROLLABLE, 16, 'p7'),
    't3': Event(EventKind.UNCONTROLLABLE, 17, 't3'),
    't4': Event(EventKind.UNCONTROLLABLE, 18, 't4'),
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
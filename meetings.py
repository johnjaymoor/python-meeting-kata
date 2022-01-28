def get_free_slots(calendar1, daily_bounds1, calendar2, daily_bounds2, meeting_duration):
    """
    Return the available slots of time from two calendars,
    two daily bounds and the meeting duration in minutes.
    
    :param calendar1:
    :param daily_bounds1:
    :param calendar2:
    :param daily_bounds2:
    :param meeting_duration:
    :return: []
    """
    free_slots_1 = _find_free_slots(calendar1, daily_bounds1, meeting_duration)
    free_slots_2 = _find_free_slots(calendar2, daily_bounds2, meeting_duration)
    return _get_intersection_slots(free_slots_1, free_slots_2, meeting_duration)


def _find_free_slots(calendar, daily_bounds, meeting_duration):
    free_slots = []
    start_time, end_time = daily_bounds
    for hour, minute in calendar:
        if _is_slot_long_enough(start_time, hour, meeting_duration):
            free_slots.append([start_time, hour])
        start_time = minute
    if _is_slot_long_enough(start_time, end_time, meeting_duration):
        free_slots.append([start_time, end_time])
    return free_slots


def _is_slot_long_enough(start_time, end_time, meeting_duration):
    slot_start_in_minutes = _strtime_to_min(start_time)
    slot_end_in_minutes = _strtime_to_min(end_time)
    return True if meeting_duration <= (slot_end_in_minutes - slot_start_in_minutes) else False


def _get_intersection_slots(free_slots_1, free_slots_2, meeting_duration):
    intersect_time_slots = []
    for slot1 in free_slots_1:
        for slot2 in free_slots_2:
            _add_intersect_slots(meeting_duration, intersect_time_slots, slot1, slot2)
    return intersect_time_slots


def _add_intersect_slots(meeting_duration, intersect_time_slots, slot1, slot2):
    if _starts_slot1_inside_slot2(slot1, slot2):
        if _strtime_to_min(slot2[1]) - _strtime_to_min(slot1[0]) >= meeting_duration:
            intersect_time_slots.append([slot1[0], slot2[1]])
    elif _starts_slot1_inside_slot2(slot2, slot1):
        if _strtime_to_min(slot1[1]) - _strtime_to_min(slot2[0]) >= meeting_duration:
            intersect_time_slots.append([slot2[0], slot1[1]])


def _starts_slot1_inside_slot2(slot1, slot2):
    return True if _strtime_to_min(slot1[0]) >= _strtime_to_min(slot2[0]) \
                   and _strtime_to_min(slot1[0]) <= _strtime_to_min(slot2[1]) \
        else False


def _strtime_to_min(slot_time):
    hour, minute = slot_time.split(':')
    return int(hour) * 60 + int(minute)

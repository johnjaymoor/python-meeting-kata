import datetime

"""
Meeting problem:
Two people with a very busy calendar are trying to meet today.
Write an algorithm that takes two people calendars returning free slots of time
during these two people may meet.
Input:
* Two calendars with the slots currently taken today for both people.
* Daily bounds.
* Meeting duration.
Output: A list of slots in which they may meet.
This problem was taken from this video, but with a different implementation:
https://www.youtube.com/watch?v=kbwk1Tw3OhE
"""


def calculate_free_slots_for_meeting(calendar1, daily_bounds1, calendar2, daily_bounds2, meeting_duration):
    free_slots_1 = get_free_slots_in_calendar_base_on_meeting_duration(calendar1, daily_bounds1, meeting_duration)
    free_slots_2 = get_free_slots_in_calendar_base_on_meeting_duration(calendar2, daily_bounds2, meeting_duration)
    return get_min_intersection_slots(free_slots_1, free_slots_2, meeting_duration)


def get_free_slots_in_calendar_base_on_meeting_duration(calendar, daily_bounds, meeting_duration):
    free_slots = []
    start_time = daily_bounds[0]
    for slot in calendar:
        if is_slot_long_enough_for_meeting_duration(start_time, slot[0], meeting_duration):
            free_slots.append([start_time, slot[0]])
        start_time = slot[1]
    if is_slot_long_enough_for_meeting_duration(start_time, daily_bounds[1], meeting_duration):
        free_slots.append([start_time, daily_bounds[1]])
    return free_slots


def is_slot_long_enough_for_meeting_duration(start_time, end_time, meeting_duration):
    slot_start_in_minutes = get_slot_time_in_minutes(start_time)
    slot_end_in_minutes = get_slot_time_in_minutes(end_time)
    return True if meeting_duration <= (slot_end_in_minutes - slot_start_in_minutes) else False


def get_min_intersection_slots(free_slots_1, free_slots_2, meeting_duration):
    intersect_time_slots = []
    for slot1 in free_slots_1:
        for slot2 in free_slots_2:
            add_intersect_slots(meeting_duration, intersect_time_slots, slot1, slot2)
    return intersect_time_slots


def add_intersect_slots(meeting_duration, intersect_time_slots, slot1, slot2):
    if is_slot_starting_inside(slot1, slot2):
        if get_slot_time_in_minutes(slot2[1]) - get_slot_time_in_minutes(slot1[0]) >= meeting_duration:
            intersect_time_slots.append([slot1[0], slot2[1]])
    elif is_slot_starting_inside(slot2, slot1):
        if get_slot_time_in_minutes(slot1[1]) - get_slot_time_in_minutes(slot2[0]) >= meeting_duration:
            intersect_time_slots.append([slot2[0], slot1[1]])


def is_slot_starting_inside(slot1, slot2):
    return True if get_slot_time_in_minutes(slot1[0]) >= get_slot_time_in_minutes(
        slot2[0]) and get_slot_time_in_minutes(slot1[0]) <= get_slot_time_in_minutes(slot2[1]) else False


def get_slot_time_in_minutes(slot_time):
    return int(slot_time.split(':')[0]) * 60 + int(slot_time.split(':')[1])

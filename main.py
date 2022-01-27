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

calendar1 = [('8:00', '9:00'), ('9:00', '10:00'), ('12:00', '13:00'), ('13:30', '14:00')]
calendar2 = [('8:00', '9:00'), ('9:00', '11:00'), ('12:00', '13:00'), ('13:30', '14:00')]
daily_bounds = ('8:00', '15:00')
duration = 60
result = [("11:00", "12:00"), ("14:00", "15:00")]


def calculate_free_slots(calendar1, calendar2, daily_bounds, duration):
    free_slots_1 = get_free_slots(calendar1, daily_bounds, duration)
    free_slots_2 = get_free_slots(calendar2, daily_bounds, duration)
    return get_min_intersection_slots(free_slots_1, free_slots_2)


def get_free_slots(calendar, daily_bounds, duration):
    pass


def get_min_intersection_slots(free_slots_1, free_slots_2):
    pass

from typing import List


class Slot:
    start: str
    end: str

    def __init__(self, slot: list):
        self.start, self.end = slot

    def starts_inside(self, other: "Slot") -> bool:
        """
        Return true if slot start time starts inside the other slot

        :param other: Slot
        :return: bool
        """
        return True if other.get_start_in_minutes() \
                       <= self.get_start_in_minutes() \
                       <= other.get_end_in_minutes() else False

    def get_start_in_minutes(self) -> int:
        return Slot.strtime_to_minute(self.start)

    def get_end_in_minutes(self) -> int:
        return Slot.strtime_to_minute(self.end)

    @classmethod
    def strtime_to_minute(cls, slot_time: str) -> int:
        """
        Return the minutes passed since 00:00 from a time string with HH:MM format

        :param slot_time: str [HH:MM]
        :return: int
        """
        hour, minute = slot_time.split(':')
        return int(hour) * 60 + int(minute)


class Calendar:
    slots: List[Slot]

    def __init__(self, slots: list):
        self.slots = [Slot(slot) for slot in slots]

    def append(self, slot: Slot):
        self.slots.append(slot)

    def get_free_slots(self, daily_bounds: Slot) -> "Calendar":
        """
        Return a Calendar with free slots between daily bounds

        :param daily_bounds: Slot with daily boundaries
        :return: Calendar
        """
        free_slots = Calendar([])
        start_time, end_time = daily_bounds.start, daily_bounds.end
        for slot in self.slots:
            if start_time != slot.start:
                free_slots.append(Slot([start_time, slot.start]))
            start_time = slot.end
        if start_time != end_time:
            free_slots.append(Slot([start_time, end_time]))
        return free_slots

    def intersects(self, calendar: "Calendar") -> "Calendar":
        """
        Intersection between calendars
        
        :param calendar: 
        :return: Calendar
        """
        intersect_time_slots = Calendar([])
        for slot1 in self.slots:
            for slot2 in calendar.slots:
                if slot1.starts_inside(slot2):
                    intersect_time_slots.append(Slot([slot1.start, slot2.end]))
                elif slot2.starts_inside(slot1):
                    intersect_time_slots.append(Slot([slot2.start, slot1.end]))
        return intersect_time_slots


def get_free_slots(slots1: list, daily_bounds1: list, slots2: list, daily_bounds2: list, meeting_duration: int):
    """
    Return the available slots of time from two calendars,
    two daily bounds and the meeting duration in minutes.

    :param slots1:
    :param daily_bounds1:
    :param slots2:
    :param daily_bounds2:
    :param meeting_duration:
    :return:
    """
    calendar1 = Calendar(slots1)
    calendar2 = Calendar(slots2)
    daily_slot1 = Slot(daily_bounds1)
    daily_slot2 = Slot(daily_bounds2)
    calendar_free_slots_1 = calendar1.get_free_slots(daily_slot1)
    calendar_free_slots_2 = calendar2.get_free_slots(daily_slot2)
    calendar_intersection = calendar_free_slots_1.intersects(calendar_free_slots_2)
    meeting_matching_slots = []
    for slot in calendar_intersection.slots:
        if slot.get_end_in_minutes() - slot.get_start_in_minutes() >= meeting_duration:
            meeting_matching_slots.append([slot.start, slot.end])
    return meeting_matching_slots

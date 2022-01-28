import unittest
import free_calendar_slots_finder


class TestFreeCalendarSlotsFinder(unittest.TestCase):
    def test_1(self):
        calendar1 = [['8:00', '9:00'], ['9:00', '10:00'], ['12:00', '13:00'], ['13:30', '14:00']]
        daily_bound1 = ['8:00', '15:00']
        calendar2 = [['8:00', '9:00'], ['9:00', '11:00'], ['12:00', '13:00'], ['13:30', '14:00']]
        daily_bound2 = ['8:00', '15:00']
        duration = 60
        result = [["11:00", "12:00"], ["14:00", "15:00"]]
        self.assertEqual(result,
                         free_calendar_slots_finder.calculate_free_slots_for_meeting(calendar1, daily_bound1, calendar2,
                                                                                     daily_bound2, duration))

    def test_2(self):
        calendar1 = [['9:00', '10:30'], ['12:00', '13:00'], ['16:00', '18:00']]
        daily_bound1 = ['9:00', '20:00']
        calendar2 = [['10:00', '11:30'], ['12:30', '14:30'], ['14:30', '15:00'], ['16:00', '17:00']]
        daily_bound2 = ['9:00', '18:30']
        duration = 30
        result = [["11:30", "12:00"], ["15:00", "16:00"], ["18:00", "18:30"]]
        self.assertEqual(result,
                         free_calendar_slots_finder.calculate_free_slots_for_meeting(calendar1, daily_bound1, calendar2,
                                                                                     daily_bound2, duration))

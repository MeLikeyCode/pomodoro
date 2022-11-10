import unittest
import time
from pomodoro import Pomodoro, OFF, WORK, BREAK, LONG_BREAK

class TestPomodoro(unittest.TestCase):
    def test_pomodoro_basics(self):
        p = Pomodoro()
        p.work_length = 20
        p.break_length = 5
        p.long_break_length = 10

        p.start()
        self.assertEqual(p.state, WORK, "initial state after start should be WORK")

        # 1st work
        time.sleep(3)
        self.assertTrue(p.time_remaining < 18, "time remaining should be less than 18 seconds after 3 seconds")

        time.sleep(3)
        self.assertTrue(p.time_remaining < 15, "time remaining should be less than 15 seconds after 6 seconds")

        time.sleep(14)

        # 1st break
        self.assertEqual(p.state, BREAK, "state should be BREAK after 20 seconds")
        self.assertTrue(p.time_remaining <= 5 and p.time_remaining >= 3, "break time remaining should be about 5 seconds initially")
        self.assertEqual(p.num_works_done, 1)

        time.sleep(1)
        self.assertTrue(p.time_remaining < 5, "time remaining should still be less than 5")
        time.sleep(4)

        for i in range(3):
            # 2nd work (then 3rd, then 4th)
            self.assertEqual(p.state, WORK)
            time.sleep(20)

            if i < 2:
                self.assertEqual(p.state, BREAK)
                time.sleep(5)
            else:
                self.assertEqual(p.state, LONG_BREAK, "state should be LONG_BREAK after 4th work")

        time.sleep(10)
        self.assertEqual(p.state, WORK, "state should be WORK after long break time is up")
        self.assertEqual(p.num_rounds_done, 1)
        self.assertEqual(p.state, WORK)
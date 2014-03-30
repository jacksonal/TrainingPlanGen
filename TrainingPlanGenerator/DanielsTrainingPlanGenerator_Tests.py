"""Unit test case for DanielsTrainingPlanGenerator"""

import unittest

from DanielsTrainingPlanGenerator import *


class TestDanielsFormula(unittest.TestCase):
    """Unit Test case for Daniel's Running Formula plan generator"""

    def setUp(self):
        """Setup for testing."""
        self.generator = DanielsTrainingPlanGenerator()

    def test_setup(self):
        """confirm setup occurred"""
        self.assertIsNotNone(self.generator)

    def test_12_weeks(self):
        #12 week plan: 4 phases; base, early quality, transition quality, final quality
        plan = self.generator.generate_training_plan(12)
        self.assertEqual(len(plan.get_phases()), 4)

        #confirm 12 weeks split between 4 phases
        phase = plan.get_phase(0)
        self.assertEqual(len(phase), 3)
        phase = plan.get_phase(1)
        self.assertEqual(len(phase), 3)
        phase = plan.get_phase(2)
        self.assertEqual(len(phase), 3)
        phase = plan.get_phase(3)
        self.assertEqual(len(phase), 3)

    def test_9_weeks(self):
        #9 week plan: 3 phases; base, transition quality, final quality
        plan = self.generator.generate_training_plan(9)
        self.assertEqual(len(plan.get_phases()), 4)

        #confirm 9 weeks split between 3 phases
        phase = plan.get_phase(0)
        self.assertEqual(len(phase), 3)
        phase = plan.get_phase(1)
        self.assertEqual(len(phase), 0)
        phase = plan.get_phase(2)
        self.assertEqual(len(phase), 3)
        phase = plan.get_phase(3)
        self.assertEqual(len(phase), 3)

    def test_6_weeks(self):
        #6 week plan: 2 phases; base, final quality
        plan = self.generator.generate_training_plan(6)
        self.assertEqual(len(plan.get_phases()), 4)

        #confirm 6 weeks split between 2 phases
        phase = plan.get_phase(0)
        self.assertEqual(len(phase), 3)
        phase = plan.get_phase(1)
        self.assertEqual(len(phase), 0)
        phase = plan.get_phase(2)
        self.assertEqual(len(phase), 0)
        phase = plan.get_phase(3)
        self.assertEqual(len(phase), 3)

    def test_3_weeks(self):
        #3 week plan: 1 phase; base
        plan = self.generator.generate_training_plan(3)

        #first phase only. 3 weeks.
        phase = plan.get_phase(0)
        self.assertEqual(len(phase), 3)
        phase = plan.get_phase(1)
        self.assertEqual(len(phase), 0)
        phase = plan.get_phase(2)
        self.assertEqual(len(phase), 0)
        phase = plan.get_phase(3)
        self.assertEqual(len(phase), 0)

    def test_basic_plan(self):
        """create a basic Daniels training plan and confirm number
            of weeks and phases
        """
        #Still want 4 phases even if a phase would have 0 weeks.

        #3 week plan: 1 phase; base
        plan = self.generator.generate_training_plan(3)
        self.assertEqual(len(plan.get_phases()), 4)

        #6 week plan: 2 phases; base, final quality
        plan = self.generator.generate_training_plan(6)
        self.assertEqual(len(plan.get_phases()), 4)

        #9 week plan: 3 phases; base, transition quality, final quality
        plan = self.generator.generate_training_plan(9)
        self.assertEqual(len(plan.get_phases()), 4)

        #12 week plan: 4 phases; base, early quality, transition quality, final quality
        plan = self.generator.generate_training_plan(12)
        self.assertEqual(len(plan.get_phases()), 4)

    def test_max_weeks(self):
        """test plan doesn't go over 24 weeks"""
        plan = self.generator.generate_training_plan(26)

        #confirm 24 weeks split between 4 phases
        phase = plan.get_phase(0)
        self.assertEqual(len(phase), 6)
        phase = plan.get_phase(1)
        self.assertEqual(len(phase), 6)
        phase = plan.get_phase(2)
        self.assertEqual(len(phase), 6)
        phase = plan.get_phase(3)
        self.assertEqual(len(phase), 6)

    def test_e_pace(self):
        """test e pace formula is aproximately correct"""
        #6:45 E Pace
        pace = DanielsTrainingPlan.get_E_pace(64)
        self.assertAlmostEqual(405, pace, delta=2)

        #9:28 E Pace
        pace = DanielsTrainingPlan.get_E_pace(42)
        self.assertAlmostEqual(568, pace, delta=2)

        #6:00 E Pace
        pace = DanielsTrainingPlan.get_E_pace(74)
        self.assertAlmostEqual(360, pace, delta=2)

        #11:09 E Pace
        pace = DanielsTrainingPlan.get_E_pace(34)
        self.assertAlmostEqual(669, pace, delta=2)

        #7:31 E Pace
        pace = DanielsTrainingPlan.get_E_pace(56)
        self.assertAlmostEqual(451, pace, delta=2)

    def test_mp_pace(self):
        """test mp pace formula is aproximately correct"""
        #5:54 MP Pace
        pace = DanielsTrainingPlan.get_MP_pace(64)
        self.assertAlmostEqual(354, pace, delta=2)

        #8:25 MP Pace
        pace = DanielsTrainingPlan.get_MP_pace(42)
        self.assertAlmostEqual(505, pace, delta=2)

        #5:12 MP Pace
        pace = DanielsTrainingPlan.get_MP_pace(74)
        self.assertAlmostEqual(312, pace, delta=2)

        #10:00 MP Pace
        pace = DanielsTrainingPlan.get_MP_pace(34)
        self.assertAlmostEqual(600, pace, delta=2)

        #6:37 MP Pace
        pace = DanielsTrainingPlan.get_MP_pace(56)
        self.assertAlmostEqual(397, pace, delta=2)

    def test_t_pace(self):
        """test t pace formula is aproximately correct"""
        #5:36 T Pace
        pace = DanielsTrainingPlan.get_T_pace(64)
        self.assertAlmostEqual(336, pace, delta=2)

        #7:52 T Pace
        pace = DanielsTrainingPlan.get_T_pace(42)
        self.assertAlmostEqual(472, pace, delta=2)

        #4:59 T Pace
        pace = DanielsTrainingPlan.get_T_pace(74)
        self.assertAlmostEqual(299, pace, delta=2)

        #9:20 T Pace
        pace = DanielsTrainingPlan.get_T_pace(34)
        self.assertAlmostEqual(560, pace, delta=2)

        #6:15 T Pace
        pace = DanielsTrainingPlan.get_T_pace(56)
        self.assertAlmostEqual(375, pace, delta=2)

    def test_i_pace(self):
        """test t pace formula is approximately correct"""
        #5:08 I pace
        pace = DanielsTrainingPlan.get_I_pace(64)
        self.assertAlmostEqual(308 / 4, pace, delta=2)

        #7:12 I Pace
        pace = DanielsTrainingPlan.get_I_pace(42)
        self.assertAlmostEqual(432 / 4, pace, delta=2)

        #4:34 I Pace
        pace = DanielsTrainingPlan.get_I_pace(74)
        self.assertAlmostEqual(274 / 4, pace, delta=2)

        #8:32 I Pace
        pace = DanielsTrainingPlan.get_I_pace(34)
        self.assertAlmostEqual(128, pace, delta=4)

        #5:44 I Pace
        pace = DanielsTrainingPlan.get_I_pace(56)
        self.assertAlmostEqual(344 / 4, pace, delta=2)

    def test_r_pace(self):
        """test r pace formula is approximately correct"""

        #2:16 R pace
        pace = DanielsTrainingPlan.get_R_pace(64)
        self.assertAlmostEqual(71, pace, delta=2)

        #1:42 R Pace
        pace = DanielsTrainingPlan.get_R_pace(42)
        self.assertAlmostEqual(102, pace, delta=2)

        #62 R Pace
        pace = DanielsTrainingPlan.get_R_pace(74)
        self.assertAlmostEqual(62, pace, delta=2)

        #2:02 R Pace
        pace = DanielsTrainingPlan.get_R_pace(34)
        self.assertAlmostEqual(122, pace, delta=4)

        #80 R Pace
        pace = DanielsTrainingPlan.get_R_pace(56)
        self.assertAlmostEqual(80, pace, delta=2)

    def test_estimate_vdot(self):
        """validate vdot interpolation function"""
        self.fail('not implemented yet')

    def test_print_workout(self):
        w = DanielsTrainingWorkout()
        w.desc = "E"
        self.assertEqual(w.desc, '%s' % w)
        pass

    def test_print_day(self):
        d = DanielsTrainingDay()
        d.set_day_of_week(1)
        w = DanielsTrainingWorkout()
        w.desc = 'E'
        d.add_workout(w)
        w = DanielsTrainingWorkout()
        w.desc = '2 x 5 min @ T'
        d.add_workout(w)
        day_string = 'Day %i workouts:' % d.get_day_of_week()
        for workout in d.get_workouts():
            day_string += '\n\t%r' % workout
        print d.get_pretty_print(0)
        self.assertEqual(day_string, '%s' % d)

    def test_print_week(self):
        self.fail('not implemented yet')

    def test_print_phase(self):
        self.fail('not implemented yet')

    def test_print_plan(self):
        self.fail('not implemented yet')


if __name__ == '__main__':
    unittest.main()

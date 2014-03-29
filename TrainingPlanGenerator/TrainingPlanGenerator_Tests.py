"""
Unit Tests
"""
import TrainingPlanGenerator
import unittest


class TestBaseFunctions(unittest.TestCase):
    """Test case for basic TrainingPlanGenerator"""

    def setUp(self):
        """Setup basic test environment. A plan with one phase"""
        self.plan = TrainingPlanGenerator.TrainingPlan()
        self.phase1 = TrainingPlanGenerator.TrainingPhase(1)
        self.phase2 = TrainingPlanGenerator.TrainingPhase(2)
        self.plan.add_phase(self.phase1)
        self.plan.add_phase(self.phase2)

    def test_setup(self):
        """Confirm setup."""
        self.assertEqual(len(self.plan.get_phases()), 2)
        self.assertEqual(self.phase1.phasenum, 1)

    def test_getweek(self):
        """test the get week method"""
        #add some weeks
        self.phase1.extend_weeks([1, 2, 3])
        self.phase2.extend_weeks([4, 5, 6])
        self.assertEqual(len(self.phase2), 3)
        #check phase 1 week at index 1 is 2
        week = self.phase1.get_week(1)
        self.assertEqual(week, 2)
        #check plan week at index 1 is 2
        week = self.plan.get_week(1)
        self.assertEqual(week, 2)
        #try a week in phase 2
        week = self.plan.get_week(4)
        self.assertEqual(week, 5)


if __name__ == '__main__':
    unittest.main()


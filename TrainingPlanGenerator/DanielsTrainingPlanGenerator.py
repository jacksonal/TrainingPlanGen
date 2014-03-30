"""
Classes that extend TrainingPlanGenerator to create a training plan for
distance running following the methodology laid out in 'Daniel's Running Formula'.
"""
from TrainingPlanGenerator import *


class DanielsTrainingPlanGenerator(TrainingPlanGenerator):
    """Extends TrainingPlanGenerator. Creates a training plan based on
        given variables.
    """

    def __init__(self):
        self.vdot = -1

    def generate_training_plan(self, numweeks):
        """Return a DanielsTrainingPlan with the number of weeks specified
            divided into phases.
            :rtype : DanielsTrainingPlan
        """
        plan = DanielsTrainingPlan()
        #fill out phases here
        plan.add_weeks(numweeks)

        return plan


###########################################################################

class DanielsTrainingPlan(TrainingPlan):
    """
        Extends TrainingPlan. Defines a Daniels Running Formula training plan.
            -Consists of 4 phases typically. Foundation, Early Quality,
                Transition Quality, and Final Quality
    """

    def __init__(self):
        """initialize a Daniels Running Formula Training plan. Creates 4 phases"""
        super(DanielsTrainingPlan, self).__init__()
        self.add_phase(DanielsTrainingPhase(1))
        self.add_phase(DanielsTrainingPhase(2))
        self.add_phase(DanielsTrainingPhase(3))
        self.add_phase(DanielsTrainingPhase(4))
        self.numweeks = 0

    def __str__(self):
        ret = '%d week plan:' % self.numweeks
        i = 0
        for phase in self.get_phases():
            if len(phase) > 0:
                i += 1
                phase.phasenum = i
                ret += '\n\t%s' % phase
        return ret

    def add_weeks(self, numweeks):
        """Adds a week to the appropriate phase and calls self recursively.
            Max weeks allowed is 24.
        """
        if 0 < numweeks:
            self.add_weeks(numweeks - 1)
            if numweeks <= 24:
                if numweeks == 24 or numweeks == 22 or numweeks == 17 or 3 < numweeks < 7:
                    phase = self.get_phase(3)
                    week = DanielsTrainingWeek()
                    week.weeknum = numweeks
                    phase.add_week(week)
                    self.numweeks += 1
                elif 13 < numweeks < 17 or 6 < numweeks < 10:
                    phase = self.get_phase(2)
                    week = DanielsTrainingWeek()
                    week.weeknum = numweeks
                    phase.add_week(week)
                    self.numweeks += 1
                elif 17 < numweeks < 21 or 9 < numweeks < 13:
                    phase = self.get_phase(1)
                    week = DanielsTrainingWeek()
                    week.weeknum = numweeks
                    phase.add_week(week)
                    self.numweeks += 1
                elif numweeks == 23 or numweeks == 21 or numweeks == 13 or numweeks < 4:
                    phase = self.get_phase(0)
                    week = DanielsTrainingWeek()
                    week.weeknum = numweeks
                    phase.add_week(week)
                    self.numweeks += 1

    @staticmethod
    def estimate_vdot(distance, time):
        """Estimate VDOT value given race distance and time."""
        if distance == 'HALF':
            pass
        elif distance == '5K':
            pass
        elif distance == 'MILE':
            pass

    @staticmethod
    def get_E_pace(vdot):
        """
        Calculate Mile E Pace based on vdot
        ALL PACES ARE APPROXIMATE.
        :param vdot:
        :rtype : int
        """
        pace = -1 * (((vdot ** 5) -
                      (400 * (vdot ** 4)) +
                      (65500 * (vdot ** 3)) -
                      (5640000 * (vdot ** 2)) +
                      (273040000 * vdot) -
                      7528000000) /
                     4000000)
        return pace

    @staticmethod
    def get_MP_pace(vdot):
        """
        Calculate Mile MP pace based on vdot
        ALL PACES ARE APPROXIMATE.
        :param vdot:
        :rtype : int
        """
        pace = -1 * (((vdot ** 5) -
                      (310 * (vdot ** 4)) +
                      (39500 * (vdot ** 3)) -
                      (2675000 * (vdot ** 2)) +
                      (103860000 * vdot) -
                      2342400000) /
                     1200000)

        return pace

    @staticmethod
    def get_T_pace(vdot):
        """
        Calculate Mile T pace based on vdot
        ALL PACES ARE APPROXIMATE.
        :param vdot:
        :rtype : int
        """
        pace = -1 * (((6 * (vdot ** 5)) -
                      (1825 * (vdot ** 4)) +
                      (226500 * (vdot ** 3)) -
                      (14787500 * (vdot ** 2)) +
                      (545190000 * vdot) -
                      11538000000) /
                     6000000)

        return pace

    @staticmethod
    def get_I_pace(vdot):
        """
        Calculate 400m I pace based on vdot
        ALL PACES ARE APPROXIMATE.
        :param vdot:
        :rtype : int
        """
        pace = -1 * (((43 * (vdot ** 6)) -
                      (14365 * (vdot ** 5)) +
                      (1958500 * (vdot ** 4)) -
                      (139117500 * (vdot ** 3)) +
                      (5406220000 * (vdot ** 2)) -
                      (107825600000 * vdot) +
                      814080000000) /
                     300000000)
        return pace

    @staticmethod
    def get_R_pace(vdot):
        """
        Calculate 400m R pace based on vdot
        ALL PACES ARE APPROXIMATE.
        :param vdot:
        :rtype : int
        """
        pace = -1 * (((43 * (vdot ** 6)) -
                      (14365 * (vdot ** 5)) +
                      (1958500 * (vdot ** 4)) -
                      (139117500 * (vdot ** 3)) +
                      (5406220000 * (vdot ** 2)) -
                      (107825600000 * vdot) +
                      815880000000) /
                     300000000)

        return pace


###########################################################################

class DanielsTrainingPhase(TrainingPhase):
    """Extends TrainingPhase."""

    def __init__(self, phasenum):
        super(DanielsTrainingPhase, self).__init__(phasenum)
        if phasenum == 1:
            self.desc = 'Foundation'
        elif phasenum == 2:
            self.desc = 'Early Quality'
        elif phasenum == 3:
            self.desc = 'Transition Quality'
        elif phasenum == 4:
            self.desc = 'Final Quality'
        else:
            raise PhaseNumberException('Daniels training plans do not have more than 4 phases.')

    def __repr__(self):
        ret = 'Phase %i (' % self.phasenum
        for week in self.get_weeks():
            ret += ' %r,' % week
        ret = '%s )' % ret[:-1]
        return ret

    def __str__(self):
        return 'Phase %d (%s): %d weeks' % (self.phasenum, self.desc, self.get_num_weeks())


###########################################################################

class DanielsTrainingWeek(TrainingWeek):
    """Extends TrainingWeek"""

    def __repr__(self):
        ret = 'Week %i (' % self.weeknum
        for day in self.get_days():
            ret += ' %r,' % day
        ret = '%s )' % ret[:-1]
        return ret


###########################################################################

class DanielsTrainingDay(TrainingDay):
    """Defines a day of training. May contain 0 or more workouts."""



    ###########################################################################


class DanielsTrainingWorkout():
    """Defines a Daniels workout."""

    def __init__(self):
        """Initialize the workout instance"""
        self.desc = ""

    def __repr__(self):
        return self.desc

    def get_pretty_print(self, tabs):
        """return string for printing human readable workout"""
        ret = '\t' * tabs
        ret += self.desc
        return ret


if __name__ == '__main__':
    gen = DanielsTrainingPlanGenerator()
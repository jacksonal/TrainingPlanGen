"""
TrainingPlanGenerator
 Defines an api for implementing specific training plan generation tools.
"""


class TrainingPlanGenerator(object):
    """Abstract class to define training plan generator structure."""

    def generate_training_plan(self, numweeks):
        """When implemented, returns a TrainingPlan object.
            :rtype : TrainingPlan
        """
        raise NotImplementedError("Method not implemented")


###########################################################################

class TrainingPlan(object):
    """Abstract class. Defines a training plan divided into
        TrainingPhase objects
    """

    def __init__(self):
        """Base TrainingPlan constructor"""
        self.__phaseList = []

    def __len__(self):
        ret = 0
        for phase in self.__phaseList:
            ret += len(phase)
        return ret

    def get_phase(self, phasenum):
        """Returns the phase with the specified phase index
            if phase_num would result in an OutOfRange exception,
            None is returned
        :rtype : TrainingPhase
        :type phasenum: int
        """
        if (phasenum > len(self.__phaseList) - 1) or phasenum < 0:
            return None
        return self.__phaseList[phasenum]

    def get_week(self, weekindex):
        """Return the TrainingWeek of this plan specified by Week"""
        weeks_to_go = weekindex
        for phase in self.__phaseList:
            if weeks_to_go < len(phase):
                return phase.get_week(weeks_to_go)
            weeks_to_go -= len(phase)
        return None

    def add_phase(self, phase):
        """Adds a phase to the plan"""
        self.__phaseList.append(phase)

    def get_phases(self):
        """return list of phases"""
        return self.__phaseList


    def get_pretty_print(self):
        ret = '%i week plan:' % len(self)
        for phase in self.get_phases():
            ret += '\n' + phase.get_pretty_print(1)
        return ret


###########################################################################

class TrainingPhase(object):
    """Abstract class. Defines a phase of a training plan.
    """

    def __init__(self, phasenum):
        """TrainingPhase constructor"""
        if phasenum < 1:
            raise PhaseNumberException('Phase number can\'t be less than 1.')
        self.phasenum = phasenum
        self.desc = ''
        self.__weeks = []

    def __len__(self):
        return len(self.__weeks)

    def get_week(self, weekindex):
        """return the training week of this phase"""
        if (weekindex > len(self.__weeks) - 1) or weekindex < 0:
            return None
        return self.__weeks[weekindex]

    def get_num_weeks(self):
        """Return the number of weeks in this phase"""
        return len(self)

    def add_week(self, week):
        """add a week to this phase"""
        self.__weeks.append(week)

    def extend_weeks(self, weeks):
        """Extend the weeks list with the weeks listed in weeks"""
        self.__weeks.extend(weeks)

    def get_weeks(self):
        """return the list of weeks"""
        return self.__weeks

    def get_pretty_print(self, tabs):
        ret = 'Phase %i:' % self.phasenum
        for week in self.get_weeks():
            ret += '\n%s' % week.get_pretty_print(tabs + 1)
        return ret


###########################################################################

class TrainingWeek(object):
    """Defines a week of training. Includes a collection of days."""

    def __init__(self):
        """TrainingWeek constructor"""
        self.__days = []
        self.weeknum = 0


    def get_pretty_print(self, tabs):
        ret = '\t' * tabs
        ret += 'Week %i:' % self.weeknum
        for day in self.get_days():
            ret += '\n%s' % day.get_pretty_print(tabs + 1)
        return ret


###########################################################################

class TrainingDay(object):
    """Defines a single day of training. Can contain multiple workouts"""

    def __init__(self, day_of_week=1):
        """
        Initialize Training Day with day of week number: [1,7]
        :type day_of_week: int
        :param day_of_week:
        """
        self.__day_of_week = 0
        self.set_day_of_week(day_of_week)
        self.__workouts = []

    def __repr__(self):
        return 'Day %i: (%r)' % (self.__day_of_week, tuple(self.get_workouts()))

    def __str__(self):
        ret = 'Day %i workouts:' % self.__day_of_week
        for workout in self.get_workouts():
            ret += '\n\t%r' % workout
        return ret

    def add_workout(self, workout):
        """Adds a workout to the list"""
        self.__workouts.append(workout)

    def get_workouts(self):
        """return the list of workouts"""
        return self.__workouts

    def get_pretty_print(self, tabs):
        """return string for printing human readable day"""
        ret = '\t' * tabs
        ret += 'Day %i workouts:' % self.__day_of_week
        for workout in self.get_workouts():
            ret += '\n%s' % workout.get_pretty_print(tabs + 1)
        return ret

    def get_day_of_week(self):
        """
        :rtype : int
        """
        return self.__day_of_week

    def set_day_of_week(self, day_of_week):
        """
        :type day_of_week: int
        :param day_of_week:
        """
        if 0 < day_of_week < 8:
            self.__day_of_week = day_of_week
        else:
            raise DayOfWeekException('Invalid day specified. Must be an integer 1 through 7')


class TrainingGeneratorException(Exception):
    """Base exception class for Training Generator errors."""
    def __init__(self, message):
        self.message = message
        pass


class DayOfWeekException(TrainingGeneratorException):
    """Exception thrown when there is an issue with a day of the week"""


class PhaseNumberException(TrainingGeneratorException):
    """Exception thrown when there is an issue with the phase number"""

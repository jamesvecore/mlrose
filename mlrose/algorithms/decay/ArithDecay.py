""" Classes for defining decay schedules for simulated annealing."""

# Author: Genevieve Hayes
# License: BSD 3 clause


class ArithDecay:
    """
    Schedule for arithmetically decaying the simulated
    annealing temperature parameter T according to the formula:

    .. math::

        T(t) = \\max(T_{0} - rt, T_{min})

    where:

    * :math:`T_{0}` is the initial temperature (at time t = 0);
    * :math:`r` is the rate of arithmetic decay; and
    * :math:`T_{min}` is the minimum temperature value.

    Parameters
    ----------
    init_temp: float, default: 1.0
        Initial value of temperature parameter T. Must be greater than 0.
    decay: float, default: 0.0001
        Temperature decay parameter, r. Must be greater than 0.
    min_temp: float, default: 0.001
        Minimum value of temperature parameter. Must be greater than 0.

    Example
    -------
    .. highlight:: python
    .. code-block:: python

        >>> import mlrose
        >>> schedule = mlrose.ArithDecay(init_temp=10, decay=0.95, min_temp=1)
        >>> schedule.evaluate(5)
        5.25
    """

    def __init__(self, init_temp=1.0, decay=0.0001, min_temp=0.001):

        self.init_temp = init_temp
        self.decay = decay
        self.min_temp = min_temp

        if self.init_temp <= 0:
            raise Exception("""init_temp must be greater than 0.""")

        if (self.decay <= 0) or (self.decay > 1):
            raise Exception("""decay must be greater than 0.""")

        if self.min_temp < 0:
            raise Exception("""min_temp must be greater than 0.""")
        elif self.min_temp > self.init_temp:
            raise Exception("""init_temp must be greater than min_temp.""")

    def evaluate(self, t):
        """Evaluate the temperature parameter at time t.

        Parameters
        ----------
        t: int
            Time at which the temperature paramter T is evaluated.

        Returns
        -------
        temp: float
            Temperature parameter at time t.
        """

        temp = self.init_temp - (self.decay*t)

        if temp < self.min_temp:
            temp = self.min_temp

        return temp

    def __str__(self):
        return str(self.init_temp)

    def __repr__(self):
        return f'{self.__class__.__name__}(init_temp={self.init_temp}, ' \
               f'decay={self.decay}, min_temp={self.min_temp})'

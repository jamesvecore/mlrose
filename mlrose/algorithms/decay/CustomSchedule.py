""" Classes for defining decay schedules for simulated annealing."""

# Author: Genevieve Hayes
# License: BSD 3 clause


class CustomSchedule:
    """Class for generating your own temperature schedule.

    Parameters
    ----------
    schedule: callable
        Function for calculating the temperature at time t with the signature
        :code:`schedule(t, **kwargs)`.

    kwargs: additional arguments
        Additional parameters to be passed to schedule.

    Example
    -------
    .. highlight:: python
    .. code-block:: python

        >>> import mlrose
        >>> def custom(t, c): return t + c
        >>> kwargs = {'c': 10}
        >>> schedule = mlrose.CustomSchedule(custom, **kwargs)
        >>> schedule.evaluate(5)
        15
    """

    def __init__(self, schedule, **kwargs):

        self.schedule = schedule
        self.kwargs = kwargs

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

        temp = self.schedule(t, **self.kwargs)
        return temp

    def __str__(self):
        return str(self.schedule)

    def __repr__(self):
        return f'{self.__class__.__name__}[{self.__dict__}]'

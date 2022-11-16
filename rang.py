"""Model of a ball movement."""


class InvalidFigureError(Exception):
    """Exception raised for invalid radius of a ball."""

    def __init__(self, message: str) -> None:
        """Error initialization.

        Parameters:
            message : str - output message of the error
        """
        self.message = message

    def __str__(self) -> str:
        """Return formated error message."""
        return 'InvalidFigureError: {0}'.format(self.message)


class Ball:
    """Representation of a ball.

    Attributes:
        radius: float - radius of a ball
    """

    def __init__(self, radius: float) -> None:
        """Initialization of ball.

        Parameters:
            radius : float - radius of a ball

        Raises:
            InvalidFigureError : if radius can not exist.
        """
        self.radius = radius
        if not self.is_valid():
            raise InvalidFigureError('Circle can not be built with this radius.')

    def angle_from_even(self, speed: float, time: float) -> float:
        """Evaluate the angle of ball`s even movement.
        
        Args:
            speed : float - speed of the ball
            time : float - time of the ball`s movement

        Returns:
            float - angle of the ball`s movement in degrees
        """
        len_bow = speed * time
        return round(len_bow / self.radius, 2)

    def angle_from_acceleration(self, acceleration: float, time: float) -> float:
        """Evaluate the angle of ball`s accelerated movement.
        
        Args:
            acceleration : float - acceleration of the ball
            time : float - time of the ball`s movement

        Return:
            float - angle of the ball`s movement in degrees
        """
        speed = acceleration * time
        return self.angle_from_acceleration(speed, time)


    def is_valid(self):
        """Check condition of circle`s existence."""
        if not isinstance(self.radius, (int, float)):
            return False
        if self.radius <= 0:
            return False
        return True

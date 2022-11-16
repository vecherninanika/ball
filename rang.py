"""Model of a ball movement."""
FLAT_ANGLE = 180


class InvalidAttributeError(Exception):
    """Exception raised for invalid radius of a ball."""

    def __init__(self, message: str) -> None:
        """Error initialization.

        Parameters:
            message : str - output message of the error
        """
        self.message = message

    def __str__(self) -> str:
        """Return formated error message."""
        return 'InvalidAttributeError: {0}'.format(self.message)


class Ball:
    """Representation of a ball.

    Attributes:
        radius: float - radius of a ball in centimetres
    """

    def __init__(self, radius: float) -> None:
        """Initialization of ball.

        Parameters:
            radius : float - radius of a ball in centimetres

        Raises:
            InvalidAttributeError : if radius cannot exist.
        """
        self.radius = radius
        if not self.is_valid():
            raise InvalidAttributeError('Ball cannot be built with this radius.')

    def angle_from_even(self, speed: float, time: float) -> float:
        """Evaluate the angle of ball`s even movement. Round the result to 2 decimal places.

        Args:
            speed : float - speed of the ball in centimetres per second
            time : float - time of the ball`s movement in seconds

        Returns:
            float - angle of the ball`s movement in degrees

        Raises:
            InvalidAttributeError : if speed or time are less than zero.
        """
        if not isinstance(speed, (int, float)) or not isinstance(time, (int, float)):
            raise InvalidAttributeError('Attributes can be only int or float.')
        elif time < 0 or speed < 0:
            raise InvalidAttributeError('Attributes cannot be less than zero.')
        len_bow = speed * time
        angle = round(len_bow / self.radius, 2)
        if angle >= FLAT_ANGLE:
            return FLAT_ANGLE - angle % FLAT_ANGLE
        return angle

    def angle_from_acceleration(self, acceleration: float, time: float) -> float:
        """Evaluate the angle of ball`s accelerated movement.

        Args:
            acceleration : float - acceleration of the ball in centimetres per square second
            time : float - time of the ball`s movement in seconds

        Return:
            float - angle of the ball`s movement in degrees

        Raises:
            InvalidAttributeError : if speed or time are less than zero.
        """
        if not isinstance(acceleration, (int, float)) or not isinstance(time, (int, float)):
            raise InvalidAttributeError('Attributes can be only int or float.')
        elif time < 0 or acceleration < 0:
            raise InvalidAttributeError('Attributes cannot be less than zero.')
        speed = acceleration * time
        return self.angle_from_even(speed, time)

    def is_valid(self):
        """Check condition of circle`s existence."""
        if not isinstance(self.radius, (int, float)):
            return False
        elif self.radius <= 0:
            return False
        return True

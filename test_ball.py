import pytest
from rang import Ball, InvalidAttributeError

tests_ball_init = [(4.0), (67.0), (16.0)]


@pytest.mark.parametrize('radius', tests_ball_init)
def test_init_ball(radius: float) -> None:
    """Test ball's initialization."""
    ball = Ball(radius)
    assert ball.radius == radius


tests_even = [(6.0, 8.0, 10.0, 13.33), (6.0, 33.0, 303.0, 133.5)]


@pytest.mark.parametrize('radius, speed, time, answer', tests_even)
def test_even_angle(radius: float, speed: float, time: float, answer: float) -> None:
    """Test ball`s angle_from_even method."""
    assert Ball(radius).angle_from_even(speed, time) == answer


tests_acceleration = [(3.0, 4.0, 6.0, 48.0), (4.0, 48.0, 606.0, 108.0)]


@pytest.mark.parametrize('radius, acceleration, time, answer', tests_acceleration)
def test_accelerated_angle(radius: float, acceleration: float, time: float, answer: float) -> None:
    """Test ball`s angle_from_acceleration method."""
    assert Ball(radius).angle_from_acceleration(acceleration, time) == answer


def test_str_radius():
    """Test for invalid radius."""
    with pytest.raises(InvalidAttributeError):
        Ball('radius')


def test_negative_radius():
    """Test for invalid radius."""
    with pytest.raises(InvalidAttributeError):
        Ball(-6)


def test_negative_args_even():
    """Test for invalid speed and time."""
    with pytest.raises(InvalidAttributeError):
        Ball(6).angle_from_even(-4, -5)


def test_str_args_even():
    """Test for invalid speed and time."""
    with pytest.raises(InvalidAttributeError):
        Ball(6).angle_from_even('speed', 'time')


def test_negative_args_acceler():
    """Test for invalid acceleration and time."""
    with pytest.raises(InvalidAttributeError):
        Ball(6).angle_from_acceleration(-8, -2)


def test_str_args_acceler():
    """Test for invalid acceleration and time."""
    with pytest.raises(InvalidAttributeError):
        Ball(6).angle_from_acceleration('acceleration', 'time')

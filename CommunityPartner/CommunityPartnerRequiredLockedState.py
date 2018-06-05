from enum import Enum


class RequiredLockState(Enum):
    """
    Required or Locked states defined and used throughout the Community Partner Field implementations.

    Note: The "R" indicates Required fields. "L" indicates Locked fields that should not be changed by the
    ACO, MCO or CP if they have been pre-populated by MassHealth. "O" indicates optional fields that
    MassHealth intends to supply when/if possible, or that the ACO or MCO may supply.
    """
    REQUIRED = 'R'
    LOCKED = 'L'
    OPTIONAL = 'O'

# -*- coding: utf-8 -*-
"""Dataclasses used with the EpicMix Class"""

from dataclasses import dataclass


@dataclass
class LifetimeStats:
    """
    Represents a user's lifetime stats.

    Attributes:
        displayName (str): The name of the person.
        summaryStatId (int): The age of the person.
        liftRides (int): Total number of lifetime lift rides.
        daysOnMountain (int): Total number of lifetime days on mountain.
        verticalInFeet (int): Total lifetime verical feet.
        verticalInMeters (float): Total lifetime verical meters.
        mostVisitedResort (int): Lifetime most visited resport number.
        updatedTimestampUtc (str): Timestamp of when the information was updated.
    """

    displayName: str
    summaryStatId: int
    liftRides: int
    daysOnMountain: int
    verticalInFeet: int
    verticalInMeters: float
    mostVisitedResort: int
    updatedTimestampUtc: str

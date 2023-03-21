# -*- coding: utf-8 -*-
"""Dataclasses used with the EpicMix Class"""

from dataclasses import dataclass


@dataclass
class LifetimeStats:
    """
    Represents a rider's lifetime stats.

    Attributes:
        displayName (str): The display name of the statistic ("Lifetime Stats").
        summaryStatId (int): The unique identifier for the rider's lifetime stats.
        liftRides (int): The number of lifetime lift rides.
        daysOnMountain (int): The number of lifetime days on mountain.
        verticalInFeet (int): The total lifetime vertical distance skied in feet.
        verticalInMeters (float): The total lifetime vertical distance skied in meters.
        mostVisitedResort (int): The identifier for the rider's lifetime most visited resort.
        updatedTimestampUtc (str): The UTC timestamp when the statistics were last updated.
    """

    displayName: str
    summaryStatId: int
    liftRides: int
    daysOnMountain: int
    verticalInFeet: int
    verticalInMeters: float
    mostVisitedResort: int
    updatedTimestampUtc: str


@dataclass
class SeasonStats:
    """
    Represents a rider's stats for a specific season.

    Attributes:
        summaryStatId (int): The unique identifier for the rider's seasonal stats.
        seasonDisplayName (str): The display name of the season.
        seasonTagId (int): The unique identifier for the season.
        liftRides (int): The number of lift rides taken during the season.
        daysOnMountain (int): The number of days on mountain during the season.
        verticalInFeet (int): The total vertical distance skied in feet during the season.
        verticalInMeters (float): The total vertical distance skied in meters during the season.
        mostVisitedResort (int): The identifier for the most visited of the season.
        updatedTimestampUtc (str): The UTC timestamp when the statistics were last updated.
    """

    summaryStatId: int
    seasonDisplayName: str
    seasonTagId: int
    liftRides: int
    daysOnMountain: int
    verticalInFeet: int
    verticalInMeters: float
    mostVisitedResort: int
    updatedTimestampUtc: str


@dataclass
class DayStats:
    """Represents a rider's stats for a single day at a resort.

    Attributes:
        resortDayStatId (int): The unique identifier for the statistics for the rider's day.
        resortId (str): The identifier for the resort where the statistics were recorded.
        verticalInFeet (int): The total vertical distance skied in feet on the day.
        verticalInMeters (float): The total vertical distance skied in meters on the day.
        liftRides (int): The number of lift rides taken on the day.
        createdTimestampUtc (str): The UTC timestamp when the statistics were created.
        updatedTimestampUtc (str): The UTC timestamp when the statistics were last updated.
    """

    resortDayStatId: int
    resortId: str
    verticalInFeet: int
    verticalInMeters: float
    liftRides: int
    createdTimestampUtc: str
    updatedTimestampUtc: str


@dataclass
class LiftRide:
    """Represents a single lift ride at a resort.

    Attributes:
        resortName (str): The name of the ski resort where the ride took place.
        liftName (str): The name of the lift that was ridden.
        scanTime (str): The time at which the rider's lift ticket was scanned.
    """

    resortName: str
    liftName: str
    scanTime: str

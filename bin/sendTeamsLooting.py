#!/usr/bin/env python3
"""Crabada script to send looting all available teams for
the given user address.

Usage:
    python3 -m bin.sendTeamsLooting

Author:
    @coccoinomane (Twitter)
"""

from src.bot.sendTeams import sendAvailableTeamsLooting
from src.helpers.General import secondOrNone
from src.helpers.Users import isRegistered
from src.common.logger import logger
from sys import argv, exit

userAddress = secondOrNone(argv)

if not userAddress:
    logger.error('Specify a user address')
    exit(1)

if not isRegistered(userAddress):
    logger.error('The given user address is not registered')
    exit(1)    

nSent = sendAvailableTeamsLooting(userAddress)
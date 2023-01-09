#!/usr/bin/env python3
'''
Contains a function wait_random
'''
import asyncio
import random


async def wait_random(max_delay: int = 10) -> float:
    """ wait random number
    Args:
        max_delay(int, optional): max number Def to 10.
    Returns:
         float: random float number
    """
    wait_time = random.random() * max_delay
    await asyncio.sleep(wait_time)
    return

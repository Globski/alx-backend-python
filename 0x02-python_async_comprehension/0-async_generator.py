#!/usr/bin/env python3
"""
Module for asynchronous number generation.
"""

import asyncio
import random


async def async_generator():
    """Asynchronous generator that yields 10
    random numbers between 0 and 10."""
    for _ in range(10):
        await asyncio.sleep(1)
        yield random.uniform(0, 10)

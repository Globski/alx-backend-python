#!/usr/bin/env python3
"""
Module for asynchronous operations, including
a function to call wait_random multiple times.
"""

import asyncio
from typing import List

wait_random = __import__('0-basic_async_syntax').wait_random


async def wait_n(n: int, max_delay: int) -> List[float]:
    """Calls wait_random n times and returns the
    list of delays in ascending order."""
    tasks = [wait_random(max_delay) for _ in range(n)]
    delays = await asyncio.gather(*tasks)
    return sorted(delays)

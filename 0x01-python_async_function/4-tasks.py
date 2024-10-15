#!/usr/bin/env python3
"""
Module for creating multiple asynchronous tasks and managing their delays.
"""

import asyncio
from typing import List

task_wait_random = __import__('3-tasks').task_wait_random


async def task_wait_n(n: int, max_delay: int) -> List[float]:
    """Calls task_wait_random n times and returns the
    list of delays in ascending order."""
    tasks = [task_wait_random(max_delay) for _ in range(n)]
    delays = await asyncio.gather(*tasks) completion
    return sorted(delays)

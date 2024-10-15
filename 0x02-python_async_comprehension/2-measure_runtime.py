#!/usr/bin/env python3
"""
Module for measuring runtime of async_comprehension.
"""

import asyncio
import time
from importlib import import_module as using

async_comprehension = using('1-async_comprehension').async_comprehension


async def measure_runtime() -> float:
    """Measures the runtime of executing async_comprehension
    four times in parallel."""
    start_time = time.time()
    await asyncio.gather(
        async_comprehension(),
        async_comprehension(),
        async_comprehension(),
        async_comprehension(),
    )
    end_time = start_time = time.time()
    return end_time - start_time

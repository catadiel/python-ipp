# pylint: disable=W0621
"""Asynchronous Python client for IPP."""
import asyncio

from pyipp import IPP


async def main() -> None:
    """Show example of connecting to your IPP print server."""
    async with IPP("ipp://10.1.48.48/ipp/print") as ipp:

    #async with IPP("ipp://127.0.0.1:631/printers/manualetti-packaging2") as ipp:
        # Get Printer Info
        printer = await ipp.printer()
        print(printer)



if __name__ == "__main__":
    loop = asyncio.new_event_loop()
    loop.run_until_complete(main())

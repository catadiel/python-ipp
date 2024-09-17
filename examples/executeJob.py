# pylint: disable=W0621
"""Asynchronous Python client for IPP."""
import asyncio

from pyipp import IPP
from pyipp.enums import IppOperation


async def main() -> None:
    """Show example of executing operation against your IPP print server."""
   #async with IPP("ipp://127.0.0.1:631/ipp/print") as ipp: #cups
    async with IPP("ipp://10.1.48.48/ipp/print") as ipp: #bay3
   # async with IPP("ipp://127.0.0.1:631/printers/Corvina") as ipp: #corvinaoffice
        response = await ipp.execute(
            IppOperation.GET_JOB_ATTRIBUTES,
            {
                "version": (2, 0),  # try (1, 1) for older devices
                "job-attributes-tag": {
                    "requested-attributes": [
                        # "printer-device-id",
                        # "printer-name",
                        # "printer-type",
                        # "printer-location",
                        # "printer-info",
                        # "printer-make-and-model",
                        # "printer-state",
                        # "printer-state-message",
                        # "printer-state-reason",
                        # "printer-supply",
                        # "printer-up-time",
                         "printer-uri-supported",
                        # "device-uri",
                        # "printer-is-shared",
                        # "printer-more-info",
                        # "printer-firmware-string-version",
                        # "marker-colors",
                        # "marker-high-levels",
                        # "marker-levels",
                        # "marker-low-levels",
                        # "marker-names",
                        # "marker-types",
                        # "color-supported",
                        # "sides-supported",
                        # "print-scaling-supported",
                        # "print-color-mode-supported",
                        # "media-col-supported",
                        # "media-size-supported",
                        # "media-format-supported",
                        "media-supported",
                        "operations-supported",
                    ],
                },
            },
        )

        print(response)


if __name__ == "__main__":
    loop = asyncio.new_event_loop()
    loop.run_until_complete(main())

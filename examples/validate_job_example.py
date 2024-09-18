# pylint: disable=W0621
"""Asynchronous Python client for IPP."""
import asyncio
import logging
from pathlib import Path
import aiofiles




from pyipp import IPP
from pyipp.enums import IppOperation, IppTag, IppOrientationRequested, IppPrintQuality
from aiosmb.commons.connection.factory import SMBConnectionFactory

logging.basicConfig(
    format="%(asctime)s [%(levelname)-5s] [%(name)s.%(funcName)s] %(message)s",
    level=logging.DEBUG,
)
logging.getLogger('root').setLevel(logging.DEBUG)



async def GetPDF(filename) -> bytes:
    url = "smb+ntlm-password://EXORINT\\carlo.tadiello:ct.apr-2024@192.168.20.144/Produzione/Sitek/UT/MANUALI/" + filename
    smburl = SMBConnectionFactory.from_url(url)
    connection = smburl.get_connection()
    smbfile = smburl.get_file()

    async with connection:
        _, err = await connection.login()
        if err is not None:
            raise err

        _, err = await smbfile.open(connection)
        if err is not None:
            raise err

        data, err = await smbfile.read()
        if err is not None:
            raise err
        return data


async def main() -> None:
    """Show example of executing operation against your IPP print server."""
    # data_folder = Path("C:/Users/carlo.tadiello/OneDrive - EXOR INTERNATIONAL SPA/Documents/")
    #
    #
    # pdf_file = data_folder / "A5_digitalization+maps.pdf"

    # pdf_file = "/Users/carlo/Downloads/42409022525.pdf"
    # async with aiofiles.open(pdf_file, mode="rb") as file:
    #     content = await file.read()

    # content = await GetPDF("MANESMARTxxBY001_IT.pdf")
    async with IPP("ipp://192.168.26.254/ipp/print") as ipp:  # brother
    # async with IPP("ipp://10.1.89.10:631/ipp/print") as ipp: #corvina
    # async with IPP("ipp://127.0.0.1:631/printers/Corvina") as ipp: #corvinaCUPS
    # async with IPP("ipp://10.1.48.48/ipp/print") as ipp: #bay3
    # async with IPP("ipp://127.0.0.1:631/printers/manualetti-packaging2") as ipp: #bay3CUPS

        response = await ipp.execute(
            IppOperation.VALIDATE_JOB,
                {
                "operation-attributes-tag": {
                     "requesting-user-name": "CupsCarlo",
                    # "job-name": "Manualetto2",
                    #"document-format": "application/pdf",
                    },
                "job-attributes-tag": {
                    # "job-k-octets": 4324,
                    #  "sides": "two-sided-long-edge",
                    # # "print-color-mode": "monochrome",
                    # "print-scaling": "fit",
                    # "page-range": (1, 4),
                    # "orientation-requested": IppOrientationRequested.PORTRAIT,
                    # 'print-quality': IppPrintQuality.NORMAL,
                    # "copies": 1,
                    # 'printer-resolution': (300, 300, 3),
                    # # "media-type": "stationery",
                    # "output-bin": "face-down",
                    # "multiple-document-handling": "separate-documents-collated-copies",
                    "media-col": {
                        # "media-color": "blue",
                        "media-size": {
                            "x-dimension" : 6,
                            "y-dimension" : 4,
                        },
                        "media-type": "stationary",
                    },
                # "data": content,
                },
                },
            )

        print(response)


if __name__ == "__main__":
    loop = asyncio.new_event_loop()
    loop.run_until_complete(main())

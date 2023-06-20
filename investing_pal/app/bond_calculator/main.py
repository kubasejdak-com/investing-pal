#!/usr/bin/env python3

import argparse
import datetime
import logging

import rich.traceback
from rich.highlighter import NullHighlighter
from rich.logging import RichHandler

from investing_pal.finances.currency import PLN
from investing_pal.finances.interest import FixedInterest
from investing_pal.securities.bond import Bond

log = logging.getLogger(__name__)


def add_common_args(args_parser: argparse.ArgumentParser) -> None:
    args_parser.add_argument(
        "-l",
        "--log",
        type=str,
        choices=["critical", "error", "warning", "info", "debug"],
        default="info",
        dest="log_level",
        help="Use given log level",
    )


def run() -> None:
    rich.traceback.install(show_locals=True)

    parser = argparse.ArgumentParser(prog="bond-calculator", formatter_class=argparse.ArgumentDefaultsHelpFormatter)

    add_common_args(parser)

    parsed_args = parser.parse_args()

    logging.basicConfig(
        level=logging.getLevelName(parsed_args.log_level.upper()),
        format="[%(name)s] %(message)s",
        datefmt="%Y.%m.%d %H:%M:%S",
        handlers=[RichHandler(highlighter=NullHighlighter())],
    )

    log.info(f"Starting bond-calculator v0.0.1")

    bond = Bond(currency=PLN, face_value=100, price=15.0, coupon_rate=FixedInterest(1.0), maturity_date=datetime.date.today())
    print(bond)

if __name__ == "__main__":
    run()

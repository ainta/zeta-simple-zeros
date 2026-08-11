"""Command-line interface."""

from __future__ import annotations

import argparse
from typing import Sequence

from .constants import H0, seven_point_bound, three_point_bound
from .report import VerificationReport
from .verify_seven import verify_seven
from .verify_three import (
    TARGET_DENOMINATOR as THREE_DENOMINATOR,
    TARGET_NUMERATOR as THREE_NUMERATOR,
    verify_three,
)


def _print_report(report: VerificationReport, as_json: bool) -> None:
    print(report.to_json() if as_json else report.to_text())


def build_parser() -> argparse.ArgumentParser:
    parser = argparse.ArgumentParser(
        prog="zeta-zero-verify",
        description="Verify the 3-point and 7-point inequalities for the simple-zero bounds.",
    )
    parser.add_argument("certificate", choices=("three", "seven", "all"))
    parser.add_argument("--json", action="store_true", help="print JSON reports")
    parser.add_argument(
        "--progress-every",
        type=int,
        default=0,
        metavar="N",
        help="print a progress line every N visited nodes",
    )
    return parser


def main(argv: Sequence[str] | None = None) -> int:
    args = build_parser().parse_args(argv)
    reports = []
    if args.certificate in ("three", "all"):
        reports.append(verify_three(args.progress_every))
    if args.certificate in ("seven", "all"):
        reports.append(verify_seven(args.progress_every))

    for index, report in enumerate(reports):
        if index:
            print()
        _print_report(report, args.json)

    if not args.json:
        epsilon = THREE_NUMERATOR / THREE_DENOMINATOR
        print()
        print(f"H0={H0:.16f}")
        print(f"three_point_bound={three_point_bound(epsilon):.16f}")
        print(f"seven_point_bound={seven_point_bound():.16f}")
    return 0

import argparse
import datetime
import re


def is_naf_correct(naf):
    """Validate that NAF has NAF format"""
    pattern = r"\d{2}/\d{8}-\d{2}"
    if re.search(pattern, naf):
        return True
    else:
        return False


def validate_naf(value):
    if not is_naf_correct(value):
        raise argparse.ArgumentTypeError("NAF must be in NAF format. Example: 43/12345678-20")
    else:
        return value


def parse_date(value, formatting="%Y_%m"):
    """Validate date format"""
    try:
        return datetime.datetime.strptime(value, formatting)
    except Exception as e:
        raise ValueError("The value " + value + " could not be formatted with "
                         + formatting + ". Datetime exception was " + e.__str__())


def parse_arguments():
    """Parse and validate command-line arguments"""
    parser = argparse.ArgumentParser(description="Process NAF and date range.")

    parser.add_argument("-n", "--naf", type=validate_naf, required=True, help="NAF (SS security number)")
    parser.add_argument("-b", "--begin", type=parse_date, required=True, help="Begin date (YYYY-MM)")
    parser.add_argument("-e", "--end", type=parse_date, required=True, help="End date (YYYY-MM)")

    args = parser.parse_args()

    return args

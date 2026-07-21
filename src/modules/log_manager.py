"""Sets up and manages the logfile of output from app running."""

# Standard lib imports
import logging
from pathlib import Path


def log_setup(logfile_destination: Path | str) -> logging.Logger:
    """Sets up projects output log file at location provided.

    Args:
        logfile_destination (Path | str): file path logfile will be written to.

    Returns:
        (object) logging.Logger instance associated with the specified name.
    """
    # Make log file path if it doesnt exist.
    if not Path(logfile_destination).exists():
        Path(logfile_destination).mkdir(parents=True, exist_ok=True)

    # Create logfile path destination.
    logging.basicConfig(
        filename=str(logfile_destination) + "file_manager.log",
        level=logging.DEBUG,
        filemode="a",  # 'a' to append, 'w' to overwrite each run
        format="%(asctime)s - %(levelname)s - %(message)s",
    )

    # initialize logger.
    logger = logging.getLogger()

    return logger

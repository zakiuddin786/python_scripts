import logging
import csv 
from pathlib import Path

logger = logging.getLogger(__name__)

class CSVRepository:
    def __init__(self, file_path):
        self.file_path = Path(file_path)

    def _initialize(self):
        if not self.file_path.exists():
            with open(self.file_path, mode="w", newline="",encoding="utf-8") as f:
                writer = csv.writer(f)
                writer.writerow(["Quote", "Author", "Tags"])

    def save(self, records: list[dict]):
        logger.info(f"Starting to save  {len(records)} quotes in CSV")
        with open(self.file_path, mode="a", newline="", encoding="utf-8") as f:
            writer = csv.writer(f)
            for record in records:
                writer.writerow([record["quote"], record["author"], record["tags"]])
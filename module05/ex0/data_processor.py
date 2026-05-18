#!/usr/bin/env python3

from abc import ABC, abstractmethod
import typing


class Invalid(Exception):
    pass


class DataProcessor(ABC):
    @abstractmethod
    def validate(self, data: any) -> bool:
        pass

    @abstractmethod
    def ingest(self, data: any) -> None:
        pass


    def output(self) -> tuple[int, str]:
        pass


class NumericProcessor(DataProcessor):
    def validate(self, data: any) -> bool:
        check = False
        if isinstance(data, int) or isinstance(data, float):
            check = True
        elif isinstance(data, list):
            for x in data:
                if isinstance(x, int) or isinstance(x, float):
                    check = True
                else:
                    check = False
        return check


    def ingest(self, data: any) -> None:
        try:
            if not self.validate(data):
                raise Invalid("Improper numeric data")
            print(f"Processing data: {data}")
            
        except Invalid as e:
            print(" Got exception:", e)


class TextProcessor(DataProcessor):
    pass


class LogProcessor(DataProcessor):
    pass


def main() -> None:
    print("\nTesting Numeric Processor...")
    num_proc = NumericProcessor()
    print(f" Trying to validate input '42': {num_proc.validate(42)}")
    print(f" Trying to validate input 'Hello': {num_proc.validate("Hello")}")
    print(" Test invalid ingestion of string 'foo' without prior validation:")
    num_proc.ingest([1, 2, 3, 4, 5])


if __name__ == "__main__":
    print("=== Code Nexus - Data Processor ===")
    main()
#!/usr/bin/env python3

from abc import ABC, abstractmethod
import typing


class Invalid(Exception):
    pass


class DataProcessor(ABC):
    def __init__(self):
        self.stock = []


    @abstractmethod
    def validate(self, data: any) -> bool:
        pass

    @abstractmethod
    def ingest(self, data: any) -> None:
        pass


    def output(self) -> tuple[int, str]:
        if not self.stock == []:
            return self.stock.pop(0)


class NumericProcessor(DataProcessor):
    def __init__(self):
        self.stock = []

    def validate(self, data: any) -> bool:
        check = False

        if isinstance(data, int) or isinstance(data, float):
            check = True
        elif all(isinstance(x, int) 
                 or isinstance(x, float) 
                 for x in data):
            check = True
        
        return check


    def ingest(self, data: any) -> None:
        try:
            if not self.validate(data):
                raise Invalid("Improper numeric data")
            
            print(f" Processing data: {data}")

            if isinstance(data, list):
                for x in data:

                    self.stock.append(str(x))
            else:
                self.stock.append(str(data))
    
        except Invalid as e:
            print(" Got exception:", e)


class TextProcessor(DataProcessor):

    def validate(self, data: any) -> bool:
        check = False

        if isinstance(data, str):
            check = True
        elif isinstance(data, list) and all(isinstance(x, str) for x in data):
            check = True

        return check
    
    def ingest(self, data: any) -> None:
        try:
            if not self.validate(data):
                raise Invalid("Improper string data")
            
            print(f" Processing data: {data}")

            if isinstance(data, list):
                for x in data:
                    self.stock.append(x)
            else:
                self.stock.append(data)

        except Invalid as e:
            print("Got exception: ", e)


class LogProcessor(DataProcessor):
    pass


def main() -> None:
    print("\nTesting Numeric Processor...")
    num_proc = NumericProcessor()
    print(f" Trying to validate input '42': {num_proc.validate(42)}")
    print(f" Trying to validate input 'Hello': {num_proc.validate("Hello")}")
    print(" Test invalid ingestion of string 'foo' without prior validation:")
    num_proc.ingest([1, 2, 3, 4, 5])
    print(" Extracting 3 values...")
    for i in range(3):
        print(f" Numeric value {i}: {num_proc.output()}")

    print("\nTesting Text Processor...")
    proc = TextProcessor()
    print(f" Trying to validate input '42': {proc.validate(42)}")
    proc.ingest(["hello", "Nexus", "World"])
    print(" Extracting 1 value...")
    for i in range(1):
        print(f" Numeric value {i}: {proc.output()}")

if __name__ == "__main__":
    print("=== Code Nexus - Data Processor ===")
    main()
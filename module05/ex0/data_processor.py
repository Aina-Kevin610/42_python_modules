#!/usr/bin/env python3

from abc import ABC, abstractmethod
from typing import Any

class Invalid(Exception):
    pass


class DataProcessor(ABC):
    def __init__(self):
        self.stock = []

    @abstractmethod
    def validate(self, data: Any) -> bool:
        pass

    @abstractmethod
    def ingest(self, data: Any) -> None:
        pass


    def output(self) -> tuple[int, str]:
        if not self.stock == []:
            return self.stock.pop(0)


class NumericProcessor(DataProcessor):

    def validate(self, data: Any) -> bool:
        check = False

        if isinstance(data, int) or isinstance(data, float):
            check = True
        elif all(isinstance(x, int) 
                 or isinstance(x, float) 
                 for x in data):
            check = True
        
        return check


    def ingest(self, data: int | float | list[int | float]) -> None:
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

    def validate(self, data: Any) -> bool:
        check = False

        if isinstance(data, str):
            check = True
        elif isinstance(data, list) and all(isinstance(x, str) for x in data):
            check = True

        return check
    
    def ingest(self, data: str | list[str]) -> None:
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
    def validate(self, data):
        check = False

        if isinstance(data, dict) and len(data) == 2:
            if set(data.keys()) == {"log_level", "log_message"}:
                check = True
        elif all(isinstance(x, dict) and len(x) == 2 for x in data):
            for x in data:
                if all(isinstance(key, str) 
                       and key in ["log_level", "log_message"] 
                       for key in x.keys()):
                    check = True
                else:
                    return False

        return check

    def ingest(self, data: dict | list[dict]) -> None:
        try:
            if not self.validate(data):
                raise Invalid("Improper {key:value} data")
            
            print(" processing data ", data)

            if isinstance(data, dict):
                self.stock.append([data["log_level"] + ": " + data["log_message"]])
            else:
                for x in data:
                    result = x["log_level"] + ": " + x["log_message"]
                    self.stock.append(result)

        except Invalid as e:
            print(" Got exception: ", e)


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
    str_proc = TextProcessor()
    print(f" Trying to validate input '42': {str_proc.validate(42)}")
    str_proc.ingest(["hello", "Nexus", "World"])
    print(" Extracting 1 value...")
    for i in range(1):
        print(f" Text value {i}: {str_proc.output()}")


    print("\nTesting Log Processor...")
    log_proc = LogProcessor()
    print(f" Trying to validate input 'Hello': {log_proc.validate("hello")}")
    log_proc.ingest([{'log_level': 'NOTICE', 
                      'log_message': 'Connection to server'}, 
                     {'log_level': 'ERROR', 
                      'log_message': 'Unauthorized access!!'}])
    for i in range(2):
        print(f" Log entry {i}: {log_proc.output()}")

if __name__ == "__main__":
    print("=== Code Nexus - Data Processor ===")
    main()
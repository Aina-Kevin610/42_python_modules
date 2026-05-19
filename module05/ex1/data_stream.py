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


    def ingest(self, data: int | float | list[int | float]) -> int:
        try:
            if not self.validate(data):
                raise Invalid("Improper numeric data")
            
            print(f" Processing data: {data}")

            if isinstance(data, list):
                for x in data:

                    self.stock.append(str(x))
                    return 1
            else:
                self.stock.append(str(data))
                return 1

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
                    return 1
            else:
                self.stock.append(data)
                return 1

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
                return 1
            else:
                for x in data:
                    result = x["log_level"] + ": " + x["log_message"]
                    self.stock.append(result)
                return 1

        except Invalid as e:
            print(" Got exception: ", e)



class DataStream:

    def __init__(self) -> None:
        self.stat = self.Statistics()
        self.proc = []
       
    def register_processor(self, proc: DataProcessor) -> None:
        self.proc.append(proc)


    def process_stream(self, stream: list[Any])-> None:
        for data in stream:
            check = False
            for proc in self.proc:
                if proc.validate(data):
                    self.stat += proc.ingest(data)
                    check = True
            if not check:
                print("Error - No process compatible!")

    def print_processors_stats(self) -> None:
        print("H")


def main() -> None:
    num_proc = NumericProcessor()
    str_proc = TextProcessor()
    log_proc = LogProcessor()

    stream = DataStream()
    
    stream.register_processor(num_proc)
    stream.register_processor(str_proc)
    stream.register_processor(log_proc)
    stream.process_stream(["hello", 
                         [1, 2, 3, 4, 5], 
                         [{"log_level": "LOGIN", "log_message": "SUCCES"}, 
                          {"log_level": "LOGOUT", "log_message": "SUCCES"}]])


if __name__ == "__main__":
    print("=== Code Nexus - Data Processor ===")
    main()

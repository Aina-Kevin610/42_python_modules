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


    def ingest(self, data: Any) -> None:
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
    
    def ingest(self, data: Any) -> None:
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
            if ["log_level", "log_message"] == data.keys():
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

    def ingest(self, data: Any) -> None:
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



class DataStream:
    def __init__(self, stream: Any) -> None:
        self.stream = stream
        self.proc = []
       
    def register_processor(self, proc: DataProcessor) -> None:
        self.proc.append(proc)


def main() -> None:
    stream = DataStream(["hello", 
                         [1, 2, 3, 4, 5], 
                         [{"log_level": "LOGIN", "log_message": "SUCCES"}, 
                          {"log_level": "LOGOUT", "log_message": "SUCCES"}]])

    stream.register_processor(NumericProcessor())
    print(stream.proc)
    num_proc = stream.proc[0]
    print(num_proc.validate("hello"))

if __name__ == "__main__":
    print("=== Code Nexus - Data Processor ===")
    main()

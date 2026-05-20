#!/usr/bin/env python3

from abc import ABC, abstractmethod
from typing import Any

class Invalid(Exception):
    pass


class EmptyError(Exception):
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
            
            if isinstance(data, dict):
                self.stock.append([data["log_level"] + ": " + data["log_message"]])
            else:
                for x in data:
                    result = x["log_level"] + ": " + x["log_message"]
                    self.stock.append(result)

        except Invalid as e:
            print(" Got exception: ", e)



class DataStream:
    # class Statistics:
    #     def __init__(self):
    #         self.num = 0
    #         self.str = 0
    #         self.log = 0

    #     def show(self):
    #         print(self.num)
    #         print(self.str)
    #         print(self.log)

    def __init__(self) -> None:
        # self.stat = self.Statistics()
        self.proc = []
       
    def register_processor(self, proc: DataProcessor) -> None:
        self.proc.append(proc)


    def process_stream(self, stream: list[Any])-> None:
        try:
            if self.proc == [] or stream == []:
                raise EmptyError("No processor found, no data")
            else:
                    for data in stream:
                        check = False
                        for proc in self.proc:
                            if proc.validate(data):
                                proc.ingest(data)
                                check = True
                        if not check:
                            print("DataStream error -  Can't process element in stream: ", data)

        except EmptyError as e:
            print(e)

    def print_processors_stats(self) -> None:
        print("H")


def main() -> None:
    stream_data = ['Hello world', 
              [3.14, -1, 2.71], 
              [{'log_level': 'WARNING', 'log_message': 'Telnet access! Use ssh instead'}, 
               {'log_level': 'INFO', 'log_message': 'User wil isconnected'}], 
               42, 
               ['Hi', 'five']
    ]
    stream = DataStream()

    num_proc = NumericProcessor()
    str_proc = TextProcessor()
    log_proc = LogProcessor()


    stream.process_stream([])
    print("\n")

    print("Registering Numeric Processor\n")
    stream.register_processor(num_proc)
    print("send first batch to data on stream: ", stream_data, "\n")
    stream.process_stream(stream_data)

    print("== DataStream statistics ==")
    
    stream.register_processor(str_proc)
    stream.register_processor(log_proc)
    


if __name__ == "__main__":
    print("=== Code Nexus - Data Stream ===")
    main()

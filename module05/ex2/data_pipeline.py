#!/usr/bin/env python3

from abc import ABC, abstractmethod
from typing import Any, Protocol


class Invalid(Exception):
    pass


class EmptyError(Exception):
    pass


class DataProcessor(ABC):
    def __init__(self) -> None:
        self.stock: list[tuple[int, str]] = []
        self.process_count = 0
        self.name = ""

    @abstractmethod
    def validate(self, data: Any) -> bool:
        raise NotImplementedError

    @abstractmethod
    def ingest(self, data: Any) -> None:
        raise NotImplementedError

    def output(self) -> tuple[int, str]:
        try:
            return self.stock.pop(0)
        except Exception:
            return (-1, "")


class NumericProcessor(DataProcessor):
    def __init__(self) -> None:
        super().__init__()
        self.name = "numeric_processor"

    def validate(self, data: Any) -> bool:
        check = False

        if isinstance(data, (int, float)):
            check = True
        elif isinstance(data, list) and all(
            isinstance(x, (int, float)) for x in data
        ):
            check = True

        return check

    def ingest(self, data: int | float | list[int | float]) -> None:
        try:
            if not self.validate(data):
                raise Invalid("Improper numeric data")

            if isinstance(data, list):
                for x in data:
                    self.stock.append((self.process_count, str(x)))
                    self.process_count += 1
            else:
                self.stock.append((self.process_count, str(data)))
                self.process_count += 1

        except Invalid as e:
            print("Got exception:", e)


class TextProcessor(DataProcessor):
    def __init__(self) -> None:
        super().__init__()
        self.name = "text_processor"

    def validate(self, data: Any) -> bool:
        check = False

        if isinstance(data, str):
            check = True
        elif isinstance(data, list) and all(
            isinstance(x, str) for x in data
        ):
            check = True

        return check

    def ingest(self, data: str | list[str]) -> None:
        try:
            if not self.validate(data):
                raise Invalid("Improper string data")

            if isinstance(data, list):
                for x in data:
                    self.stock.append((self.process_count, x))
                    self.process_count += 1
            else:
                self.stock.append((self.process_count, data))
                self.process_count += 1

        except Invalid as e:
            print("Got exception:", e)


class LogProcessor(DataProcessor):
    def __init__(self) -> None:
        super().__init__()
        self.name = "log_processor"

    def validate(self, data: Any) -> bool:
        check = False

        if isinstance(data, dict) and len(data) == 2:
            if set(data.keys()) == {"log_level", "log_message"}:
                check = True

        elif isinstance(data, list) and all(
            isinstance(x, dict) and len(x) == 2 for x in data
        ):
            for x in data:
                if all(
                    isinstance(key, str)
                    and key in ["log_level", "log_message"]
                    for key in x.keys()
                ):
                    check = True
                else:
                    return False

        return check

    def ingest(
        self,
        data: dict[str, str] | list[dict[str, str]],
    ) -> None:
        try:
            if not self.validate(data):
                raise Invalid("Improper {key:value} data")

            if isinstance(data, dict):
                self.stock.append(
                    (
                        self.process_count,
                        data["log_level"] + ": " +
                        data["log_message"],
                    ))
                self.process_count += 1
            else:
                for x in data:
                    result = (
                        x["log_level"] + ": " + x["log_message"]
                    )
                    self.stock.append((self.process_count, result))
                    self.process_count += 1

        except Invalid as e:
            print("Got exception:", e)


class ExportPlugin(Protocol):
    def process_output(self, data: list[tuple[int, str]],) -> None:
        raise NotImplementedError


class CSVPlugin:
    def process_output(self, data: list[tuple[int, str]],) -> None:
        print("CSV Output:")
        exported = [info[1] for info in data]
        print(",".join(exported))


class JSONPlugin:
    def process_output(self, data: list[tuple[int, str]],) -> None:
        print("JSON Output:")

        json_pairs: list[str] = []

        for rank, value in data:
            clean_value = value.replace('"', '\\"')
            pair = f'"item_{rank}": "{clean_value}"'
            json_pairs.append(pair)

        json_string = "{" + ", ".join(json_pairs) + "}"
        print(json_string)


class DataStream:
    class Statistics:
        def __init__(self) -> None:
            self.num = 0
            self.str = 0
            self.log = 0

    def __init__(self) -> None:
        self.stat = self.Statistics()
        self.proc: list[DataProcessor] = []

    def register_processor(self, proc: DataProcessor) -> None:
        self.proc.append(proc)

    def process_stream(
        self,
        stream: list[Any],
    ) -> None:
        try:
            if self.proc == [] or stream == []:
                raise EmptyError("No processor found, no data")

            for data in stream:
                check = False

                for proc in self.proc:
                    if proc.validate(data):
                        proc.ingest(data)

                        if proc.name == "numeric_processor":
                            if isinstance(data, list):
                                self.stat.num += len(data)
                            else:
                                self.stat.num += 1

                        if proc.name == "text_processor":
                            if isinstance(data, list):
                                self.stat.str += len(data)
                            else:
                                self.stat.str += 1

                        if proc.name == "log_processor":
                            if isinstance(data, list):
                                self.stat.log += len(data)
                            else:
                                self.stat.log += 1

                        check = True

                if not check:
                    print(
                        "DataStream error - Can't",
                        " process element in stream:", data
                        )

        except EmptyError as e:
            print(e)

    def output_pipeline(self,
                        nb: int,
                        plugin: ExportPlugin) -> None:

        for process in self.proc:
            processed_output: list[tuple[int, str]] = []

            for _ in range(nb):
                if len(process.stock) > 0:
                    info = process.output()
                    processed_output.append(info)
                else:
                    break

            if processed_output != []:
                plugin.process_output(processed_output)

    def print_processors_stats(self) -> None:
        print("== DataStream statistics ==")

        for x in self.proc:
            if x.name == "numeric_processor":
                print(
                    "Numeric Processor: "
                    f"total {self.stat.num} items processed, "
                    f"remaining {len(x.stock)} on processor"
                )

            elif x.name == "text_processor":
                print(
                    "Text Processor: "
                    f"total {self.stat.str} items processed, "
                    f"remaining {len(x.stock)} on processor"
                )

            elif x.name == "log_processor":
                print(
                    "Log Processor: "
                    f"total {self.stat.log} items processed, "
                    f"remaining {len(x.stock)} on processor"
                )


def main() -> None:
    print("\nInitialize Data Stream...\n")

    stream_data = [
        "Hello world",
        [3.14, -1, 2.71],
        [
            {
                "log_level": "WARNING",
                "log_message": (
                    "Telnet access! Use ssh instead"
                ),
            },
            {
                "log_level": "INFO",
                "log_message": (
                    "User wil is connected"
                ),
            },
        ],
        42,
        ["Hi", "five"],
    ]

    stream = DataStream()

    print("== DataStream statistics ==")
    stream.process_stream([])

    print("Registering Processors\n")

    num_proc = NumericProcessor()
    str_proc = TextProcessor()
    log_proc = LogProcessor()

    stream.register_processor(num_proc)
    stream.register_processor(str_proc)
    stream.register_processor(log_proc)

    print(
        "Send first batch of data on stream:",
        stream_data,
        "\n",
    )

    stream.process_stream(stream_data)
    stream.print_processors_stats()

    print(
        "\nSend 3 processed data "
        "from each processor to a CSV plugin:"
    )

    csv = CSVPlugin()
    stream.output_pipeline(3, csv)

    print("\n")

    stream.print_processors_stats()

    stream_data = [
        21,
        [
            "I love AI",
            "LLMs are wonderful",
            "Stay healthy",
        ],
        [
            {
                "log_level": "ERROR",
                "log_message": "500 server crash",
            },
            {
                "log_level": "NOTICE",
                "log_message": (
                    "Certificate expires in 10 days"
                ),
            },
        ],
        [32, 42, 64, 84, 128, 168],
        "World hello",
    ]

    print(
        "\nSend another batch of data:",
        stream_data,
        "\n",
    )

    stream.process_stream(stream_data)
    stream.print_processors_stats()

    print()

    json = JSONPlugin()

    stream.output_pipeline(5, json)

    print()

    stream.print_processors_stats()


if __name__ == "__main__":
    print("=== Code Nexus - Data Pipeline ===")
    try:
        main()
    except Exception as e:
        print("Error - ", e)

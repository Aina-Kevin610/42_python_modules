#!/usr/bin/env python3

from abc import ABC, abstractmethod
from typing import Any


class Invalid(Exception):
    pass


class DataProcessor(ABC):
    def __init__(self) -> None:
        self.stock: list[Any] = []
        self.process_count = 0

    @abstractmethod
    def validate(self, data: Any) -> bool:
        raise NotImplementedError

    @abstractmethod
    def ingest(self, data: Any) -> None:
        raise NotImplementedError

    def output(self) -> tuple[int, str]:
        return (self.process_count, self.stock.pop(0))


class NumericProcessor(DataProcessor):
    def validate(self, data: Any) -> bool:
        check = False

        if isinstance(data, (int, float)):
            check = True

        elif isinstance(data, list) and all(
            isinstance(x, (int, float))
            for x in data
        ):
            check = True

        return check

    def ingest(
        self,
        data: int | float | list[int | float],
    ) -> None:
        try:
            if not self.validate(data):
                raise Invalid(
                    "Improper numeric data"
                )

            print(f" Processing data: {data}")

            if isinstance(data, list):
                for x in data:
                    self.stock.append(
                        str(
                            (
                                self.process_count,
                                str(x),
                            )
                        )
                    )

                    self.process_count += 1

            else:
                self.stock.append(
                    str(
                        (
                            self.process_count,
                            str(data),
                        )
                    )
                )

                self.process_count += 1

        except Invalid as e:
            print(" Got exception:", e)


class TextProcessor(DataProcessor):
    def validate(self, data: Any) -> bool:
        check = False

        if isinstance(data, str):
            check = True

        elif isinstance(data, list) and all(
            isinstance(x, str)
            for x in data
        ):
            check = True

        return check

    def ingest(
        self,
        data: str | list[str],
    ) -> None:
        try:
            if not self.validate(data):
                raise Invalid(
                    "Improper string data"
                )

            print(f" Processing data: {data}")

            if isinstance(data, list):
                for x in data:
                    self.stock.append(
                        str(
                            (
                                self.process_count,
                                x,
                            )
                        )
                    )

                    self.process_count += 1

            else:
                self.stock.append(
                    str(
                        (
                            self.process_count,
                            data,
                        )
                    )
                )

                self.process_count += 1

        except Invalid as e:
            print("Got exception: ", e)


class LogProcessor(DataProcessor):
    def validate(self, data: Any) -> bool:
        check = False

        if (
            isinstance(data, dict)
            and len(data) == 2
        ):
            if set(data.keys()) == {
                "log_level",
                "log_message",
            }:
                check = True

        elif isinstance(data, list) and all(
            isinstance(x, dict)
            and len(x) == 2
            for x in data
        ):
            for x in data:
                if all(
                    isinstance(key, str)
                    and key in [
                        "log_level",
                        "log_message",
                    ]
                    for key in x.keys()
                ):
                    check = True
                else:
                    return False

        return check

    def ingest(
        self,
        data: dict[Any, Any]
        | list[dict[Any, Any]],
    ) -> None:
        try:
            if not self.validate(data):
                raise Invalid(
                    "Improper {key:value} data"
                )

            print(" processing data ", data)

            if isinstance(data, dict):
                self.stock.append(
                    str(
                        (
                            self.process_count,
                            [
                                data["log_level"]
                                + ": "
                                + data["log_message"]
                            ],
                        )
                    )
                )

                self.process_count += 1

            else:
                for x in data:
                    result = (
                        x["log_level"]
                        + ": "
                        + x["log_message"]
                    )

                    self.stock.append(
                        str(
                            (
                                self.process_count,
                                result,
                            )
                        )
                    )

                    self.process_count += 1

        except Invalid as e:
            print(" Got exception: ", e)


def main() -> None:
    print("\nTesting Numeric Processor...")

    num_proc = NumericProcessor()

    print(
        " Trying to validate input "
        f"'42': {num_proc.validate(42)}"
    )

    str_value = "Hello"

    print(
        " Trying to validate input "
        f"'Hello': "
        f"{num_proc.validate(str_value)}"
    )

    print(
        " Test invalid ingestion "
        "of string 'foo' without "
        "prior validation:"
    )

    num_proc.ingest([1, 2, 3, 4, 5])

    print(" Extracting 3 values...")

    for i in range(3):
        print(
            f" Numeric value {i}: "
            f"{num_proc.output()}"
        )

    print("\nTesting Text Processor...")

    str_proc = TextProcessor()

    print(
        " Trying to validate input "
        f"'42': {str_proc.validate(42)}"
    )

    str_proc.ingest(
        ["hello", "Nexus", "World"]
    )

    print(" Extracting 1 value...")

    for i in range(1):
        print(
            f" Text value {i}: "
            f"{str_proc.output()}"
        )

    print("\nTesting Log Processor...")

    log_proc = LogProcessor()

    print(
        " Trying to validate input "
        f"'Hello': "
        f"{log_proc.validate(str_value)}"
    )

    log_proc.ingest(
        [
            {
                "log_level": "NOTICE",
                "log_message": (
                    "Connection to server"
                ),
            },
            {
                "log_level": "ERROR",
                "log_message": (
                    "Unauthorized access!!"
                ),
            },
        ]
    )

    for i in range(2):
        print(
            f" Log entry {i}: "
            f"{log_proc.output()}"
        )


if __name__ == "__main__":
    print(
        "=== Code Nexus - "
        "Data Processor ==="
    )

    main()

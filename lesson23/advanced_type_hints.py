from typing import Optional
from typing import Union

from Lesson4.forloops import numbers
from lesson6.main2 import result


def get_name(name: Optional[str] = None) -> str:
    if name:
        return name
    return "anonymous"

print(get_name())


def process_value(value: Union[int,str]) -> str:
    if isinstance(value, int):
        return f"number: {value}"
    return f"String: {value}"

print(process_value("digital school"))


def process_anything(value: Any) -> str:
    return  f"Processed {value}"


print(process_value(1))


def sum_list(numbers: List[int]) -> int:
    return sum(numbers)

numbers: List[int] = [1,2,3]
result: int = sum_list(numbers)
print(result)
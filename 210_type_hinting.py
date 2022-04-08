import logging
from typing import Union, List, Optional, Sequence, Tuple


class TypeDemo:
    class_label: str
    logger: logging.Logger

    def __init__(self, class_label: str):
        self.logger = logging.getLogger()
        self.class_label = class_label

    @staticmethod
    def give_me_results(result_type: str) -> Union[List, Tuple, None]:
        if result_type == "list":
            return_value = [1, 2, 3, 4]
        elif result_type == "tuple":
            return_value = (1, 2, 3, 4)
        else:
            return_value = None
        return return_value

    @staticmethod
    def return_sum(values=Sequence[int]) -> Optional[int]:
        try:
            return sum(values)
        except TypeError:
            return None


if __name__ == "__main__":
    td: TypeDemo = TypeDemo("MyTypeDemo")
    summary: str = td.return_sum(values=(1, 2, "3"))  # None












    def multiply_stuff_(x: int, y: int) -> int:
        return x * y

    def multiply_stuff(x: Mapping[str, int], y: int) -> list[int]:
        try:
            x.get("ssd")
        except:
            ValueError
            .asdfasdf
        tmp = []
        for i in x:
            tmp.append(i*y)
        return tmp

    multiply_stuff([1, 2, 3, 4], 9)


    multiply_stuff(4, 9)
    multiply_stuff(4, 9)

















"""
Template Method is a behavioral design pattern that defines the skeleton of an
algorithm in the superclass but lets subclasses override specific steps of the
algorithm without changing its structure.

This pattern focus on enabling the extensibility of particular steps of an
algorithm, but not the whole algorithm or its structure.
"""

from abc import ABC, abstractmethod


class DeepLearningModel(ABC):
    """
    << Abstract Class >>
    """

    def execute(self) -> None:
        """
        << Template Method >>
        """

        self.first_required_operation()
        self.first_layer()
        self.first_hook()
        self.second_required_operation()
        self.second_layer()
        self.second_hook()
        self.third_layer()

    # << Methods that already have implementation >>

    def first_layer(self) -> None:
        """Pass through layer 1."""
        print("Passed through layer 1 ...")

    def second_layer(self) -> None:
        """Pass through layer 2"""
        print("Passed through layer 2 ...")

    def third_layer(self) -> None:
        """Pass through layer 3."""
        print("Passed through layer 3 ...")

    # << Methods that have to be implemented in subclasses >>

    @abstractmethod
    def first_required_operation(self) -> None:
        pass

    @abstractmethod
    def second_required_operation(self) -> None:
        pass

    # << 'Hooks' methods may be overrided but it's not mandatory, since they >>
    # << already have default empty implementations. They provide additional
    # << extension points in the algorithm >>

    def first_hook(self) -> None:
        pass

    def second_hook(self) -> None:
        pass


class ModelV1(DeepLearningModel):
    """
    << Concrete Class A >>
    """

    def first_required_operation(self) -> None:
        print("ModelV1 preprocessing before layer 1 ...")

    def second_required_operation(self) -> None:
        print("ModelV1 preprocessing before layer 2 ...")


class ModelV2(DeepLearningModel):
    """
    << Concrete Class B >>
    Concrete classes override only a fraction of base class operations.
    """

    def first_required_operation(self) -> None:
        print("ModelV2 preprocessing before layer 1 ...")

    def second_required_operation(self) -> None:
        print("ModelV2 preprocessing before layer 2 ...")

    def first_hook(self) -> None:
        print("Hook 1 triggered !")


def client(model: DeepLearningModel) -> None:
    """
    The client calls the template method to execute the algorithm. They does
    not have to know the concrete class of an object it works with, as long as
    it works with objects through the interface of their base class.
    """

    model.execute()


def main() -> None:
    print("The client working with the ModelV1 subclass:\n")
    client(model=ModelV1())
    print("\n" + "=" * 50 + "\n")
    print("The client working with the ModelV2 subclass:\n")
    client(model=ModelV2())


if __name__ == "__main__":
    main()

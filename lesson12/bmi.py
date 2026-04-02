from abc import ABC, abstractmethod


class Person(ABC):
    """Abstract base class for a person."""

    def __init__(self, name: str, age: int, height: float, weight: float):
        self.name = name
        self.age = age
        self.height = height
        self.weight = weight

    @abstractmethod
    def calculate_bmi(self) -> float:
        """Calculate BMI. Must be implemented by subclasses."""
        pass

    def get_bmi_category(self) -> str:
        """Return BMI category - different logic for adults vs children/teens"""
        bmi = self.calculate_bmi()

        if self.age < 18:
            return self._get_child_bmi_category(bmi)
        else:
            return self._get_adult_bmi_category(bmi)

    def _get_adult_bmi_category(self, bmi: float) -> str:
        if bmi < 18.5:
            return "Underweight"
        elif 18.5 <= bmi < 25:
            return "Normal weight"
        elif 25 <= bmi < 30:
            return "Overweight"
        else:
            return "Obese"

    def _get_child_bmi_category(self, bmi: float) -> str:
        if bmi < 5:
            return "Severely Underweight"
        elif 5 <= bmi < 85:
            return "Healthy weight"
        elif 85 <= bmi < 95:
            return "Overweight"
        else:
            return "Obese"

    def __str__(self):
        return (f"{self.name}, {self.age} years old\n"
                f"BMI: {self.calculate_bmi():.2f} - {self.get_bmi_category()}")


class Adult(Person):
    """For people 18 years and older"""

    def calculate_bmi(self) -> float:
        if self.height <= 0:
            raise ValueError("Height must be greater than 0")
        return self.weight / (self.height ** 2)


class Child(Person):
    """For people under 18 years old"""

    def calculate_bmi(self) -> float:
        if self.height <= 0:
            raise ValueError("Height must be greater than 0")
        return self.weight / (self.height ** 2)


def main():
    print("=== BMI Calculator ===\n")

    try:
        name = input("Enter your name: ").strip()
        age = int(input("Enter your age: "))
        height = float(input("Enter your height in meters (e.g. 1.75): "))
        weight = float(input("Enter your weight in kg (e.g. 70): "))

        if age >= 18:
            person = Adult(name, age, height, weight)
        else:
            person = Child(name, age, height, weight)

        print("\n" + "=" * 40)
        print(person)
        print("=" * 40)

    except ValueError as e:
        print(f"\nError: {e}. Please make sure you entered valid numbers.")
    except Exception as e:
        print(f"\nSomething went wrong: {e}")


if __name__ == "__main__":
    main()
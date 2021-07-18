''''

Model for aircraft flights.

'''


class Flight:

    """
    A flight with a particular passanger aircraft
    """

    def __init__(self, number, aircraft):  # Initializing object method
        if not number[:2].isalpha():  # Class invariantes for specific form of input!
            raise ValueError(f"No airline code in '{number}'!")

        if not number[:2].isupper():
            raise ValueError(f"No airline code in '{number}'!")

        if not (number[2:].isdigit()) and int(number[2:] <= 9999):
            raise ValueError(f"No airline code in '{number}'!")

        self._number = number
        self._aircraft = aircraft
        rows, seats = self._aircraft.seating_plan()
        self._seating = [None] + \
            [{letter: None for letter in seats} for _ in rows]

    def aircraft_model(self):  # Method to return aircraft from number
        return self._aircraft.model()

    def number(self):  # method of the class object.number()
        return self._number  # returning initialized method number

    def airline(self):
        return self._number[:2]  # Returning just Airline code

    def alocate_seat(self, seat, passanger):
        """Alocate seat to the passanger

    Args:
        seat: A seat designator like '12C' or '21F'
        passanger: A passanger name

    Raises:
        ValueError if seat is unavailable

    """
        row, letter = self._parse_seat(
            seat)  # Underscore, method is implementation detail

        if self._seating[row][letter] is not None:
            raise ValueError(f"Seat {seat} is alredy occupied")

        self._seating[row][letter] = passanger

    def _parse_seat(self, seat):
        rows, seat_letters = self._aircraft.seating_plan()

        letter = seat[-1]
        if letter not in seat_letters:
            raise ValueError(f"Invalide seat letter {letter}")

        row_text = seat[:-1]
        try:
            row = int(row_text)
        except ValueError:
            raise ValueError(f"Invalide seat row {row_text}")

        if row not in rows:
            raise ValueError(f"Invalide seat number {row}")

        return row, letter

    def relocate_passenger(self, from_seat, to_seat):
        """
        Relocate a passenger to a different seat

        Args:
            from_seat: Existing seat designator for the 
                        passanger to be moved

            to_seat: The new seat designator

        """
        from_row, from_letter = self._parse_seat(from_seat)
        if self._seating[from_row][from_letter] is None:
            raise ValueError(f"No passenger to relocate seat {from_seat}")

        to_row, to_letter = self._parse_seat(to_seat)
        if self._seating[to_row][to_letter] is not None:
            raise ValueError(f"Seat {to_seat} already occupied")

        self._seating[to_row][to_letter] = self._seating[from_row][from_letter]
        self._seating[from_row][from_letter] = None

    def num_available_seats(self):
        return sum(sum(1 for s in row.values() if s is None) for row in self._seating if row is not None)

    def make_boarding_cards(self, card_printer):
        for passenger, seat in sorted(self._passenger_seats()):
            card_printer(passenger, seat, self.number(), self.aircraft_model())

    def _passenger_seats(self):
        """
        An iterable series of passenger seating locations
        """
        row_numbers, seat_letters = self._aircraft.seating_plan()
        for row in row_numbers:
            for letter in seat_letters:
                passenger = self._seating[row][letter]
                if passenger is not None:
                    yield (passenger, f"{row}{letter}")


class Aircraft:  # Main class for subclasses

    def __init__(self, registration):
        self._registration = registration

    def registration(self):
        return self._registration

    def num_seats(self):
        rows, row_seats = self.seating_plan()
        return len(rows) * len(row_seats)


class Airbus319(Aircraft):  # Derived class
    # In production we can validate input

    def model(self):
        return "Airbus A319"

    def seating_plan(self):
        return range(1, 23), "ABCDEF"


class Boeing777(Aircraft):  # Derived class
    # In production we can validate input
    def __init__(self, registration):
        self._registration = registration

    def registration(self):
        return self._registration


def make_flight():
    f = Flight("AB3344", Aircraft("Yoko", "Ono", 22, 6))
    f.alocate_seat("14B", "Milos Basaraba")
    f.alocate_seat("11A", "Bilja Basaraba")
    f.alocate_seat("21E", "John John")

    return f


def console_card_printer(passanger, seat, flight_number, aircraft):
    output = f"Name: {passanger} "   \
             f"Flight: {flight_number} "     \
             f"Seat: {seat} "    \
             f"Aircraft: {aircraft} "    \
             " |"
    banner = "+" + "-" * (len(output) - 2) + "+"
    border = "|" + " " * (len(output) - 2) + "|"
    lines = [banner, border, output, border, banner]
    card = "\n".join(lines)
    print(card)
    print()


# Exsecution check
#f = Flight("AB3344", Aircraft("Yoko", "Ono", 22, 6))
#f.alocate_seat("14B", "Milos Basaraba")

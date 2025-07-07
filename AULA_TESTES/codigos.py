def fizz_buzz(number: int) -> str | int:
    match number % 3 == 0, number % 5 == 0:
        case [True, False]:
            return 'Fizz'
        case [False, True]:
            return 'Buzz'
        case [True, True]:
            return 'FizzBuzz'
        case _:
            return number

class HarshadNumber:
    count = 0

    def sum_of_digits(self, x):
        self.count += 1
        if x // 10 == 0:
            return x
        else:
            return (self.sum_of_digits(x // 10 + x % 10)) % 10

    def sumOfTheDigitsOfHarshadNumber(self, x: int) -> int:
        sum_digits = self.sum_of_digits(x)
        print(sum_digits)
        return sum_digits if sum_digits and not x % sum_digits else -1


obj = HarshadNumber()
print(obj.sumOfTheDigitsOfHarshadNumber(99))
print(obj.count)

#10. Write a program to Convert digit/number to words                                                                                                                                                          ABCD
def number_to_words(num):
    ones = ["", "One", "Two", "Three", "Four", "Five", "Six", "Seven", "Eight", "Nine"]
    teens = ["Ten", "Eleven", "Twelve", "Thirteen", "Fourteen", "Fifteen", "Sixteen", "Seventeen", "Eighteen", "Nineteen"]
    tens = ["", "", "Twenty", "Thirty", "Forty", "Fifty", "Sixty", "Seventy", "Eighty", "Ninety"]
    thousands = ["", "Thousand", "Million", "Billion"]

    def num_to_999(n):
        if n == 0:
            return ""
        elif n < 10:
            return ones[n]
        elif n < 20:
            return teens[n - 10]
        elif n < 100:
            return tens[n // 10] + (" " + ones[n % 10] if n % 10 != 0 else "")
        else:
            return ones[n // 100] + " Hundred" + (" " + num_to_999(n % 100) if n % 100 != 0 else "")

    if num == 0:
        return "Zero"

    result = ""
    i = 0

    while num > 0:
        if num % 1000 != 0:
            result = num_to_999(num % 1000) + " " + thousands[i] + (" " if result else "") + result
        num //= 1000
        i += 1

    return result.strip()

number = int(input("Enter a number: "))
print(number_to_words(number))

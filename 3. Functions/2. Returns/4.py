decimals = {2: "twenty", 3: "thirty", 4: "fourty", 5: "fifty", 
            6: "sixty", 7: "seventy", 8: "eighty", 9: "ninety"}
units = {1: "one", 2: "two", 3: "three", 4: "four", 5: "five",
         6: "six", 7: "seven", 8: "eight", 9: "nine"}
teens = {10: "ten", 11: "eleven", 12: "twelve", 13: "thirteen", 14: "fourteen",
         15: "fifteen", 16: "sixteen", 17: "seventeen", 18: "eighteen", 19: "nineteen"}

def numerals(num):
    if num in range(10, 20):
        return teens[num]
    elif not num // 10:
        return units[num]
    else:
        dec = decimals[num // 10]
        unit = None
        if num % 10:
            unit = units[num % 10]
        if unit:
            return dec + "-" + unit
        return dec

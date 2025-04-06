def letters_to_int(number): 

    words = {
    "zero": 0, "one": 1, "two": 2, "three": 3, "four": 4,
    "five": 5, "six": 6, "seven": 7, "eight": 8, "nine": 9,
    "ten": 10, "eleven": 11, "twelve": 12, "thirteen": 13,
    "fourteen": 14, "fifteen": 15, "sixteen": 16,
    "seventeen": 17, "eighteen": 18, "nineteen": 19,
    "twenty": 20, "thirty": 30, "forty": 40, "fifty": 50,
    "sixty": 60, "seventy": 70, "eighty": 80, "ninety": 90
    }

    number_in_int = 0

    if "hundred" in number:
        word_list = number.split("hundred")
        last = word_list[-1]
        thousands = word_list[-2]
        thousands_word_list = list(filter(None, thousands.split(" ")))
    else:
        last = number.split(" ")

    last_words = last.split(" ")
    
    for item in last_words:
        if item in words.keys():
            number_in_int += words[item]

    if thousands_word_list:
        number_in_int += 100*words[thousands_word_list[-1]]
        if "thousand" in thousands_word_list:
            multiple_of_1000 = 0
            temp_list = thousands_word_list[:thousands_word_list.index("thousand")]
            for item in temp_list:
                if item in words.keys():
                    multiple_of_1000 += words[item]          
            number_in_int += 1000*multiple_of_1000

    if len(word_list) >= 3:
        hundred_thousands = word_list[-3]
        temp_num = hundred_thousands.strip()
        number_in_int += 100000*words[temp_num]

    return number_in_int

if __name__ == "__main__":

    print("Example input ==> 'Two Thousand Three Hundred Fifty Six (2356)'")
    number_in_lett = input("Enter number in Letters: ")

    your_number = letters_to_int(number_in_lett.lower())
    print(f'{number_in_lett} converted to int is: {your_number}")


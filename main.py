from itertools import chain


class Morse:
    def __init__(self, message):

        morse_code_Capital = {
            'A': '.-', 'B': '-...', 'C': '-.-.', 'D': '-..', 'E': '.',
            'F': '..-.', 'G': '--.', 'H': '....', 'I': '..', 'J': '.---',
            'K': '-.-', 'L': '.-..', 'M': '--', 'N': '-.', 'O': '---',
            'P': '.--.', 'Q': '--.-', 'R': '.-.', 'S': '...', 'T': '-',
            'U': '..-', 'V': '...-', 'W': '.--', 'X': '-..-', 'Y': '-.--',
            'Z': '--..'}

        morse_code_dict_small = {
            'a': '.-', 'b': '-...', 'c': '-.-.', 'd': '-..', 'e': '.',
            'f': '..-.', 'g': '--.', 'h': '....', 'i': '..', 'j': '.---',
            'k': '-.-', 'l': '.-..', 'm': '--', 'n': '-.', 'o': '---',
            'p': '.--.', 'q': '--.-', 'r': '.-.', 's': '...', 't': '-',
            'u': '..-', 'v': '...-', 'w': '.--', 'x': '-..-', 'y': '-.--',
            'z': '--..'}

        morse_code_numbers = {
            '0': '-----', '1': '.----', '2': '..---', '3': '...--', '4': '....-',
            '5': '.....', '6': '-....', '7': '--...', '8': '---..', '9': '----.'}

        morse_code_spl_char = {
            '.': '.-.-.-', ',': '--..--', '?': '..--..', "'": '.----.', '!': '-.-.--',
            '/': '-..-.', '(': '-.--.', ')': '-.--.-', '&': '.-...', ':': '---...',
            ';': '-.-.-.', '=': '-...-', '+': '.-.-.', '-': '-....-', '_': '..--.-',
            '"': '.-..-.', '$': '...-..-', '@': '.--.-.'}

        global msg
        modified_msg = [list(i) for i in msg]
        transformed_msg = list(chain.from_iterable(modified_msg))

        def morse():
            morse_result = []
            for i in transformed_msg:
                if i == " ":
                    morse_result.append('/')
                elif i in morse_code_Capital:
                    morse_result.append(morse_code_Capital[i])
                elif i in morse_code_dict_small:
                    morse_result.append(morse_code_dict_small[i])
                elif i in morse_code_numbers:
                    morse_result.append(morse_code_numbers[i])
                elif i in morse_code_spl_char:
                    morse_result.append(morse_code_spl_char[i])

            morse_word = ' '.join(morse_result)
            print(morse_word)
        morse()


msg = input('Enter the message: ')
my_morse = Morse(msg)

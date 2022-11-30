def convert_roman_to_arabic(roman: str) -> str:
    """
    convert a string containing a number in roman coding to a
    string containing the number in arabic (positinal) coding
    :param roman: string to be converted
    :return: converted string
    """

    # Creo un dizionario per tener traccia degli elementi base del sistema a numeri romani
    # e dei corrispondenti valori. Cosi da poter effettuare le operazioni in modo più semplice
    roman_number = {"I": 1, "V": 5, "X": 10, "L": 50, "C": 100, "D": 500, "M": 1000}

    arabic = 0  # numero convertito inizializzato a 0

    if check_roman_number(roman):  # se il check è andato a buon fine eseguo la conversione
        i = 0  # Contatore per indice stringa in input

        while i < len(roman):
            # controllo che l'elemento in considerazione sia corrispondente a una delle chiavi
            # di roman_number:
            if roman[i] in roman_number.keys():
                roman_current_value = roman_number.get(roman[i])

                # Controllo se i corrisponde all'ultimo elemento della stringa da convertire
                # in tal caso forzo l'elemento successivo a 0 in modo da non avere un errore di
                # IndexError
                if i == len(roman) - 1:  # se sono arrivato alla fine dell'array roman
                    roman_next_value = 0
                else:
                    roman_next_value = roman_number.get(roman[i + 1])

                # Se il valore corrente è minore di quello successivo nella stringa allora devo
                # sommare la differenza tra il valore successivo e quello corrente
                # Altrimenti posso semplicemente sommare il valore corrente
                if roman_current_value < roman_next_value:
                    arabic += roman_next_value - roman_current_value
                    i += 2
                else:
                    arabic += roman_current_value
                    i += 1
    return arabic


def check_roman_number(roman: str) -> bool:
    """
    La funzione controlla tutti gli elementi presenti nella stringa da convertire.
    Se uno di questi elementi non corrisponde ad uno dei simboli che fanno parte dei
    numeri romani viene sollevata l'eccezione ValueError e si ritorna False (la verifica fallisce).
    Solo se tutti gli elementi sono validi ritorno True.
    :param roman:
    :return:
    """
    roman_bumbers = ["I", "V", "X", "L", "C", "D", "M"]
    for el in roman:
        if not(el in roman_bumbers):
            raise ValueError("Typed value is not a roman number!")
            return False
    return True


if __name__ == '__main__':
    exit_cond = 0  # condizione di terminazione del programma
    while exit_cond == 0:
        x = input("Digita un numero romano da convertire: ")
        if x != 'fine':
            print(convert_roman_to_arabic(x))
        else:
            exit_cond = 1
            print("processo terminato..")

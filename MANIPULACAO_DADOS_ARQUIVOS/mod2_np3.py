def zenit_polar_replace(text):
    #Aplicar a codificação zenit_polar, utilizando a função replace
    replacements = [('z', 'p'), ('e', 'o'), ('n', 'l'), ('i', 'a'), ('t', 'r'),
                    ('Z', 'P'), ('E', 'O'), ('N', 'L'), ('I', 'A'), ('T', 'R'),]
    for old, new in replacements:
        text = text.replace(old, new)
    return text

def main():
    # Entrada da frase e aplicação da codificação
    phrase = "The quick brown fox jumps over the lazy dog"
    phrase = phrase.title() # Primeira letra maiúscula

    #Dividir a frase em palavras
    words = phrase.split()

    # Processar cada palavra na lista usando ZENIT POLAR
    coded_words = [zenit_polar_replace(word) for word in words]

    # Juntar as palavras codificadas em uma única frase
    coded_phrase = " ".join(coded_words)
    print("Frase original:", phrase)
    print("Frase codificada:", coded_phrase)

if __name__ == "__main__":
    main()
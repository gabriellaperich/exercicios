# recebe a entrada do usuário
print('Bem-vindo! Vamos analisar quantas letras "A" existem nas palavras e frases.')
strings = input('Para começar, digite a palavra ou frase que você deseja verificar: ')

# resolve de forma simples a acentuação não reconhecida em ".count()" -- poderia usar a biblioteca Unicode
strings = strings.replace('á','a').replace('à','a').replace('ã','a').replace('Á','A').replace('À','A').replace('Ã','A')

# transforma a entraada do usuário toda em letra minúscula e depois conta as letras "A"
contagem = strings.lower().count('a')

print(f'A quantidade de letras "A" é {contagem}.')
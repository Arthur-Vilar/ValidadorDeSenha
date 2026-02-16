def cadastrarSenha():
    while True:
        senha = input("Digite uma senha: ")
        if senha == '' or ' ' in senha:
            print('Senhas vazias ou que contém espaços não são aceitas.')
            continue
        temNumero = temCaracteres = temMaiuscula = temSimbolo = False
        temCaracteres = len(senha) >= 8
        for caractere in senha:
            if caractere.isdigit():
                temNumero = True
            if caractere.isupper():
                temMaiuscula = True
            if caractere in '!@#$%&*':
                temSimbolo = True
        if temNumero and temCaracteres and temMaiuscula and temSimbolo:
            return senha
        listaProblemas = []
        if not temNumero: listaProblemas.append('um número') 
        if not temMaiuscula: listaProblemas.append('uma letra maiúscula') 
        if not temSimbolo: listaProblemas.append('um caractere especial') 
        if not temCaracteres: listaProblemas.append('oito caracteres') 
        print("\033[31mSenha inválida!\033[m") 
        for problema in listaProblemas: 
            print(f'- Sua senha precisa de ao menos {problema}!') 

senha = cadastrarSenha()
print(senha)
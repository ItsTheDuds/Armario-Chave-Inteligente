from datetime import datetime, time

docente = {
    "1": {
        "nome": "Maria",
        "idade": 25,
        "cidade": "Goiânia",
        "cracha": "123456789",
        "funcao": "Docente",
        "ativo": True,
        "bypass_horario": False
    },
    
    "2": {
        "nome": "Pedro",
        "idade": 28,
        "cidade": "Belo Horizonte",
        "cracha": "987654321",
        "funcao": "Docente",
        "ativo": False,
        "bypass_horario": False
    }
}

admin = {
    "1": {
        "nome": "João",
        "idade": 30,
        "cidade": "São Paulo",
        "cracha": "987654321",
        "funcao": "Admin",
        "ativo": True,
        "bypass_horario": True
    }
}

portaria = {
    "1": {
        "nome": "Carlos",
        "idade": 40,
        "cidade": "Rio de Janeiro",
        "cracha": "456789123",
        "funcao": "Portaria",
        "ativo": True,
        "bypass_horario": False
    }
}

data_hora = datetime.now()
horario_atual = data_hora.time()
inicio_noturno = time(23, 0, 0) 
fim_noturno = time(5, 0, 0)

def verificar_acesso(usuario):
    if not usuario["ativo"]:
        print(f"Acesso negado: Usuário {usuario['nome']} está inativo.")
        return

    if usuario["bypass_horario"]:
        print(f"Acesso permitido: {usuario['nome']} possui bypass de horário.")
        return

    if horario_atual >= inicio_noturno or horario_atual <= fim_noturno:
        print(f"Acesso negado: Fora do horário permitido para a função {usuario['funcao']}.")
    else:
        print(f"Acesso permitido: Bem-vindo(a), {usuario['nome']}.")

from datetime import datetime, time

data_hora = datetime.now()
horario_atual = data_hora.time()
docente_ativo = True

inicio_noturno = time(23, 0, 0)  # 23:00:00
fim_noturno = time(5, 0, 0) 

if (horario_atual >= inicio_noturno or horario_atual <= fim_noturno) and docente_ativo:
    docente_acesso = False
    print("Acesso negado: Fora do horário permitido para docentes.")
else:
    docente_acesso = True
    print("Acesso permitido: Dentro do horário permitido para docentes.")
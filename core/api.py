from django.db import connection
from ninja import NinjaAPI, Schema


api = NinjaAPI(
    title="API Armário Inteligente SENAI",
    version="1.0.0",
    description="Serviços RESTful para validação e controle de chaves RFID/NFC",
)


class StatusResponseSchema(Schema):
    status: str
    servidor: str
    versao: str


class ConsultaUUIDSchema(Schema):
    uuid: str
    tipo_identificado: str
    autorizado: bool
    mensagem: str
    
class ConsultaEspaco(Schema):
    status: str
    num_chave: str
    st_disponivel: bool
    ds_espaco: str
    docente_nome: str
    data_retirada: str
    horario_retirada: str
    horario_previsto: str



@api.get("/status", response=StatusResponseSchema, tags=["Sistema"])
def status_sistema(request):
    return {
        "status": "ONLINE",
        "servidor": "Django Ninja + Supabase",
        "versao": "1.0.0",
    }


@api.get(
    "/consulta-uuid/{uuid}",
    response=ConsultaUUIDSchema,
    tags=["Portaria / Claviculário"],
)
def consultar_uuid(request, uuid: str):
    """Consulta um UUID de crachá docente ou tag de chave."""
    uuid_limpo = uuid.strip().upper()

    with connection.cursor() as cursor:
        cursor.execute(
        """
        SELECT
            tu.uuid_cracha,
            tu.nm_usuario,
            tu.st_status
        FROM tb_usuario tu 
        INNER JOIN tb_cargo tc ON tu.id_cargo = tc.id_cargo 
        WHERE tc.id_cargo = '2' AND tu.uuid_cracha = %s
        """,
            [uuid_limpo],
        )
        docente = cursor.fetchone()

        if docente:
            uuid_cracha, nome, ativo = docente
            if ativo:
                return {
                    "uuid": uuid_limpo,
                    "tipo_identificado": "DOCENTE",
                    "autorizado": True,
                    "mensagem": f"Docente {nome} identificado e ativo.",
                }
            return {
                "uuid": uuid_limpo,
                "tipo_identificado": "DOCENTE",
                "autorizado": False,
                "mensagem": f"Acesso Negado: Docente {nome} está inativo.",
            }

    return {
        "uuid": uuid_limpo,
        "tipo_identificado": "DESCONHECIDO",
        "autorizado": False,
        "mensagem": "Cartão/Tag não cadastrado no sistema.",
    }
    
@api.get(
    "/consulta-espaco/{num_chave}",
    response=ConsultaEspaco,
    tags=["Espaço / Nicho"],
)
def consultar_espaco(request, num_chave: str):
    """Consulta o status de um nicho específico."""
    num_chave_limpo = num_chave.strip().upper()

    with connection.cursor() as cursor:
        cursor.execute(
            """
            SELECT
                status,
                num_chave,
                nome_sala,
                docente_nome,
                data_retirada,
                horario_retirada,
                horario_previsto
            FROM vw_status_espacos
            WHERE num_chave = %s;
            """,
            [num_chave_limpo],
)
        espaco = cursor.fetchone()

        if espaco:
            status, num_chave, nome_sala, docente_nome, data_retirada, horario_retirada, horario_previsto = espaco
            st_disponivel = status == "disponivel"
            return {
                "status": "OK",
                "num_chave": num_chave_limpo,
                "st_disponivel": st_disponivel,
                "ds_espaco": nome_sala,
                "docente_nome": docente_nome if docente_nome else "",
                "data_retirada": data_retirada.isoformat() if data_retirada else "",
                "horario_retirada": horario_retirada.isoformat() if horario_retirada else "",
                "horario_previsto": horario_previsto.isoformat() if horario_previsto else "",
            }

    return {
        "status": "ERRO",
        "num_chave": num_chave_limpo,
        "st_disponivel": False,
        "ds_espaco": "",
        "docente_nome": "",
        "data_retirada": "",
        "horario_retirada": "",
        "horario_previsto": "",
    }

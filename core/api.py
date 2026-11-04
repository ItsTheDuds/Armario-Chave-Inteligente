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
            SELECT nome_docente, status_docente
            FROM tb_docente
            WHERE uuid_cracha = %s;
            """,
            [uuid_limpo],
        )
        docente = cursor.fetchone()

        if docente:
            nome, ativo = docente
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

        cursor.execute(
            """
            SELECT id_nicho, status_nicho
            FROM tb_nicho
            WHERE uuid_tag_chave = %s;
            """,
            [uuid_limpo],
        )
        chave = cursor.fetchone()

        if chave:
            id_nicho, status_nicho = chave
            return {
                "uuid": uuid_limpo,
                "tipo_identificado": "CHAVE",
                "autorizado": True,
                "mensagem": (
                    f"Chave vinculada ao Nicho #{id_nicho} "
                    f"(Status: {status_nicho})."
                ),
            }

    return {
        "uuid": uuid_limpo,
        "tipo_identificado": "DESCONHECIDO",
        "autorizado": False,
        "mensagem": "Cartão/Tag não cadastrado no sistema.",
    }

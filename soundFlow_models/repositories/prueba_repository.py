def verify_prueba(respuesta_user, prueba):
    return (respuesta_user['pregunta'] == prueba.datos) and (
                respuesta_user['respuesta'] == prueba.resultado) if True else False

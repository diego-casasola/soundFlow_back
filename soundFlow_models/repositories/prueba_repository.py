def verify_prueba(respuesta_user, prueba):
    return (respuesta_user['pregunta'] == prueba.datos) and (
                respuesta_user['respuesta'] == prueba.resultado) if True else False

def add_premios(user, model, trofeo):
    trofeoAd = model.objects.create(user_id=user.id, trofeo_id=trofeo[0].id)
    trofeoAd = model.objects.get(pk=trofeoAd.id)
    return trofeoAd
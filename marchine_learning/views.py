from admins.models import Myuser
from usuario.models import Trabajo , Perfil , powerbi_user
from .categorizacion import cargo_catego , sector_catego , genero_catego , nucleo_catego , respuesta_catego
from .models import RegresionLineal , RegresionLogistica
from powerbi.models import prediccion_power
import joblib
import numpy as np

# Create your views here.

class Modelo:
    def categoria_ml (id_user : int):
        data = Myuser.objects.get(pk = id_user)
        data1 = Perfil.objects.get(myuser_id = id_user)
        data2 = Trabajo.objects.get(myuser_id = id_user)

        nacimiento = data.birthdate.year
        id_genero = genero_catego()[data.gender]
        id_cargo = cargo_catego()[data2.position]
        id_sector = sector_catego()[data2.sector]
        nucleo = nucleo_catego()[data1.nucleo_familiar]
        fm_cambio = respuesta_catego()[data1.cambios_trabajo]
        tm_desplazamiento = data1.tiempoDesplazamiento
        t_casa = data1.horasDomestica
        t_familia = data1.horasPersonal
        t_remoto_meses = data2.tiempoDedicado/10

        ml = [[
            nacimiento,
            id_genero,
            id_cargo,
            id_sector,
            nucleo,
            fm_cambio,
            tm_desplazamiento,
            t_casa,
            t_familia,
            t_remoto_meses,
        ]]

        Modelo.powerbi_añadir(id_user , tm_desplazamiento , t_casa , t_familia , t_remoto_meses)

        return ml

    def conexion (self , id_user : int):
        # Lineal
        datos = Modelo.categoria_ml(id_user)

        model = joblib.load('modelos/lineal/modelo_productividad.pkl')
        nuevos_datos = np.array(datos)

        scaler = joblib.load('modelos/lineal/escalador_lineal.pkl')

        nuevos_datos_escalados = scaler.transform(nuevos_datos)

        prediccion = model.predict(nuevos_datos_escalados)
        prediccion = np.round(prediccion[0] , 2)
        prediccion = float(prediccion)

        if RegresionLineal.objects.filter(myuser_id = id_user).exists():
            lineal = RegresionLineal.objects.get(myuser_id = id_user)
            lineal.delete()

        Modelo.añadir_predi(id_user , prediccion)
        lineal = RegresionLineal(myuser_id = id_user, trabajoRemoto = prediccion)
        lineal.save()


        #Logistica
        modelo_cargado = joblib.load('modelos/logistica/modelo_logistico.pkl')

        escalador_cargado = joblib.load('modelos/logistica/escalador.pkl')

        codificador_etiquetas_cargado = joblib.load('modelos/logistica/codificador_etiquetas.pkl')

        nuevos_datos_escalados = escalador_cargado.transform(datos)

        predicciones_codificadas = modelo_cargado.predict(nuevos_datos_escalados)

        predicciones_decodificadas = codificador_etiquetas_cargado.inverse_transform(predicciones_codificadas)

        if RegresionLogistica.objects.filter(myuser_id = id_user).exists():
            logistica = RegresionLogistica.objects.get(myuser_id = id_user)
            logistica.delete()

        logistica = RegresionLogistica(myuser_id = id_user , trabajoRemoto = predicciones_decodificadas[0])
        logistica.save()

    def powerbi_añadir (id_user , hora_desplazamiento , hora_hogar , hora_familia , horaTrabajo):
        print(powerbi_user.objects.filter(myuser_id = id_user).exists())
        if not powerbi_user.objects.filter(myuser_id = id_user).exists():
            desplazamiento = powerbi_user (
                myuser_id = id_user,
                categoria_id = 1,
                valor = hora_desplazamiento
            )

            hogar = powerbi_user (
                myuser_id = id_user,
                categoria_id = 2,
                valor = hora_hogar
            )

            familia = powerbi_user (
                myuser_id = id_user,
                categoria_id = 3,
                valor = hora_familia
            )

            trabajo  = powerbi_user (
                myuser_id = id_user,
                categoria_id = 4,
                valor = horaTrabajo
            )

            predi  = powerbi_user (
                myuser_id = id_user,
                categoria_id = 5,
                valor = 0
            )

            desplazamiento.save()
            hogar.save()
            familia.save()
            trabajo.save()
            predi.save()

        else:
            Modelo.powerbi_editar(id_user , hora_desplazamiento , hora_hogar , hora_familia , horaTrabajo)

    def añadir_predi (id_user , valor_prediccion):
        data = [1,3,4.30,6.40]

        if  prediccion_power.objects.filter(myuser_id = id_user).exists():
            predicccion = prediccion_power.objects.get(myuser_id = id_user , categoria_id = 5)
            predicccion.valor = valor_prediccion
            predicccion.save()

        else:
            for i in range(1,5):
                power = prediccion_power(
                    categoria_id=i,
                    myuser_id=id_user,
                    valor= data[i-1],
                )

                power.save()

            power = prediccion_power(
                    categoria_id=5,
                    myuser_id=id_user,
                    valor = valor_prediccion,
                )
            power.save()


    def powerbi_editar (id_user , hora_desplazamiento , hora_hogar , hora_familia , horaTrabajo):
        desplazamiento = powerbi_user.objects.get(myuser_id=id_user, categoria_id=1)
        hogar = powerbi_user.objects.get(myuser_id=id_user, categoria_id=2)
        familia = powerbi_user.objects.get(myuser_id=id_user, categoria_id=3)
        trabajo = powerbi_user.objects.get(myuser_id=id_user, categoria_id=4)

        desplazamiento.valor = hora_desplazamiento
        hogar.valor = hora_hogar
        familia.valor = hora_familia
        trabajo.valor = horaTrabajo

        desplazamiento.save()
        hogar.save()
        familia.save()
        trabajo.save()

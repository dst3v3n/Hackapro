from admins.models import Myuser
from usuario.models import Trabajo , Perfil
from .categorizacion import cargo_catego , sector_catego , genero_catego , nucleo_catego , respuesta_catego
import joblib
import numpy as np

# Create your views here.

class Modelo:
    def categoria_ml (self , id_user : int):
        data = Myuser.objects.get(pk = id_user)
        data1 = Perfil.objects.get(myuser_id = id_user)
        data2 = Trabajo.objects.get(myuser_id = id_user)

        nacimiento = data.birthdate.year
        id_genero = genero_catego()[data.gender]
        id_cargo = cargo_catego()[data.position]
        id_sector = sector_catego()[data.sector]
        nucleo = nucleo_catego()[data1.nucleo_familiar]
        fm_cambio = respuesta_catego()[data1.cambios_trabajo] 
        tm_desplazamiento = data1.tiempoDesplazamiento
        t_casa = data1.horasDomestica
        t_familia = data1.horasPersonal
        t_remoto_meses = data2.tiempoDedicado

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
        
        return ml

    def conexion (self , id_user : int):
        datos = Modelo.categoria_ml(self , id_user)

        model = joblib.load('modelos/lineal/modelo_productividad.pkl')
        nuevos_datos = np.array(datos)  # Sustituye con tus valores

        #scaler = StandardScaler()
        scaler = joblib.load('modelos/lineal/escalador_lineal.pkl')

        nuevos_datos_escalados = scaler.transform(nuevos_datos)

        prediccion = model.predict(nuevos_datos_escalados)
 
        print(f'Predicción de horas de trabajo remoto: {prediccion[0]}')

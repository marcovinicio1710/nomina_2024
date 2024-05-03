from django.db import models
from django.contrib import auth
from django.contrib.auth.models import User


# Create your models here.

class Info_Empresa(models.Model):
    nombre_empresa = models.CharField(max_length=100, help_text="The name of the Enterprise.")
    Cedula_Juridica = models.CharField(max_length=50, help_text="The number of the RIF.")
    Direccion = models.CharField(max_length=300 , help_text="Address.")
    Ciudad = models.CharField(max_length=50 , help_text="City.")
    Estado = models.CharField(max_length=50 , help_text="State.")
    Pais = models.CharField(max_length=50 , help_text="Country.", default='Panama')
    Zip_code = models.IntegerField( help_text="zipcode", default= 0000)
    Telefono = models.CharField(max_length=15, help_text="telepohone number")
    Correo = models.EmailField(help_text="email of the company")
    Pagina_web = models.URLField(max_length=300 , help_text="Pagina Oficial de la compania")
    Representante = models.CharField(max_length=100, help_text="The name of the representante")
    Representante_email = models.EmailField(help_text="email of the representante")
    Encargado_RRHH = models.CharField(max_length=100, help_text="The name of the Encargado RRHH")
    Encargado_RRHH_email = models.EmailField(help_text="email of the Encargado RRHH")



    def __str__(self):
        return (self.nombre_empresa+' '+self.Cedula_Juridica)
    
class Info_Clientes(models.Model):
    nombre_empresa = models.CharField(max_length=100, help_text="The name of the Enterprise.")
    Cedula_Juridica = models.CharField(max_length=50, help_text="The number of the RIF.")
    Codigo_cliente=models.CharField(max_length=20, help_text="Registro del cliente.")
    Direccion = models.CharField(max_length=300 , help_text="Address.")
    Ciudad = models.CharField(max_length=50 , help_text="City.")
    Estado = models.CharField(max_length=50 , help_text="State.")
    Pais = models.CharField(max_length=50 , help_text="Country.", default='Panama')
    Zip_code = models.IntegerField( help_text="zipcode", default= 0000)
    Telefono = models.CharField(max_length=15, help_text="telepohone number")
    Correo = models.EmailField(help_text="email of the company")
    Pagina_web = models.URLField(max_length=300 , help_text="Pagina Oficial de la compania", default='www.not-a-web-page.com')
    Representante = models.CharField(max_length=100, help_text="The name of the representante")
    Representante_email = models.EmailField(help_text="email of the representante")
    status = models.CharField(max_length=25, help_text="The name of the representante", default='Pendiente')
    

class Departamento_Empresa(models.Model):
    Nombre_departamento = models.CharField(max_length=100, help_text="Crear nombre departamento")
    Comentario= models.CharField(max_length=200, help_text="Crear comentario departamento")
    Empresa = models.ForeignKey(Info_Empresa, on_delete=models.PROTECT)
    def __str__(self):
        return (self.Nombre_departamento)

class Colaboradores(models.Model): 
    Usuario_permiso= models.BooleanField(default=False)
    Colaborador_nombre= models.CharField(max_length=50, help_text="The name of the worker.")
    Colaborador_apellido= models.CharField(max_length=50, help_text="The lastname of the worker.")
    Tipo_documento= models.CharField(max_length=50, help_text="tipo documento of the worker.")
    Nro_Identificacion= models.CharField(max_length=50, help_text="The number of the RIF.")
    Nro_Seguro_Social= models.CharField(max_length=50, help_text="The number of the RIF.")
    Direccion = models.CharField(max_length=300 , help_text="Address.")
    Ciudad = models.CharField(max_length=50 , help_text="City.")
    Pais = models.CharField(max_length=50 , help_text="Country.", default='Panama')
    Zip_code = models.IntegerField( help_text="zipcode", default= 0000)
    Telefono = models.CharField(max_length=15, help_text="telepohone number")
    Correo = models.EmailField(help_text="email of the company")
    Profesion = models.CharField(max_length=100,help_text="email of the company" )
    Cargo=models.CharField(max_length=100,help_text="cargo of the company" )
    Departamento=models.CharField(max_length=100,help_text="si es ruta o no " )
    Tipo_contrato=models.CharField(max_length=100,help_text="tipo de contrato " )
    Tipo_pago=models.CharField(max_length=100,help_text="como se va pagar el sueldo " )
    Sueldo=models.FloatField(help_text="como se va pagar el sueldo " )
    Nombre_Banco=models.CharField(max_length=100,help_text="como se va pagar el sueldo " )
    Tipo_cuenta=models.CharField(max_length=100,help_text="como se va pagar el sueldo " )
    Nro_cuenta=models.BigIntegerField(help_text="solo en numero el numero de cuenta " )
    Fecha_Ingreso=models.DateField( help_text="fecha ingreso")
    Fecha_Egreso=models.DateField( help_text="fecha egreso",default="9999-12-31")
    Contanto_Urgencia = models.CharField(max_length=60, help_text="The number of the RIF.", default='Sin contacto')
    Telefono_Urgencia = models.CharField(max_length=15, help_text="telepohone number", default='Sin contacto')
    Status = models.CharField(max_length=25, help_text="The name of the representante", default='Activo') 
    Hora_entrada=models.CharField(max_length=50, help_text="hora entrada.", default='08')
    
    Hora_salida=models.CharField(max_length=50, help_text="hora entrada.",default='17')
    Vacaciones_totales= models.IntegerField( help_text="total vacaciones desde que inicio empresa", default= 0)
    Vacaciones_usadas= models.IntegerField( help_text="total vacaciones desde que inicio empresa", default= 0)

    Jornada_Laboral_Equitativa_Semanal= models.BooleanField( help_text="zipcode", default= True)
    
    Dia_descanso_1= models.IntegerField( help_text="zipcode", default= 6)
    Dia_descanso_2= models.IntegerField( help_text="zipcode", default= 8)
    Almuerzo_bool= models.BooleanField (help_text="si debe tomar Hora Almuerzo", default= True)
    Inicio_Hora_Almuerzo=models.IntegerField( help_text="zipcode", default= 12)
    Jornada_diaria=models.FloatField( help_text="jornada diario de trabajo ya con el almuerzo quitado", default= 8)
    Jornada_semanal=models.IntegerField( help_text="jornada semanal de trabajo ", default= 48)
    Tipo_Jornada=models.CharField(max_length=50, help_text="tipo jornada laboral",default='Diurno')

    Sexo=models.CharField(max_length=20, help_text="sexo colaborador",default='Masculino')
    #Fecha_nacimiento=models.DateField( help_text="fecha ingreso", default="1900-12-31")
    Fecha_nacimiento=models.CharField(max_length=20, help_text="sexo colaborador",default='Masculino')
    Estado_civil=models.CharField(max_length=30, help_text="estado civil colaborador",default='Soltero/a')
    Nro_Hijos=models.IntegerField( help_text="hijos del colaborador",default=0)

    Posee_Licencia_Vehicular=models.CharField(max_length=10, help_text="licencia de conducir del colaborador",default='Si')
    Posee_Carro_Vehicular=models.CharField(max_length=10, help_text="Posee carro vehicular del colaborador",default='Si')
    Supervisor = models.ForeignKey('self', on_delete=models.PROTECT ,  null=True, blank=True)
    imagen = models.ImageField( default='no_hay_archivo.jpg')
    Quien_agrego_Jornada=models.CharField(max_length=50, help_text="Quien agrego la jornada", default='Administrador')



#agregar tipo de jornada semana
    #agregar dias libre de la semana


    def __str__(self):
        return (self.Colaborador_nombre+'  '+self.Colaborador_apellido)
    
class Dias_Feriados(models.Model):
    Dia_Feriado= models.DateField(help_text="Dia feriado en el pais.")
    Motivo_Feriado= models.CharField(max_length=100, help_text="Motivo del Feriado", default='Dia Feriado con gozo de prestaciones')
    def __str__(self):
        return (self.Dia_Feriado+'  '+self.Motivo_Feriado)

class UserProfile(models.Model):
    user = models.OneToOneField(User, on_delete=models.CASCADE)
    # Agregar campos adicionales según tus necesidades
    Status = models.CharField(max_length=20, default='Activo')
    nivel_seguridad = models.IntegerField(default=5)
    Colaborador = models.ForeignKey(Colaboradores, on_delete=models.PROTECT, null=True, blank=True)
    contrasena_default=models.BooleanField(default=True)
    Administrador=models.CharField(max_length=20, default='Administrador')
    creado_por=models.CharField(max_length=20, default='Administrador')
    fecha_creacion=models.DateField(default='2024-01-02')
    

    def __str__(self):
        return self.user.username


class Hoja_tiempo(models.Model):
    Entrada=models.CharField(max_length=30, help_text="entrada de la jornada laboral")
    Salida=models.CharField(max_length=30, help_text="entrada de la jornada laboral")
    Dia_entrada=models.DateField(help_text="dia entrada", default='2024-01-02')
    Dia_salida=models.DateField(help_text="dia salida", default='2024-01-02')
    Colaborador= models.ForeignKey(Colaboradores,
                                  on_delete=models.PROTECT)
    Empresa=models.ForeignKey(Info_Clientes,
                                  on_delete=models.PROTECT , default=1)
    Quien_agrego_Jornada=models.CharField(max_length=50, help_text="Quien agrego la jornada", default='Administrador')
    Minutos_Trabajads= models.FloatField( help_text="minutos trabajados en todo la jornada laboral")
    Minutos_Trabajads_Jornada_Laboral= models.FloatField( help_text="minutos trabajados en todo la jornada laboral")
    Minutos_Extras_Diurnos= models.FloatField( help_text="minutos extras entre 6am a 6pm")
    Minutos_Extras_Noctuno= models.FloatField( help_text="minutos extras entre 6pm a 6am")
    Minutos_Laborales_extras= models.FloatField( help_text="minutos extras para jornada de ruta o medio turno")
    Minutos_Tardia= models.FloatField( help_text="minutos extras para jornada de ruta o medio turno")
    Minutos_Faltantes_turno= models.FloatField( help_text="minutos faltante de turno")
    Minutos_llego_temprano= models.FloatField( help_text="minutos faltante de turno")
    Minutos_extras_mixtas_nocturnas= models.FloatField( help_text="minutos faltante de turno")
    Minutos_extras_mixtas_diurnas= models.FloatField( help_text="minutos faltante de turno")
    #horas despues 3hr extras
    Minutos_extras_diurnos_3h= models.FloatField( help_text="minutos faltante de turno")
    Minutos_extras_nocturnos_3h= models.FloatField( help_text="minutos faltante de turno")
    Minutos_de_extras_mixtas_diurnas_3hr= models.FloatField( help_text="minutos faltante de turno")
    Minutos_de_extras_mixtas_nocturnas_3hr= models.FloatField( help_text="minutos faltante de turno")
    Laboro_dia_domingo_descanso= models.BooleanField( help_text="minutos faltante de turno")
    laboro_dia_feriado= models.BooleanField( help_text="minutos faltante de turno")
    Ausencias_Aprobada=models.BooleanField( help_text="si fueron aprobadas las ausencia de toempo jornada",default='False')
    Ausencias_Aprobadas_por=models.CharField(max_length=60, help_text="quien aprobo las ausencia", default='Sin aprobar')
    HR_3_Aprobada=models.BooleanField( help_text="si fueron aprobadas las ausencia de toempo jornada",default='False')
    HR_3_Aprobadas_por=models.CharField(max_length=60, help_text="quien aprobo las ausencia", default='Sin aprobar')

    def __str__(self):
        return (self.Entrada+'  '+self.Colaborador)

class Planificacion(models.Model):
    
    Dia_Inicio_Planificacion=models.DateField(help_text="dia entrada", default='2024-01-02')
    Dia_Salidad_Planificacion=models.DateField(help_text="dia salida", default='2024-01-02')
    Colaborador= models.ForeignKey(Colaboradores,
                                  on_delete=models.PROTECT)
    Cliente=models.ForeignKey(Info_Clientes,
                                  on_delete=models.PROTECT , default=1)
    #Lunes
    Hr_Laboradas_Lunes=models.FloatField()
    Entrada_Lunes=models.CharField(max_length=30, help_text="entrada de la jornada laboral")
    Salida_Lunes=models.CharField(max_length=30, help_text="entrada de la jornada laboral")
    Almuerzo_bool_Lunes=models.BooleanField (help_text="si debe tomar Hora Almuerzo", default= True)
    Inicio_Hora_Almuerzo_Lunes=models.IntegerField( help_text="zipcode", default= 12)
    Jornada_Nocturna_bool_Lunes=models.BooleanField (help_text="si dpasar una noche al dia siguiente", default= False)
    Dia_Descanso_bool_Lunes=models.BooleanField (help_text="si toca descansar Lunes", default= False)
    #Martes
    Hr_Laboradas_Martes=models.FloatField()
    Entrada_Martes=models.CharField(max_length=30, help_text="entrada de la jornada laboral")
    Salida_Martes=models.CharField(max_length=30, help_text="entrada de la jornada laboral")
    Almuerzo_bool_Martes=models.BooleanField (help_text="si debe tomar Hora Almuerzo", default= True)
    Inicio_Hora_Almuerzo_Martes=models.IntegerField( help_text="zipcode", default= 12)
    Jornada_Nocturna_bool_Martes=models.BooleanField (help_text="si dpasar una noche al dia siguiente", default= False)
    Dia_Descanso_bool_Martes=models.BooleanField (help_text="si toca descansar Martes", default= False)
    #Miercoles
    Hr_Laboradas_Miercoles=models.FloatField()
    Entrada_Miercoles=models.CharField(max_length=30, help_text="entrada de la jornada laboral")
    Salida_Miercoles=models.CharField(max_length=30, help_text="entrada de la jornada laboral")
    Almuerzo_bool_Miercoles=models.BooleanField (help_text="si debe tomar Hora Almuerzo", default= True)
    Inicio_Hora_Almuerzo_Miercoles=models.IntegerField( help_text="zipcode", default= 12)
    Jornada_Nocturna_bool_Miercoles=models.BooleanField (help_text="si dpasar una noche al dia siguiente", default= False)
    Dia_Descanso_bool_Miercoles=models.BooleanField (help_text="si toca descansar Miercoles", default= False)
    #Jueves
    Hr_Laboradas_Jueves=models.FloatField()
    Entrada_Jueves=models.CharField(max_length=30, help_text="entrada de la jornada laboral")
    Salida_Jueves=models.CharField(max_length=30, help_text="entrada de la jornada laboral")
    Almuerzo_bool_Jueves=models.BooleanField (help_text="si debe tomar Hora Almuerzo", default= True)
    Inicio_Hora_Almuerzo_Jueves=models.IntegerField( help_text="zipcode", default= 12)
    Jornada_Nocturna_bool_Jueves=models.BooleanField (help_text="si dpasar una noche al dia siguiente", default= False)
    Dia_Descanso_bool_Jueves=models.BooleanField (help_text="si toca descansar Jueves", default= False)
    #Viernes
    Hr_Laboradas_Viernes=models.FloatField()
    Entrada_Viernes=models.CharField(max_length=30, help_text="entrada de la jornada laboral")
    Salida_Viernes=models.CharField(max_length=30, help_text="entrada de la jornada laboral")
    Almuerzo_bool_Viernes=models.BooleanField (help_text="si debe tomar Hora Almuerzo", default= True)
    Inicio_Hora_Almuerzo_Viernes=models.IntegerField( help_text="zipcode", default= 12)
    Jornada_Nocturna_bool_Viernes=models.BooleanField (help_text="si dpasar una noche al dia siguiente", default= False)
    Dia_Descanso_bool_Viernes=models.BooleanField (help_text="si toca descansar Viernes", default= False)
    #Sabado
    Hr_Laboradas_Sabado=models.FloatField()
    Entrada_Sabado=models.CharField(max_length=30, help_text="entrada de la jornada laboral")
    Salida_Sabado=models.CharField(max_length=30, help_text="entrada de la jornada laboral")
    Almuerzo_bool_Sabado=models.BooleanField (help_text="si debe tomar Hora Almuerzo", default= True)
    Inicio_Hora_Almuerzo_Sabado=models.IntegerField( help_text="zipcode", default= 12)
    Jornada_Nocturna_bool_Sabado=models.BooleanField (help_text="si dpasar una noche al dia siguiente", default= False)
    Dia_Descanso_bool_Sabado=models.BooleanField (help_text="si toca descansar Sabado", default= False)
    #Doming
    Hr_Laboradas_Domingo=models.FloatField(default= 0)
    Entrada_Domingo=models.CharField(max_length=30, help_text="entrada de la jornada laboral",default= '08:00')
    Salida_Domingo=models.CharField(max_length=30, help_text="entrada de la jornada laboral", default= '08:00')
    Almuerzo_bool_Domingo=models.BooleanField (help_text="si debe tomar Hora Almuerzo", default= True)
    Inicio_Hora_Almuerzo_Domingo=models.IntegerField( help_text="zipcode", default= 12)
    Jornada_Nocturna_bool_Domingo=models.BooleanField (help_text="si dpasar una noche al dia siguiente", default= False)
    Dia_Descanso_bool_Domingo=models.BooleanField (help_text="si toca descansar Domingo", default= False)

class Permisos(models.Model):
    
    Dia_inicio_permiso=models.DateField(help_text="dia entrada", default='2024-01-02')
    Dia_fin_permiso=models.DateField(help_text="dia salida", default='2024-01-02')
    Dias_permiso=models.IntegerField()
    Colaborador= models.ForeignKey(Colaboradores,
                                  on_delete=models.PROTECT)
    Tipo_permiso=models.CharField(max_length=50, help_text="Quien agrego la jornada", default='Vacaciones')
    Comentario_Permiso=models.CharField(max_length=200, help_text="Quien agrego la jornada", default='Compentario no Agregado')
    Estado_Permiso=models.CharField(max_length=50, help_text="Pendiente, Rechazado, Aprobado", default='Pendiente')

    Quien_agrego_Jornada=models.CharField(max_length=50, help_text="Quien agrego la jornada", default='Administrador')
    Aprobado_por=models.CharField(max_length=50, help_text="Quien agrego la jornada", default='Estado Pendiente')

    Documento_permiso=models.FileField(default='/no_hay_archivo')
    Pagado_por_Empresa_o_CCSS=models.FileField(default='empresa')
    
    def __str__(self):
        return (self.Dia_inicio_permiso+'  '+self.Dia_fin_permiso+' '+self.Colaborador)

class Cerrar_Planilla(models.Model):
    Periodo=models.CharField(max_length=15, help_text="QUE QUATER ESTA", default='Q1-02-2020')
    Empresa= models.ForeignKey(Info_Empresa,
                                  on_delete=models.PROTECT)



class Acreedores(models.Model):
    
    Dia_inicio_cobro=models.DateField(help_text="dia entrada", default='2024-01-01')
    Dia_fin_cobro=models.DateField(help_text="dia salida", default='9999-12-31')
    Meses_de_cobro=models.IntegerField(default=0)
    Monto_total=models.FloatField()
    Monto_mensual=models.FloatField()
    Colaborador= models.ForeignKey(Colaboradores,
                                  on_delete=models.PROTECT)
    Tipo_acreeditor=models.CharField(max_length=50, help_text="Quien agrego la jornada", default='Empresa')
    Nombre_acreeditor=models.CharField(max_length=120, help_text="Quien agrego la jornada", default='Empresa')
    Comentario_Permiso=models.CharField(max_length=200, help_text="Quien agrego la jornada", default='Compentario no Agregado')
    Estado_Permiso=models.CharField(max_length=50, help_text="Pendiente, Rechazado, Aprobado", default='Pendiente')

    Quien_agrego_Jornada=models.CharField(max_length=50, help_text="Quien agrego la jornada", default='Administrador')
    
    Aprobado_por=models.CharField(max_length=50, help_text="Quien agrego la jornada", default='Estado Pendiente')
    cuotas_restante=models.FloatField(default=0)
    dinero_pagado=models.FloatField(default=0)
    Documento_permiso=models.FileField(default='/no_hay_archivo')
    
    
    def __str__(self):
        return (self.Dia_inicio_cobro+'  '+self.Monto_mensual+' '+self.Colaborador)

class Acreedores_quincena(models.Model):
    
    Dia_Inicio_cobro=models.DateField(help_text="dia entrada", default='2024-01-01')
    Periodo_Cobro=models.CharField(max_length=50, help_text="Quien agrego la jornada", default='Q1-1-2023')
    Monto_periodo=models.FloatField()
    Nro_Cuota=models.IntegerField()
    Total_monto_abonado=models.FloatField()
    Acreedores= models.ForeignKey(Acreedores,
                                  on_delete=models.PROTECT)
    Tipo_Operacion=models.CharField(max_length=50, help_text="Planilla o Liquidacion", default='Planilla')
    Realizo_Cobreo= models.BooleanField( default=False)
    
 
class Ajuste_Planilla(models.Model):
    
    
    Retencion_Iva=models.BooleanField( default=False)
    Monto=models.FloatField()
    Etapa=models.CharField(max_length=15, help_text="QUE QUATER ESTA", default='Q1-02-2020')
    Colaborador= models.ForeignKey(Colaboradores,
                                  on_delete=models.PROTECT)
    Tipo_Ajuste=models.CharField(max_length=50, help_text="Quien agrego la jornada", default='Sin Ajuste')
    Concepto_Ajuste=models.CharField(max_length=60, help_text="Quien agrego la jornada", default='Sin Descripcion')
    Comentario=models.CharField(max_length=500, help_text="Quien agrego la jornada", default='Compentario no Agregado')
    Estado_Permiso=models.CharField(max_length=50, help_text="Pendiente, Rechazado, Aprobado", default='Pendiente')
    Quien_agrego_Jornada=models.CharField(max_length=50, help_text="Quien agrego la jornada", default='Administrador')
    Aprobado_por=models.CharField(max_length=50, help_text="Quien agrego la jornada", default='Proceso Pendiente')
    Aprobado_bool=models.BooleanField(default=False)
    
    
    def __str__(self):
        return (str(self.Monto)+'  '+self.Etapa+' '+self.Colaborador.Nro_Identificacion)

class Generar_Horario_Aministrativo(models.Model):
    
    
    Dias_Trabajados=models.IntegerField( help_text=" dias trabajado", default=0)
    Dias_Permiso=models.IntegerField( help_text=" dias perimso", default=0)
    Periodo=models.CharField(max_length=15, help_text="QUE QUATER ESTA", default='Q1-02-2020')
    Colaborador= models.ForeignKey(Colaboradores,
                                  on_delete=models.PROTECT)
    
    Estado_Generacion=models.CharField(max_length=50, help_text="Pendiente, Rechazado, Aprobado", default='Pendiente')
    Quien_agrego_Jornada=models.CharField(max_length=50, help_text="Quien agrego la jornada", default='Administrador')
    Aprobado_por=models.CharField(max_length=50, help_text="Quien agrego la jornada", default='Sin_Aprobaciones')
    Aprobado_bool=models.BooleanField(default=False)
    
    
    def __str__(self):
        return (str(self.Periodo)+' '+self.Colaborador.Nro_Identificacion)

class Panilla_por_periodo_quincenal(models.Model):
    Periodo=models.CharField(max_length=15, help_text="QUE QUATER ESTA", default='Q1-02-2020')
    Colaborador= models.ForeignKey(Colaboradores,
                                  on_delete=models.PROTECT)
    
    Sueldo_quincenal=models.FloatField(default=0)
    Sueldo_Diario=models.FloatField(default=0)
    Sueldo_HR=models.FloatField(default=0)
    Sueldo_MIN=models.FloatField(default=0)
    Trabajo_quincena_sin_falta=models.BooleanField(default=True)
    Dias_Trabajado=models.IntegerField(default=0)
    Dias_Trabajado_Completo=models.IntegerField(default=0)
    Dias_trabajados_incompleto=models.IntegerField(default=0)
    Dias_trabajados_hr_regulares=models.IntegerField(default=0)
    Dias_Vacaciones=models.IntegerField(default=0)
    Dias_Incapacidad=models.IntegerField(default=0)
    Dias_Licencia_Paga=models.IntegerField(default=0)
    Dias_Descanso=models.IntegerField(default=0)
    Dias_Trabajo_Feriado_descanso=models.IntegerField(default=0)
    Pago_Dias_Trabajo_Feriado_descanso=models.FloatField(default=0)
    Dias_Trabajo_Feriado=models.IntegerField(default=0)
    Pago_Dias_Trabajo_Feriado=models.FloatField(default=0)
    Dias_Trabajo_Descanso=models.IntegerField(default=0)
    Pago_Dias_Trabajo_Descanso=models.FloatField(default=0)
    Dias_Trabajo_HR_Regulares_Adicionales=models.IntegerField(default=0)
    Pago_Dias_Trabajo_HR_Regulares_Adicionales=models.FloatField(default=0)
    MIN_Ausencia=models.IntegerField(default=0)
    Pago_MIN_Ausencia=models.FloatField(default=0)
    Dia_ausencia=models.IntegerField(default=0)
    Pago_Dia_ausencia=models.FloatField(default=0)
    #HORA EXTRA
    HR_extras_diurnas=models.IntegerField(default=0)
    Pago_HR_extras_diurnas=models.FloatField(default=0)
    HR_extras_nocturnas=models.IntegerField(default=0)
    Pago_HR_extras_nocturnas=models.FloatField(default=0)
    HR_extras_diurnas_mixta=models.IntegerField(default=0)
    Pago_HR_extras_diurnas_mixta=models.FloatField(default=0)
    HR_extras_nocturnas_mixta=models.IntegerField(default=0)
    Pago_HR_extras_nocturnas_mixta=models.FloatField(default=0)
    #+3h
    HR_extras_diurnas_3h=models.IntegerField(default=0)
    Pago_HR_extras_diurnas_3h=models.FloatField(default=0)
    HR_extras_nocturnas_3h=models.IntegerField(default=0)
    Pago_HR_extras_nocturnas_3h=models.FloatField(default=0)
    HR_extras_diurnas_mixta_3h=models.IntegerField(default=0)
    Pago_HR_extras_diurnas_mixta_3h=models.FloatField(default=0)
    HR_extras_nocturnas_mixta_3h=models.IntegerField(default=0)
    Pago_HR_extras_nocturnas_mixta_3h=models.FloatField(default=0)
    ##hr extras feriado
    HR_extras_diurnas_Feriado=models.IntegerField(default=0)
    Pago_HR_extras_diurnas_Feriado=models.FloatField(default=0)
    HR_extras_nocturnas_Feriado=models.IntegerField(default=0)
    Pago_HR_extras_nocturnas_Feriado=models.FloatField(default=0)
    HR_extras_diurnas_mixta_Feriado=models.IntegerField(default=0)
    Pago_HR_extras_diurnas_mixta_Feriado=models.FloatField(default=0)
    HR_extras_nocturnas_mixta_Feriado=models.IntegerField(default=0)
    Pago_HR_extras_nocturnas_mixta_Feriado=models.FloatField(default=0)
    #+3h
    HR_extras_diurnas_3h_Feriado=models.IntegerField(default=0)
    Pago_HR_extras_diurnas_3h_Feriado=models.FloatField(default=0)
    HR_extras_nocturnas_3h_Feriado=models.IntegerField(default=0)
    Pago_HR_extras_nocturnas_3h_Feriado=models.FloatField(default=0)
    HR_extras_diurnas_mixta_3h_Feriado=models.IntegerField(default=0)
    Pago_HR_extras_diurnas_mixta_3h_Feriado=models.FloatField(default=0)
    HR_extras_nocturnas_mixta_3h_Feriado=models.IntegerField(default=0)
    Pago_HR_extras_nocturnas_mixta_3h_Feriado=models.FloatField(default=0)
    #HORA EXTRA Dia descanso
    HR_extras_diurnas_descanso=models.IntegerField(default=0)
    Pago_HR_extras_diurnas_descanso=models.FloatField(default=0)
    HR_extras_nocturnas_descanso=models.IntegerField(default=0)
    Pago_HR_extras_nocturnas_descanso=models.FloatField(default=0)
    HR_extras_diurnas_mixta_descanso=models.IntegerField(default=0)
    Pago_HR_extras_diurnas_mixta_descanso=models.FloatField(default=0)
    HR_extras_nocturnas_mixta_descanso=models.IntegerField(default=0)
    Pago_HR_extras_nocturnas_mixta_descanso=models.FloatField(default=0)
    #+3h
    HR_extras_diurnas_3h_descanso=models.IntegerField(default=0)
    Pago_HR_extras_diurnas_3h_descanso=models.FloatField(default=0)
    HR_extras_nocturnas_3h_descanso=models.IntegerField(default=0)
    Pago_HR_extras_nocturnas_3h_descanso=models.FloatField(default=0)
    HR_extras_diurnas_mixta_3h_descanso=models.IntegerField(default=0)
    Pago_HR_extras_diurnas_mixta_3h_descanso=models.FloatField(default=0)
    HR_extras_nocturnas_mixta_3h_descanso=models.IntegerField(default=0)
    Pago_HR_extras_nocturnas_mixta_3h_descanso=models.FloatField(default=0)
    #Bonos
    Pago_Bono_con_Impuesto=models.FloatField(default=0)
    Pago_Bono_sin_Impuesto=models.FloatField(default=0)
    #deduciones
    Deduccion_con_Impuesto=models.FloatField(default=0)
    Deduccion_sin_Impuesto=models.FloatField(default=0)
    #acreedores hipotecario
    Descuento_Acreedores_Hipotecario=models.FloatField(default=0)
    Descuento_Acreedores_Empresa=models.FloatField(default=0)
    #totales a favor
    Sueldo_base_quincenal=models.FloatField(default=0)
    Pago_Total_Sobretiempo_quincenal=models.FloatField(default=0)
    Pago_dias_trabj_fer_con_descanso=models.FloatField(default=0)
    Pago_dias_traba_feriados=models.FloatField(default=0)
    Pago_dias_traba_feriados=models.FloatField(default=0)
    Pago_dias_trabaja_descanso=models.FloatField(default=0)
    
    Pago_Incapacidad=models.FloatField(default=0)
    Pago_Licencia_paga=models.FloatField(default=0)
    Sueldo_Bruto=models.FloatField(default=0)
    
    #
    Pago_quincena_despues_descuento=models.FloatField(default=0)
    #
    Deduccion_Seguro_Social=models.FloatField(default=0)
    Deduccion_Seguro_Educacional=models.FloatField(default=0)
    Deduccion_ISLR=models.FloatField(default=0)
    Total_deduciones_Ley=models.FloatField(default=0)
    Total_deduciones_quinceas=models.FloatField(default=0)
    # BONOS POR DEBAJO LA MESA
    Pago_total_bonos_sin_impuesto=models.FloatField(default=0)
    Pago_Sueldo_neto=models.FloatField(default=0)
    ##Patrono
    Decimo_xiii_quincena_Bruto=models.FloatField(default=0)
    Deduccion_Seg_social_decimo=models.FloatField(default=0)
    Deduccion_ISLR_Decimmo_xiii=models.FloatField(default=0)
    Decimo_xiii_quincena_Neto=models.FloatField(default=0)
    Deduccion_Seg_social_Patron=models.FloatField(default=0)
    Deduccion_Seg_social_decimo_Patron=models.FloatField(default=0)
    Deduccion_Seguro_Educacional_Patron=models.FloatField(default=0)
    Prima_Antiguedad_Patron=models.FloatField(default=0)
    Riesgo_Profesional_Patron=models.FloatField(default=0)
    Vacacionciones_Acumuladas_Patron=models.FloatField(default=0)
    #totales
    Totales_patronales=models.FloatField(default=0)
    Total_general_sueldo=models.FloatField(default=0)
    #fecha pago
    Fecha_pago_quincena=models.DateField(default='2024-01-15')
    #vacacione
    Pago_Vacaciones=models.FloatField(default=0)
    Vacaciones_Seguro_Social=models.FloatField(default=0)
    Vacaciones_Seguro_educacion=models.FloatField(default=0)
    Vacaciones_ISLR=models.FloatField(default=0)
    Deducion_Vacaciones_Totales=models.FloatField(default=0)
    Pago_Vacaciones_Neto=models.FloatField(default=0)
    Vacaciones_Seguro_Social_patron=models.FloatField(default=0)
    Vacaciones_Seguro_educacion_patron=models.FloatField(default=0)
    Deducion_Vacaciones_Totales_patron=models.FloatField(default=0)
    #XIII de pago 
    Pago_XIII_periodo_Bruto=models.FloatField(default=0)
    Pago_XIII_periodo_Seguro_Social=models.FloatField(default=0)
    
    Pago_XIII_periodo_ISLR=models.FloatField(default=0)
    

    Pago_XIII_periodo_Neto=models.FloatField(default=0)
    Deduccion_XIII_periodo_Seguro_social_patron=models.FloatField(default=0)
    

class Panilla_por_periodo_quincenal_clientes(models.Model):
    Periodo=models.CharField(max_length=15, help_text="QUE QUATER ESTA", default='Q1-02-2020')
    Colaborador= models.ForeignKey(Colaboradores,
                                  on_delete=models.PROTECT)
    Cliente= models.ForeignKey(Info_Clientes,
                                  on_delete=models.PROTECT)
    
    Sueldo_quincenal=models.FloatField(default=0)
    Sueldo_Diario=models.FloatField(default=0)
    Sueldo_HR=models.FloatField(default=0)
    Sueldo_MIN=models.FloatField(default=0)
    Trabajo_quincena_sin_falta=models.BooleanField(default=True)
    Dias_Trabajado=models.FloatField(default=0)
    Dias_Trabajado_Completo=models.FloatField(default=0)
    Dias_trabajados_incompleto=models.FloatField(default=0)
    Dias_trabajados_hr_regulares=models.FloatField(default=0)
    Dias_Vacaciones=models.FloatField(default=0)
    Dias_Incapacidad=models.FloatField(default=0)
    Dias_Licencia_Paga=models.FloatField(default=0)
    Dias_Descanso=models.FloatField(default=0)
    Dias_Trabajo_Feriado_descanso=models.FloatField(default=0)
    Pago_Dias_Trabajo_Feriado_descanso=models.FloatField(default=0)
    Dias_Trabajo_Feriado=models.FloatField(default=0)
    Pago_Dias_Trabajo_Feriado=models.FloatField(default=0)
    Dias_Trabajo_Descanso=models.FloatField(default=0)
    Pago_Dias_Trabajo_Descanso=models.FloatField(default=0)
    Dias_Trabajo_HR_Regulares_Adicionales=models.FloatField(default=0)
    Pago_Dias_Trabajo_HR_Regulares_Adicionales=models.FloatField(default=0)
    MIN_Ausencia=models.FloatField(default=0)
    Pago_MIN_Ausencia=models.FloatField(default=0)
    Dia_ausencia=models.FloatField(default=0)
    Pago_Dia_ausencia=models.FloatField(default=0)
    #HORA EXTRA
    HR_extras_diurnas=models.FloatField(default=0)
    Pago_HR_extras_diurnas=models.FloatField(default=0)
    HR_extras_nocturnas=models.FloatField(default=0)
    Pago_HR_extras_nocturnas=models.FloatField(default=0)
    HR_extras_diurnas_mixta=models.FloatField(default=0)
    Pago_HR_extras_diurnas_mixta=models.FloatField(default=0)
    HR_extras_nocturnas_mixta=models.FloatField(default=0)
    Pago_HR_extras_nocturnas_mixta=models.FloatField(default=0)
    #+3h
    HR_extras_diurnas_3h=models.FloatField(default=0)
    Pago_HR_extras_diurnas_3h=models.FloatField(default=0)
    HR_extras_nocturnas_3h=models.FloatField(default=0)
    Pago_HR_extras_nocturnas_3h=models.FloatField(default=0)
    HR_extras_diurnas_mixta_3h=models.FloatField(default=0)
    Pago_HR_extras_diurnas_mixta_3h=models.FloatField(default=0)
    HR_extras_nocturnas_mixta_3h=models.FloatField(default=0)
    Pago_HR_extras_nocturnas_mixta_3h=models.FloatField(default=0)
    ##hr extras feriado
    HR_extras_diurnas_Feriado=models.FloatField(default=0)
    Pago_HR_extras_diurnas_Feriado=models.FloatField(default=0)
    HR_extras_nocturnas_Feriado=models.FloatField(default=0)
    Pago_HR_extras_nocturnas_Feriado=models.FloatField(default=0)
    HR_extras_diurnas_mixta_Feriado=models.FloatField(default=0)
    Pago_HR_extras_diurnas_mixta_Feriado=models.FloatField(default=0)
    HR_extras_nocturnas_mixta_Feriado=models.FloatField(default=0)
    Pago_HR_extras_nocturnas_mixta_Feriado=models.FloatField(default=0)
    #+3h
    HR_extras_diurnas_3h_Feriado=models.FloatField(default=0)
    Pago_HR_extras_diurnas_3h_Feriado=models.FloatField(default=0)
    HR_extras_nocturnas_3h_Feriado=models.FloatField(default=0)
    Pago_HR_extras_nocturnas_3h_Feriado=models.FloatField(default=0)
    HR_extras_diurnas_mixta_3h_Feriado=models.FloatField(default=0)
    Pago_HR_extras_diurnas_mixta_3h_Feriado=models.FloatField(default=0)
    HR_extras_nocturnas_mixta_3h_Feriado=models.FloatField(default=0)
    Pago_HR_extras_nocturnas_mixta_3h_Feriado=models.FloatField(default=0)
    #HORA EXTRA Dia descanso
    HR_extras_diurnas_descanso=models.FloatField(default=0)
    Pago_HR_extras_diurnas_descanso=models.FloatField(default=0)
    HR_extras_nocturnas_descanso=models.FloatField(default=0)
    Pago_HR_extras_nocturnas_descanso=models.FloatField(default=0)
    HR_extras_diurnas_mixta_descanso=models.FloatField(default=0)
    Pago_HR_extras_diurnas_mixta_descanso=models.FloatField(default=0)
    HR_extras_nocturnas_mixta_descanso=models.FloatField(default=0)
    Pago_HR_extras_nocturnas_mixta_descanso=models.FloatField(default=0)
    #+3h
    HR_extras_diurnas_3h_descanso=models.FloatField(default=0)
    Pago_HR_extras_diurnas_3h_descanso=models.FloatField(default=0)
    HR_extras_nocturnas_3h_descanso=models.FloatField(default=0)
    Pago_HR_extras_nocturnas_3h_descanso=models.FloatField(default=0)
    HR_extras_diurnas_mixta_3h_descanso=models.FloatField(default=0)
    Pago_HR_extras_diurnas_mixta_3h_descanso=models.FloatField(default=0)
    HR_extras_nocturnas_mixta_3h_descanso=models.FloatField(default=0)
    Pago_HR_extras_nocturnas_mixta_3h_descanso=models.FloatField(default=0)
    #Bonos
    Pago_Bono_con_Impuesto=models.FloatField(default=0)
    Pago_Bono_sin_Impuesto=models.FloatField(default=0)
    #deduciones
    Deduccion_con_Impuesto=models.FloatField(default=0)
    Deduccion_sin_Impuesto=models.FloatField(default=0)
    #acreedores hipotecario
    Descuento_Acreedores_Hipotecario=models.FloatField(default=0)
    Descuento_Acreedores_Empresa=models.FloatField(default=0)
    #totales a favor
    Sueldo_base_quincenal=models.FloatField(default=0)
    Pago_Total_Sobretiempo_quincenal=models.FloatField(default=0)
    Pago_dias_trabj_fer_con_descanso=models.FloatField(default=0)
    Pago_dias_traba_feriados=models.FloatField(default=0)
    Pago_dias_traba_feriados=models.FloatField(default=0)
    Pago_dias_trabaja_descanso=models.FloatField(default=0)
    Pago_Vacaciones=models.FloatField(default=0)
    Pago_Incapacidad=models.FloatField(default=0)
    Pago_Licencia_paga=models.FloatField(default=0)
    Sueldo_Bruto=models.FloatField(default=0)
    
    #
    Pago_quincena_despues_descuento=models.FloatField(default=0)
    #
    Deduccion_Seguro_Social=models.FloatField(default=0)
    Deduccion_Seguro_Educacional=models.FloatField(default=0)
    Deduccion_ISLR=models.FloatField(default=0)
    Total_deduciones_Ley=models.FloatField(default=0)
    Total_deduciones_quinceas=models.FloatField(default=0)
    # BONOS POR DEBAJO LA MESA
    Pago_total_bonos_sin_impuesto=models.FloatField(default=0)
    Pago_Sueldo_neto=models.FloatField(default=0)
    ##Patrono
    Decimo_xiii_quincena_Bruto=models.FloatField(default=0)
    Deduccion_Seg_social_decimo=models.FloatField(default=0)
    Deduccion_ISLR_Decimmo_xiii=models.FloatField(default=0)
    Decimo_xiii_quincena_Neto=models.FloatField(default=0)
    Deduccion_Seg_social_Patron=models.FloatField(default=0)
    Deduccion_Seg_social_decimo_Patron=models.FloatField(default=0)
    Deduccion_Seguro_Educacional_Patron=models.FloatField(default=0)
    Prima_Antiguedad_Patron=models.FloatField(default=0)
    Riesgo_Profesional_Patron=models.FloatField(default=0)
    Vacacionciones_Acumuladas_Patron=models.FloatField(default=0)
    #fecha pago
    Fecha_pago_quincena=models.DateField(default='2024-01-15')
    Totales_patronales=models.FloatField(default=0)
    Total_general_sueldo=models.FloatField(default=0)
    Porcentaje=models.FloatField(default=0)
    #vacaciones
    Vacaciones_Seguro_Social=models.FloatField(default=0)
    Vacaciones_Seguro_educacion=models.FloatField(default=0)
    Vacaciones_ISLR=models.FloatField(default=0)
    Deducion_Vacaciones_Totales=models.FloatField(default=0)
    Pago_Vacaciones_Neto=models.FloatField(default=0)
    Vacaciones_Seguro_Social_patron=models.FloatField(default=0)
    Vacaciones_Seguro_educacion_patron=models.FloatField(default=0)
    Deducion_Vacaciones_Totales_patron=models.FloatField(default=0)
    #XIII de pago 
    Pago_XIII_periodo_Bruto=models.FloatField(default=0)
    Pago_XIII_periodo_Seguro_Social=models.FloatField(default=0)
    
    Pago_XIII_periodo_ISLR=models.FloatField(default=0)
    

    Pago_XIII_periodo_Neto=models.FloatField(default=0)
    Deduccion_XIII_periodo_Seguro_social_patron=models.FloatField(default=0)
 

class Archivo_TXT(models.Model):
   Periodo=models.CharField(max_length=255)
   Nombre = models.CharField(max_length=255)
   Archivo = models.FileField(upload_to='NOMINA_TXT/')

class Liquidaciones(models.Model):
    Periodo=models.CharField(max_length=15, help_text="QUE QUATER ESTA", default='Q1-02-2020')
    Fecha_pago_liquidacion=models.DateField(default='2024-01-15')
    Anos_Laborado=models.FloatField(default=0)
    Meses_Laborados=models.FloatField(default=0)
    Dias_Laborados=models.FloatField(default=0)
    Mes_Diferencia_XIII=models.FloatField(default=0)
    Dias_Diferencia_XIII=models.FloatField(default=0)

    Colaborador= models.ForeignKey(Colaboradores,
                                  on_delete=models.PROTECT)
    Tipo_de_Liquidacion=models.CharField(max_length=40, help_text="Tipo de Liquidacion", default='Renuncia Voluntaria')
    Salario_Mayor=models.FloatField(default=0)
    Salario_Ultimos_30_Dias=models.FloatField(default=0)
    Salario_Ultimos_6_meses=models.FloatField(default=0)
    Salario_Ultimos_5_anios=models.FloatField(default=0)
    Dias_Vacaciones_Acumuladas=models.FloatField(default=0)
    Antiguedad_En_Anios=models.FloatField(default=0)
    Vacaciones_Provisionales_Brutas=models.FloatField(default=0)
    #Deducciones
    Seguro_Social_Provisiones_Vacas=models.FloatField(default=0)
    Seguro_Educativo_Proviciones_Vacas=models.FloatField(default=0)
    Decimo_Provisional_Bruto=models.FloatField(default=0)
    Seguro_Social_Decimo_Provisiones=models.FloatField(default=0)
    Devolucion_ISLR=models.FloatField(default=0)
    #acreedores hipotecario
   
    Descuento_Acreedores_Empresa=models.FloatField(default=0)

    Preaviso=models.FloatField(default=0)
    Prima_Antiguedad=models.FloatField(default=0)
    Indemnizacion=models.FloatField(default=0)
    Cesantía=models.FloatField(default=0)
    # Totales Colaborador
    Total_Liquidacion_Bruta=models.FloatField(default=0)
    Total_deduciones_Colaborador=models.FloatField(default=0)
    Total_Liquidacion_Neta=models.FloatField(default=0)

    #Patronales
    Seguro_Social_Provisiones_Vacas_Patron=models.FloatField(default=0)
    Seguro_Educativo_Proviciones_Vacas_Patron=models.FloatField(default=0)
    Seguro_Social_Decimo_Provisiones_Patron=models.FloatField(default=0)
    Total_Deduciones_Patronales=models.FloatField(default=0)
    Total_Gastos_Patron=models.FloatField(default=0)

    #Totales gasto para el patron

class Liquidaciones_Clientes(models.Model):
    Periodo=models.CharField(max_length=15, help_text="QUE QUATER ESTA", default='Q1-02-2020')
    Fecha_pago_liquidacion=models.DateField(default='2024-01-15')
    Anos_Laborado=models.FloatField(default=0)
    Meses_Laborados=models.FloatField(default=0)
    Dias_Laborados=models.FloatField(default=0)
    Mes_Diferencia_XIII=models.FloatField(default=0)
    Dias_Diferencia_XIII=models.FloatField(default=0)

    Colaborador= models.ForeignKey(Colaboradores,
                                  on_delete=models.PROTECT)
    Cliente= models.ForeignKey(Info_Clientes,
                                  on_delete=models.PROTECT)
    Tipo_de_Liquidacion=models.CharField(max_length=40, help_text="Tipo de Liquidacion", default='Renuncia Voluntaria')
    Salario_Mayor=models.FloatField(default=0)
    Salario_Ultimos_30_Dias=models.FloatField(default=0)
    Salario_Ultimos_6_meses=models.FloatField(default=0)
    Salario_Ultimos_5_anios=models.FloatField(default=0)
    Dias_Vacaciones_Acumuladas=models.FloatField(default=0)
    Antiguedad_En_Anios=models.FloatField(default=0)
    Vacaciones_Provisionales_Brutas=models.FloatField(default=0)
    #Deducciones
    Descuento_Acreedores_Empresa=models.FloatField(default=0)
    Seguro_Social_Provisiones_Vacas=models.FloatField(default=0)
    Seguro_Educativo_Proviciones_Vacas=models.FloatField(default=0)
    Decimo_Provisional_Bruto=models.FloatField(default=0)
    Seguro_Social_Decimo_Provisiones=models.FloatField(default=0)
    Devolucion_ISLR=models.FloatField(default=0)
    Preaviso=models.FloatField(default=0)
    Prima_Antiguedad=models.FloatField(default=0)
    Indemnizacion=models.FloatField(default=0)
    Cesantía=models.FloatField(default=0)
    # Totales Colaborador
    Total_Liquidacion_Bruta=models.FloatField(default=0)
    Total_deduciones_Colaborador=models.FloatField(default=0)
    Total_Liquidacion_Neta=models.FloatField(default=0)

    #Patronales
    Seguro_Social_Provisiones_Vacas_Patron=models.FloatField(default=0)
    Seguro_Educativo_Proviciones_Vacas_Patron=models.FloatField(default=0)
    Seguro_Social_Decimo_Provisiones_Patron=models.FloatField(default=0)
    Total_Deduciones_Patronales=models.FloatField(default=0)
    Total_Gastos_Patron=models.FloatField(default=0)

    Porcentaje=models.FloatField(default=0)

    #Totales gasto para el patron

class Archivos(models.Model):
    nombre= models.CharField(max_length=200, help_text="The name of the worker.")
    
    file = models.FileField( )

class Seguimiento_Actividad(models.Model):
    Tipo_seguimiento= models.CharField(max_length=50, help_text="tipo seguimiento.")
    SUB_Tipo_seguimiento= models.CharField(max_length=50, help_text="tipo seguimiento.")
    comentario= models.CharField(max_length=200, help_text="tipo seguimiento.")
    Fecha_novedad=models.DateField(default='2024-01-15')
    hora_novedad=models.CharField(max_length=20, help_text="tipo seguimiento.")
    Colaborador = models.ForeignKey(Colaboradores, on_delete=models.PROTECT, null=True, blank=True)

#agregar tipo de jornada semana
    #agregar dias libre de la semana


    def __str__(self):
        return (self.Colaborador_nombre+'  '+self.Colaborador_apellido)
  
class SIPE_Mensual(models.Model):
        empresa=models.CharField(max_length=60)
        ced_jur=models.CharField(max_length=30)
        year=models.IntegerField()
        mes=models.CharField(max_length=20)
        fecha_sipe=models.DateField(default='2024-01-15')
        nombre=models.CharField(max_length=40)
        apellido=models.CharField(max_length=40)
        sexo=models.CharField(max_length=15)
        tipo_docu=models.CharField(max_length=20)
        nro_identificacion=models.CharField(max_length=20)
        seguro_social=models.CharField(max_length=30)
        
        total_sueldo=models.FloatField(default=0)
        total_vacaciones=models.FloatField(default=0)
        total_xxi=models.FloatField(default=0)
        total_sueldo_ajustado=models.FloatField(default=0)
        
        total_ss=models.FloatField(default=0)
        SS_Patron=models.FloatField(default=0)
        total_se=models.FloatField(default=0)
        SE_Patron=models.FloatField(default=0)
        total_dtm=models.FloatField(default=0)
        DTM_SS_Patro=models.FloatField(default=0)
        total_islr=models.FloatField(default=0)
        total_rp=models.FloatField(default=0)
        Total_Gasto_Patron=models.FloatField(default=0)
        total_pago_Sipe=models.FloatField(default=0)
        fecha_entrada=models.CharField(max_length=60)
        fecha_salida=models.CharField(max_length=60)
        notifi_vacaciones=models.CharField(max_length=120)

class Archivos_Colaboradores(models.Model):
    Fecha_Subido=models.DateField(default='2024-01-01')
    Nombre_Archivo = models.CharField(max_length=255)
    Comentario_Archivo = models.CharField(max_length=255)
    Archivo = models.FileField()
    Empresa = models.ForeignKey(Info_Empresa, on_delete=models.PROTECT)
    Colaborador = models.ForeignKey(Colaboradores, on_delete=models.PROTECT)
    Quien_lo_subio= models.ForeignKey(UserProfile, on_delete=models.PROTECT)


'''    _
laboro_dia_domingo_descanso False
laboro_dia_feriado True'''

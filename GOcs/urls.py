from django.contrib import admin
from django.urls import path
from . import views
from django.conf import settings
from django.conf.urls.static import static

urlpatterns = [
    
    path('', views.index, name='home-page'),
    path('home-page/<str:mensuales>/<str:liquidacion>/', views.index_1, name='main'),
    path('test/', views.test, name='test'),
    path('inicio_info_empresa/', views.inicio_empresa, name='inicio-empresa/'),
    path('clientes/', views.inicio_clientes, name='clientes/'),
    path('agregar_colaborador/', views.agregar_colaborador, name='agregar-colaborador/'),
    path('previsualizar_colaborador/', views.previsualisar_colaboradores, name='previsualizar-colaborador/'),
    path('previsualizar_colaborador_1/', views.previsualisar_colaboradores_1, name='previsualizar-colaborador-1/'),
    path('ver_colaborador_Individual/<str:searched>/', views.ver_colaboradores, name='ver_colaborador_Individual/'),
    path('ver_Contrato_Trabajo/<str:searched>/', views.ver_contrato_trabajo, name='ver_carta_trabajo/'),
    path('ver_Carta_Trabajo/<str:searched>/', views.ver_carta_trabajo, name='ver_constacia_trabajo/'),
    path('ver_Archivos_Colaborador/<str:searched>/', views.ver_archivos_colaborador, name='ver_archivos_colaborador'),
    path('modificar_colaborador/<str:searched>/', views.modificar_colaboradores, name='modificar-colaborador/'),
    path('dias_feriados/', views.dias_feriados, name='dias-feriados/'),
    path('Agregar_Departamento/', views.agregar_departamento, name='Agregar_Departamento'),

    path('agregar-planificacion-colaboradores/', views.agregar_planificacion_colaboradores, name='agregar-planificacion/'),
    path('ver-planificacion/', views.ver_planificacion, name='ver_planificacion/'),
    path('agregar_jornada_individual/', views.agregar_jornada_individual, name='agregar-jornada-individual/'),
    path('agregar_jornada_masiva/', views.agregar_jornada_masiva, name='agregar-jornada-masiva'),
    path('agregar_jornada_masiva-paso1/', views.agregar_jornada_masiva_p1, name='agregar-jornada-masiva-p1'),
    path('agregar_jornada_masiva-paso2/', views.agregar_jornada_masiva_p2, name='agregar-jornada-masiva-p2'),
    path('ver_jornada/', views.ver_jornada, name='ver_jornada/'),
    path('agregar_permisos/', views.agregar_permisos, name='agregar-permisos/'),
    path('ver_permisos/', views.ver_permisos, name='ver-permisos/'),
    path('editar-permisos/<str:searched>', views.editar_permisos, name='permisos'),
    path('validar-permisos/', views.validar_permisos, name='validar-permisos'),
    path('agregar_acreedores/', views.agregar_acreedores, name='agregar-acreedores/'),
    path('ver_acreedores/', views.ver_acreedores, name='ver-acreedores/'),
    path('motor-planilla/', views.motor_planilla, name='motor-planilla/'),
    path('motor-planilla-paso1/', views.motor_planilla_p1, name='motor-planilla_p1/'),
    path('motor-planilla-paso2/', views.motor_planilla_p2, name='motor-planilla_p2/'),
    path('motor-planilla-paso3/', views.motor_planilla_p3, name='motor-planilla_p3/'),
    path('motor-planilla-paso4/', views.motor_planilla_p4, name='motor-planilla_p4/'),
    path('motor-planilla-paso5/', views.motor_planilla_p5, name='motor-planilla_p5/'),
    path('motor-planilla-paso6/', views.motor_planilla_p6, name='motor-planilla_p6/'),
    path('motor-planilla-paso7/', views.motor_planilla_p7, name='motor-planilla_p7/'),
    path('motor-planilla-paso8/', views.motor_planilla_p8, name='motor-planilla_p8/'),
    path('motor-planilla-paso9/', views.motor_planilla_p9, name='motor-planilla_p9/'),
    path('motor-planilla-paso10/', views.motor_planilla_p10, name='motor-planilla_p10/'),
    path('liquidar-Colaborador/', views.liquidar, name='liquidar/'),
    path('ver-detalles-planilla/<str:searched>/', views.ver_planilla_detalles, name='planilla-detalles/'),
    path('ver-planilla-colaborador', views.ver_planilla_trabajadores, name='planilla-colaborador/'),
    path('ver-planilla-colaborador-fechas', views.ver_planilla_trabajadores_fechas, name='planilla-colaborador-fechas/'),
    path('ver-planilla-clientes-fechas', views.ver_planilla_cliente_fechas, name='planilla-cliente-fechas/'),
    path('txt-archivo-quincena', views.txt_quincena, name='txt-quincena/'),
    path('sipe-quincena', views.sipe_quincena, name='sipe-quincena/'),
    path('reporte-colaboradores', views.reporte_quincena, name='reporte-quincena/'),
    path('reporte-liquidacion', views.reporte_liquidacion, name='reporte-liquidacion'),
    path('reporte-cliente', views.reporte_cliente, name='reporte-cliente/'),
    path('comprobantes-pagos', views.comprobantes_pagos, name='comprobantes_pagos/'),
    path('motor-planilla-paso1-l/', views.motor_planilla_p1_l, name='motor-planilla_p1-l/'),
    path('motor-planilla-paso2-l/', views.motor_planilla_p2_l, name='motor-planilla_p2-l/'),
    path('motor-planilla-paso3-l/', views.motor_planilla_p3_l, name='motor-planilla_p3-l/'),
    path('motor-planilla-paso4-l/', views.motor_planilla_p4_l, name='motor-planilla_p4-l/'),
    path('motor-planilla-paso5-l/', views.motor_planilla_p5_l, name='motor-planilla_p5-l/'),
    path('motor-planilla-paso6-l/', views.motor_planilla_p6_l, name='motor-planilla_p6-l/'),
    path('motor-planilla-paso7-l/', views.motor_planilla_p7_l, name='motor-planilla_p7-l/'),
    path('ver-detalles-liquidacion/<str:searched>/', views.ver_liquidacion_detalles, name='liquidacion-detalles/'),
    path('ver-liquidaciones-historico', views.ver_liquidaciones_historico, name='liquidaciones-historico/'),
    path('comprobante-prestaciones/<str:searched>/', views.comprobante_prestaciones, name='comprobante_prestaciones/'),
    path('Asignacion-Viaticos-Fijos/', views.Viaticos, name='Viaticos/'),
    path('Asignacion-Viaticos-Fijos-/', views.Viaticos_supervisor, name='Viaticos-supervisor/'),
    path('ver_Viaticos/', views.ver_viaticos, name='ver-viacticos/'),
    path('Analisis_Quincenas/', views.analisis_quincena, name='analisis-quincenas/'),
    path('Analisis_Cliente/<str:mensuales>/<str:cliente>/<str:buscador>', views.analisis_cliente, name='analisis-cliente'),
    path('Analisis_Colaborador/<str:mensuales>/<str:cliente>/<str:buscador>', views.analisis_colaborador, name='analisis-colaborador'),
    path('Analisis_Colaborador_Fechas/', views.analisis_fecha_colaborador, name='analisis-fechas-colaborador'),
    path('Reporte_Novedades/', views.reporte_novedades, name='reporte_novedades'),
    path('Reporte_Acreedores/', views.reporte_acreedores, name='reporte_acreedores'),
    path('Importar_SIPE_csv/', views.Importar_SIPE_csv, name='Importar_SIPE_csv'),
    path('Ver-Importar_SIPE/', views.ver_Importar_SIPE, name='ver_Importar_SIPE'),
    path('Cleaning_Go/sign-up/', views.sign_up_page, name='sign-up'),
    path('Cleaning_Go/sign-in/', views.log_in, name='sign-in'),
    path('Cleaning_Go/log-out/', views.log_out, name='log-out'),
    path('Cleaning_Go/change-password/', views.change_password, name='change-password'),
    path('Cleaning_Go/Activar_Usuarios/', views.activar_usuarios, name='activar_usuarios'),
    path('Cleaning_Go/modificar_Usuarios/', views.modificar_usuarios, name='modificar_usuarios'),
    path('Cleaning_Go/Actividad_Usuarios/', views.actividad_usuario, name='actividad-usuario'),
    path('Cleaning_Go/Pagina_no_Permitida/', views.pagina_no_permitida, name='pagina_no_permitida'),
    path('Cleaning_Go/Planilla_Cerrada/', views.pagina_planilla_cerrada, name='pagina_planilla_cerrada'),
    path('Cleaning_Go/Planilla_Creada/', views.pagina_planilla_creada, name='pagina_planilla_creada'),
    path('Cleaning_Go/crear_admin/', views.crear_admin, name='crear_admin'),
    
    
    
    

    
    ]

if settings.DEBUG:

    urlpatterns += static(settings.MEDIA_URL,document_root=settings.MEDIA_ROOT)
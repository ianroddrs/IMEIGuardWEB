# This is an auto-generated Django model module.
# You'll have to do the following manually to clean this up:
#   * Rearrange models' order
#   * Make sure each model has one field with primary_key=True
#   * Make sure each ForeignKey and OneToOneField has `on_delete` set to the desired behavior
#   * Remove `managed = False` lines if you wish to allow Django to create, modify, and delete the table
# Feel free to rename the models, but don't rename db_table values or field names.
from django.db import models


class AppCelular(models.Model):
    nro_bop = models.CharField(max_length=500, blank=True, null=True)
    data_fato = models.DateField(blank=True, null=True)
    data_registro = models.DateField(blank=True, null=True)
    registros = models.CharField(max_length=500, blank=True, null=True)
    relato = models.TextField(blank=True, null=True)
    vit_nome = models.TextField(blank=True, null=True)

    class Meta:
        managed = False
        db_table = 'app_celular'


class AuthGroup(models.Model):
    name = models.CharField(unique=True, max_length=150)

    class Meta:
        managed = False
        db_table = 'auth_group'


class AuthGroupPermissions(models.Model):
    id = models.BigAutoField(primary_key=True)
    group = models.ForeignKey(AuthGroup, models.DO_NOTHING)
    permission = models.ForeignKey('AuthPermission', models.DO_NOTHING)

    class Meta:
        managed = False
        db_table = 'auth_group_permissions'
        unique_together = (('group', 'permission'),)


class AuthPermission(models.Model):
    name = models.CharField(max_length=255)
    content_type = models.ForeignKey('DjangoContentType', models.DO_NOTHING)
    codename = models.CharField(max_length=100)

    class Meta:
        managed = False
        db_table = 'auth_permission'
        unique_together = (('content_type', 'codename'),)


class AuthUser(models.Model):
    password = models.CharField(max_length=128)
    last_login = models.DateTimeField(blank=True, null=True)
    is_superuser = models.BooleanField()
    username = models.CharField(unique=True, max_length=150)
    first_name = models.CharField(max_length=150)
    last_name = models.CharField(max_length=150)
    email = models.CharField(max_length=254)
    is_staff = models.BooleanField()
    is_active = models.BooleanField()
    date_joined = models.DateTimeField()

    class Meta:
        managed = False
        db_table = 'auth_user'


class AuthUserGroups(models.Model):
    id = models.BigAutoField(primary_key=True)
    user = models.ForeignKey(AuthUser, models.DO_NOTHING)
    group = models.ForeignKey(AuthGroup, models.DO_NOTHING)

    class Meta:
        managed = False
        db_table = 'auth_user_groups'
        unique_together = (('user', 'group'),)


class AuthUserUserPermissions(models.Model):
    id = models.BigAutoField(primary_key=True)
    user = models.ForeignKey(AuthUser, models.DO_NOTHING)
    permission = models.ForeignKey(AuthPermission, models.DO_NOTHING)

    class Meta:
        managed = False
        db_table = 'auth_user_user_permissions'
        unique_together = (('user', 'permission'),)


class Consolidados(models.Model):
    consolidado = models.TextField(blank=True, null=True)

    class Meta:
        managed = False
        db_table = 'consolidados'


class DicionarioLeitura(models.Model):
    consolidado = models.CharField(max_length=500, blank=True, null=True)
    especificacao_crime = models.CharField(max_length=500, blank=True, null=True)
    descricao = models.CharField(max_length=500, blank=True, null=True)
    exemplos = models.CharField(max_length=500, blank=True, null=True)

    class Meta:
        managed = False
        db_table = 'dicionario_leitura'


class DicionarioPenal(models.Model):
    categoria = models.CharField(max_length=500, blank=True, null=True)
    artigo = models.CharField(max_length=50, blank=True, null=True)
    termo = models.CharField(max_length=500, blank=True, null=True)
    descricao = models.CharField(max_length=500, blank=True, null=True)
    codigo = models.CharField(max_length=50)

    class Meta:
        managed = False
        db_table = 'dicionario_penal'


class DjangoAdminLog(models.Model):
    action_time = models.DateTimeField()
    object_id = models.TextField(blank=True, null=True)
    object_repr = models.CharField(max_length=200)
    action_flag = models.SmallIntegerField()
    change_message = models.TextField()
    content_type = models.ForeignKey('DjangoContentType', models.DO_NOTHING, blank=True, null=True)
    user = models.ForeignKey(AuthUser, models.DO_NOTHING)

    class Meta:
        managed = False
        db_table = 'django_admin_log'


class DjangoContentType(models.Model):
    app_label = models.CharField(max_length=100)
    model = models.CharField(max_length=100)

    class Meta:
        managed = False
        db_table = 'django_content_type'
        unique_together = (('app_label', 'model'),)


class DjangoCronCronjoblock(models.Model):
    id = models.BigAutoField(primary_key=True)
    job_name = models.CharField(unique=True, max_length=200)
    locked = models.BooleanField()

    class Meta:
        managed = False
        db_table = 'django_cron_cronjoblock'


class DjangoCronCronjoblog(models.Model):
    id = models.BigAutoField(primary_key=True)
    code = models.CharField(max_length=64)
    start_time = models.DateTimeField()
    end_time = models.DateTimeField()
    is_success = models.BooleanField()
    message = models.TextField()
    ran_at_time = models.TimeField(blank=True, null=True)

    class Meta:
        managed = False
        db_table = 'django_cron_cronjoblog'


class DjangoMigrations(models.Model):
    id = models.BigAutoField(primary_key=True)
    app = models.CharField(max_length=255)
    name = models.CharField(max_length=255)
    applied = models.DateTimeField()

    class Meta:
        managed = False
        db_table = 'django_migrations'


class DjangoSession(models.Model):
    session_key = models.CharField(primary_key=True, max_length=40)
    session_data = models.TextField()
    expire_date = models.DateTimeField()

    class Meta:
        managed = False
        db_table = 'django_session'


class Localidades(models.Model):
    risp = models.CharField(max_length=500, blank=True, null=True)
    municipios = models.CharField(max_length=500, blank=True, null=True)
    bairros = models.CharField(max_length=500, blank=True, null=True)

    class Meta:
        managed = False
        db_table = 'localidades'


class Sicadfull(models.Model):
    servidor = models.CharField(max_length=50, blank=True, null=True)
    nro_bop = models.CharField(max_length=500, blank=True, null=True)
    nro_bop_aditado = models.CharField(max_length=500, blank=True, null=True)
    nro_tombo = models.CharField(max_length=500, blank=True, null=True)
    tipo_tombo = models.CharField(max_length=500, blank=True, null=True)
    unidade_origem = models.CharField(max_length=500, blank=True, null=True)
    unidade_responsavel = models.CharField(max_length=500, blank=True, null=True)
    data_registro = models.DateField(blank=True, null=True)
    hora_registro = models.TimeField(blank=True, null=True)
    data_fato = models.DateField(blank=True, null=True)
    dia_semana = models.CharField(max_length=500, blank=True, null=True)
    hora_fato = models.TimeField(blank=True, null=True)
    fx_4_hor = models.CharField(max_length=500, blank=True, null=True)
    fx_12_hr = models.CharField(max_length=500, blank=True, null=True)
    relatorio = models.CharField(max_length=500, blank=True, null=True)
    ident_autoria = models.CharField(max_length=500, blank=True, null=True)
    qtd_autor = models.IntegerField(blank=True, null=True)
    classe_motivo = models.CharField(max_length=500, blank=True, null=True)
    mes_registro = models.CharField(max_length=500, blank=True, null=True)
    mes_fato = models.CharField(max_length=500, blank=True, null=True)
    ano_registro = models.IntegerField(blank=True, null=True)
    ano_fato = models.IntegerField(blank=True, null=True)
    registros = models.CharField(max_length=500, blank=True, null=True)
    consolidado = models.CharField(max_length=500, blank=True, null=True)
    fato_real = models.CharField(max_length=500, blank=True, null=True)
    especificacao_crime = models.CharField(max_length=500, blank=True, null=True)
    meio_emp_deac = models.CharField(max_length=500, blank=True, null=True)
    latitude = models.CharField(max_length=500, blank=True, null=True)
    longitude = models.CharField(max_length=500, blank=True, null=True)
    causa_presumivel = models.CharField(max_length=500, blank=True, null=True)
    especializacao_fato = models.CharField(max_length=500, blank=True, null=True)
    grupo_ocorrencia = models.CharField(max_length=500, blank=True, null=True)
    sub_grupo = models.CharField(max_length=500, blank=True, null=True)
    meio_empregado_sisp = models.CharField(max_length=500, blank=True, null=True)
    distrito = models.CharField(max_length=500, blank=True, null=True)
    municipios = models.CharField(max_length=500, blank=True, null=True)
    regionais = models.CharField(max_length=500, blank=True, null=True)
    bairros = models.CharField(max_length=500, blank=True, null=True)
    reg_integracao = models.CharField(max_length=500, blank=True, null=True)
    risp = models.CharField(max_length=500, blank=True, null=True)
    aisp = models.CharField(max_length=500, blank=True, null=True)
    rua_fato = models.CharField(max_length=500, blank=True, null=True)
    empresa = models.CharField(max_length=500, blank=True, null=True)
    linha = models.CharField(max_length=500, blank=True, null=True)
    tipo_transporte = models.CharField(max_length=500, blank=True, null=True)
    complemento = models.TextField(blank=True, null=True)
    local_ocorrencia = models.TextField(blank=True, null=True)
    identificacao_fato = models.TextField(blank=True, null=True)
    relator = models.TextField(blank=True, null=True)
    relato = models.TextField(blank=True, null=True)
    atuacao = models.CharField(max_length=500, blank=True, null=True)
    vit_nome = models.TextField(blank=True, null=True)
    vit_alcunha = models.CharField(max_length=500, blank=True, null=True)
    vit_dt_nasc = models.DateField(blank=True, null=True)
    vit_idade = models.IntegerField(blank=True, null=True)
    vit_fx_etaria = models.CharField(max_length=500, blank=True, null=True)
    vit_nro_doc = models.CharField(max_length=500, blank=True, null=True)
    vit_tipo_doc = models.CharField(max_length=500, blank=True, null=True)
    vit_pai = models.CharField(max_length=500, blank=True, null=True)
    vit_mae = models.CharField(max_length=500, blank=True, null=True)
    vit_tipo = models.CharField(max_length=500, blank=True, null=True)
    vit_sexo = models.CharField(max_length=100, blank=True, null=True)
    vit_cor_pele = models.CharField(max_length=500, blank=True, null=True)
    vit_grau_inst = models.CharField(max_length=500, blank=True, null=True)
    vit_profissao = models.CharField(max_length=500, blank=True, null=True)
    vit_situacao_emprego = models.CharField(max_length=500, blank=True, null=True)
    vit_estado_civil = models.CharField(max_length=500, blank=True, null=True)
    aut_nome = models.CharField(max_length=500, blank=True, null=True)
    aut_alcunha = models.CharField(max_length=500, blank=True, null=True)
    aut_data_nasc = models.DateField(blank=True, null=True)
    aut_idade = models.IntegerField(blank=True, null=True)
    aut_fx_etaria = models.CharField(max_length=500, blank=True, null=True)
    aut_nro_doc = models.CharField(max_length=500, blank=True, null=True)
    aut_tipo_doc = models.CharField(max_length=500, blank=True, null=True)
    aut_pai = models.CharField(max_length=500, blank=True, null=True)
    aut_mae = models.CharField(max_length=500, blank=True, null=True)
    aut_tipo = models.CharField(max_length=500, blank=True, null=True)
    aut_sexo = models.CharField(max_length=500, blank=True, null=True)
    grau_de_relacionamento = models.CharField(max_length=500, blank=True, null=True)
    aut_cor_pele = models.CharField(max_length=500, blank=True, null=True)
    aut_grau_inst = models.CharField(max_length=500, blank=True, null=True)
    aut_profissao = models.CharField(max_length=500, blank=True, null=True)
    aut_sit_emprego = models.CharField(max_length=500, blank=True, null=True)
    aut_est_civil = models.CharField(max_length=500, blank=True, null=True)
    meio_locomocao = models.CharField(max_length=500, blank=True, null=True)
    cor_veiculo = models.CharField(max_length=500, blank=True, null=True)
    marca_veic_fuga = models.CharField(max_length=500, blank=True, null=True)
    modelo_do_veic_fuga = models.CharField(max_length=500, blank=True, null=True)
    controle = models.CharField(max_length=500, blank=True, null=True)
    controle_ctcd = models.CharField(max_length=500, blank=True, null=True)
    flags = models.CharField(max_length=500, blank=True, null=True)
    data_upload = models.DateTimeField(blank=True, null=True)
    data_modificacao = models.DateTimeField(blank=True, null=True)
    id_servidor_sicad = models.IntegerField(blank=True, null=True)
    qtd = models.IntegerField(blank=True, null=True)
    data_leitura = models.DateField(blank=True, null=True)
    usuario_modificacao = models.CharField(max_length=200, blank=True, null=True)
    observacao = models.TextField(blank=True, null=True)
    exclusao = models.BooleanField()
    pk = models.AutoField(primary_key=True)
    acompanhar = models.BooleanField()

    class Meta:
        managed = False
        db_table = 'sicadfull'

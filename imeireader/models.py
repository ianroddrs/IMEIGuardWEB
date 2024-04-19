from django.db import models


class ApiProfile(models.Model):
    identification_number = models.CharField(max_length=15)
    user_id = models.IntegerField(unique=True)
    is_reporter = models.BooleanField()
    is_reviewer = models.BooleanField()

    class Meta:
        managed = False
        db_table = 'api_profile'


class ApiRegistroconsolidado(models.Model):
    name = models.CharField(max_length=255)
    active = models.BooleanField()

    class Meta:
        managed = False
        db_table = 'api_registroconsolidado'


class AuthGroup(models.Model):
    name = models.CharField(unique=True, max_length=150)

    class Meta:
        managed = False
        db_table = 'auth_group'


class AuthGroupPermissions(models.Model):
    group_id = models.IntegerField()
    permission_id = models.IntegerField()

    class Meta:
        managed = False
        db_table = 'auth_group_permissions'
        unique_together = (('group_id', 'permission_id'),)


class AuthPermission(models.Model):
    name = models.CharField(max_length=255)
    content_type_id = models.IntegerField()
    codename = models.CharField(max_length=100)

    class Meta:
        managed = False
        db_table = 'auth_permission'
        unique_together = (('content_type_id', 'codename'),)


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
    id = models.AutoField(primary_key=True,unique=True, db_index=True, serialize=True,null=False,blank=False)

    class Meta:
        managed = False
        db_table = 'auth_user'


class AuthUserGroups(models.Model):
    user_id = models.IntegerField()
    group_id = models.IntegerField()

    class Meta:
        managed = False
        db_table = 'auth_user_groups'
        unique_together = (('user_id', 'group_id'),)


class AuthUserUserPermissions(models.Model):
    user_id = models.IntegerField()
    permission_id = models.IntegerField()

    class Meta:
        managed = False
        db_table = 'auth_user_user_permissions'
        unique_together = (('user_id', 'permission_id'),)


class DjangoAdminLog(models.Model):
    action_time = models.DateTimeField()
    object_id = models.TextField(blank=True, null=True)
    object_repr = models.CharField(max_length=200)
    action_flag = models.SmallIntegerField()
    change_message = models.TextField()
    content_type_id = models.IntegerField(blank=True, null=True)
    user_id = models.IntegerField()

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


class DjangoMigrations(models.Model):
    app = models.CharField(max_length=255)
    name = models.CharField(max_length=255)
    applied = models.DateTimeField()

    class Meta:
        managed = False
        db_table = 'django_migrations'


class DjangoRestPasswordresetResetpasswordtoken(models.Model):
    created_at = models.DateTimeField()
    key = models.CharField(unique=True, max_length=64)
    ip_address = models.GenericIPAddressField(blank=True, null=True)
    user_agent = models.CharField(max_length=256)
    user_id = models.IntegerField()

    class Meta:
        managed = False
        db_table = 'django_rest_passwordreset_resetpasswordtoken'


class DjangoSession(models.Model):
    session_key = models.CharField(primary_key=True, max_length=40)
    session_data = models.TextField()
    expire_date = models.DateTimeField()

    class Meta:
        managed = False
        db_table = 'django_session'

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

class log_pesquisa(models.Model):
    usuario = models.ForeignKey(AuthUser,models.DO_NOTHING)
    pesquisa = models.CharField(max_length=20, blank=False, null=False)
    bop_resultado = models.CharField(max_length=20, blank=False, null=True)
    data_pesquisa = models.DateTimeField(auto_now_add=True)
    
    class Meta:
        managed = False
        db_table = 'log_pesquisa'
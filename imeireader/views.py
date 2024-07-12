from django.http import HttpResponse, JsonResponse, HttpResponseRedirect, FileResponse
from core.settings import STATICFILES_DIRS
import os
from datetime import date, timedelta
from django.shortcuts import render,redirect
from .models import log_pesquisa, AuthUser
from django.contrib.auth import logout,login, authenticate, update_session_auth_hash
from django.contrib.auth.forms import AuthenticationForm, PasswordChangeForm
from django.contrib.auth.decorators import login_required,permission_required
from django.views.decorators.csrf import csrf_exempt
from django.forms.models import model_to_dict
from .form import *
from django.contrib.auth.models import User
import pandas as pd
import datetime
from django.db.models import Q


@login_required
@permission_required('is_superuser')
def cad_user(request):
    #####################AUTOMACAO PARA CADASTRO E ENVIO DE USUARIOS #################
    if request.method == "GET":
        dados = pd.read_excel('cad_user/LOT13IMEIGUARD.xlsx')
        df = pd.DataFrame(dados)
        df = df.to_dict('records')
        for df in df:
            try:
                print(df['nome_completo'])
                # if df['nome_completo'] == 'pessoa1':
                senha = generate_secure_password()
                partes = df['nome_completo'].split()
                form_authuser = User.objects.create_user(username=df['matricula_funcional'], password=senha,first_name=partes[0],last_name=partes[-1],email=df['email'])
                form_authuser.save()
                user = AuthUser.objects.get(id=form_authuser.id)
                usuario = ModelUsuarios(authuser=user,nome_completo=df['nome_completo'],instituicao=df['instituicao'],matricula_funcional=df['matricula_funcional'],cpf=df['cpf'],cargo_funcao=df['cargo_funcao'],lotacao=df['lotacao']).save()
                email(df['email'], df['nome_completo'],df['matricula_funcional'],senha)
            except Exception as error:
                print(error)
    if request.method == "POST":
        nome = request.POST['nome_completo']
        nome = nome.upper()
        partes = nome.split()
        primeiro_nome = partes[0]
        ultimo_nome = partes[-1]
        form_authuser = User.objects.create_user(username=request.POST['matricula_funcional'], email=request.POST['email'],password=request.POST['password'],first_name=primeiro_nome,last_name=ultimo_nome)
        if form_authuser:
            form_authuser.save()
            user = AuthUser.objects.get(id=form_authuser.id)
            usuario = ModelUsuarios(authuser=user,nome_completo=nome,instituicao=request.POST['instituicao'],matricula_funcional=request.POST['matricula_funcional'],cpf=request.POST['cpf'],cargo_funcao=request.POST['cargo_funcao'],lotacao=request.POST['lotacao']).save()
            return redirect('home')
    else:
        form_user = FormUser()
    return render(request, 'cad_user.html', {'form_user':form_user})
    
    
def loginView(request):
    if request.method == 'POST':
        form = AuthenticationForm(request, data=request.POST)
        if form.is_valid():
            user = authenticate(username=form.cleaned_data.get('username'), password=form.cleaned_data.get('password')) 
            if form.cleaned_data.get('username') == "05054994000142":
                return render(request, 'login.html', {'form': form})
            if user is not None:
                if user.last_login == None:
                    login(request, user)
                    return redirect('password')
                login(request, user)
                next_url = request.POST.get('next')
                if next_url:
                    return redirect(next_url)
                return redirect(home)
    else:
        form = AuthenticationForm()
    return render(request, 'login.html', {'form': form})

@login_required
def exit(request):
    logout(request)
    return redirect(home)

@login_required
def home(request):
    return render(request, 'home.html')

def test(request):
    if request.method == 'POST':
        img = request.POST.get('device_img')
        print(img)
        log = log_pesquisa(usuario=AuthUser.objects.get(id=request.user.id),pesquisa='0000000000000',bop_resultado=None, img_aparelho=img)
        log.save()
    return render(request, 'test.html')


@csrf_exempt
def resultado(request):
    if request.method == 'POST':
        print(request.POST)
        list_bops = []
        list_recup = []
        form = AuthenticationForm(request, data=request.POST)
        if form.is_valid():
            user = authenticate(username=form.cleaned_data.get('username'), password=form.cleaned_data.get('password'))
            if user is not None:
                login(request, user)
                retorno_pm = {
                'status': 200,
                'num_token_id_requisicao':request.POST.get('num_token_id_requisicao')
                # 'num_token_id_requisicao':request.POST.get('csrfmiddlewaretoken')
                }
                user = AuthUser.objects.get(username=user)
                imei  = request.POST.get('imei')

                img = request.POST.get('device_img')

                log_pm = Log_Pm(cpf=request.POST.get('cpf'),matricula=request.POST.get('matricula'),data_requisicao=request.POST.get('data_requisicao'),lotacao=request.POST.get('lotacao'))
                log_pm.save()
                pm = Log_Pm.objects.get(id=log_pm.id)
                if imei.isdigit():
                    # if len(imei) == 15 and len(set(imei)) > 3:
                    if is_luhn_valid(imei) and len(imei) == 15:
                        consulta = Imei_Data.objects.filter(relato__icontains=f'{imei}').order_by('-data_registro')
                        if consulta.count()>0:
                            for i in consulta:
                                recuperacao = Imei_recuperacao.objects.filter(bop_delito=i.id)
                                if recuperacao:
                                    print(recuperacao[''])
                                    list_recup.append(recuperacao)
                                    print(consulta)
                                resultado_log = model_to_dict(i,fields=['nro_bop'])
                                list_bops.append(resultado_log['nro_bop'])
                            log = log_pesquisa(usuario=user,pesquisa=imei,bop_resultado=list_bops,log_pm=pm, img_aparelho=img)
                        else:
                            log = log_pesquisa(usuario=user,pesquisa=imei,bop_resultado=None,log_pm=pm, img_aparelho=img)
                        log.save()
                        consultas = []
                        for c in consulta:
                            consultas.append(model_to_dict(c))
                        consulta = consultas
                        for c in consulta:
                            c.pop('relato', None)
                        consulta = {'consulta':consulta,'retorno':retorno_pm, 'exception': None,'id_pesquisa': pm.id,'imei':imei}
                        return JsonResponse( data=consulta, safe=True)
                    else:
                        erro = 'O termo pesquisado não é um IMEI válido'
                        consulta = {'consulta':None,'retorno':retorno_pm, 'exception': erro }
                        return JsonResponse( data=consulta, safe=True)
                else:
                    erro = 'O termo pesquisado não é um IMEI'
                    consulta = {'consulta':None,'retorno':retorno_pm, 'exception': erro,'id_pesquisa': pm.id,'imei':imei}
                    return JsonResponse( data=consulta, safe=True)
    return redirect('home')


@login_required
def historico(request):
    user = AuthUser.objects.get(id=request.user.id)
    historico = log_pesquisa.objects.filter(usuario_id=user,data_pesquisa__date=date.today().strftime("%Y-%m-%d")).order_by('-data_pesquisa')
    return render(request, 'historico.html',{'historico':historico})

@login_required
def changePassword(request):
    if request.method == 'GET':
        form = PasswordChangeForm(user=request.user)
    if request.method == 'POST':
        form = PasswordChangeForm(data=request.POST, user=request.user)
        if form.is_valid():
            form.save()
            update_session_auth_hash(request,form.user)
            return redirect('home')
    return render(request, 'changepassword.html', {'form':form})

def download_apk(request):
    caminho_arquivo = os.path.join(STATICFILES_DIRS[0], 'IMEIGuard.apk')
    arquivo = open(caminho_arquivo, 'rb')
    response = FileResponse(arquivo)
    response['Content-Disposition'] = 'attachment; filename="IMEIGuard.apk"'
    return response

@login_required
def resultadoGET(request):
    if request.method == 'GET':
        try:
            list_bops = []
            list_recup = []
            user = AuthUser.objects.get(id=request.user.id)
            usuario = ModelUsuarios.objects.get(authuser=request.user.id)
            instituicao = Model_instituicao.objects.all()
            imei = request.GET.get('imei')

            if imei.isdigit() and is_luhn_valid(imei):
                consulta = Imei_Data.objects.filter(relato__icontains=f'{imei}').order_by('-data_registro')
                if consulta.count()>0:
                    for i in consulta:
                        # recuperacao = Imei_recuperacao.objects.filter(Q(imei1=imei)|Q(imei2=imei))
                        recuperacao = Imei_recuperacao.objects.filter(Q(bop_delito=i.id)&Q(Q(imei1=imei)|Q(imei2=imei)))
                        for x in recuperacao:
                            list_recup.append(x)
                        resultado_log = model_to_dict(i,fields=['nro_bop'])
                        list_bops.append(resultado_log['nro_bop'])
                    log = log_pesquisa(usuario=user,pesquisa=imei,bop_resultado=list_bops).save()
                else:
                    log = log_pesquisa(usuario=user,pesquisa=imei,bop_resultado=None).save()
            else: 
                erro = 'O termo pesquisado não é um IMEI válido'
                return render(request, 'resultado.html', {'erro': erro})
        except ValueError:
            erro = 'Ocorreu um erro desconhecido. Por favor contate a equipe de suporte'
            return render(request, 'resultado.html', {'erro': erro})
        except:
            try:
                erro = 'Ocorreu um erro desconhecido. Por favor contate a equipe de suporte'
                log = log_pesquisa(usuario=user,pesquisa=imei,bop_resultado=None)
                log.save()
            except:
                erro = 'Ocorreu um erro. Por favor verifique se o IMEI pesquisado está correto'
            return render(request, 'resultado.html', {'erro': erro})
        # print(vars(consulta[0]))
        # print(vars(list_recup[0][0]))
        return render(request, 'resultado.html', {'resultado': consulta, 'list_recuperacao':list_recup,'usuario':usuario,'instituicao':instituicao})

@login_required 
def recuperacao(request):
    user = AuthUser.objects.get(id=request.user.id)
    bop_delito = Imei_Data.objects.get(id=request.POST.get('id_bop'))
    recuperado = Imei_recuperacao.objects.filter(bop_delito=bop_delito)
    if recuperado:
        recuperado.update(
            usuario_entrega=user, 
            imei1=request.POST.get('imei1'),
            imei2=request.POST.get('imei2'),
            bop_entrega=request.POST.get('bop_entrega'),
            data_manutencao=datetime.datetime.now()
        )
        return HttpResponseRedirect(request.META.get('HTTP_REFERER'))
    instituicao = Model_instituicao.objects.get(id_instituicao=request.POST.get('instituicao'))
    recuperacao = Imei_recuperacao(
        usuario_apresentacao=user,
        usuario_entrega=user if request.POST.get('bop_entrega') else None,
        pesquisa=request.POST.get('pesquisa'),
        bop_delito=bop_delito,
        imei1=request.POST.get('imei1'),
        imei2=request.POST.get('imei2'),
        id_inst_apresentacao=instituicao.id_instituicao,
        bop_apresentacao=request.POST.get('bop_apresentacao'),
        bop_entrega=request.POST.get('bop_entrega'),data_manutencao=datetime.datetime.now())
    recuperacao.save()
    return HttpResponseRedirect(request.META.get('HTTP_REFERER'))
                

######################################################################################################
import smtplib
from email.mime.text import MIMEText
from email.mime.application import MIMEApplication
from email.mime.multipart import MIMEMultipart
from email.message import EmailMessage
def email(email, nome,usuario, senha):
    servidor_email = smtplib.SMTP('smtp.gmail.com', 587)
    servidor_email.starttls()
    servidor_email.login('coletadiariasiac@gmail.com', 'rvya ocro irit efnm')
    msg = EmailMessage()
    msg.set_content(f'''
                    Prezado(a) {nome},

                    Agradecemos seu cadastro na aplicação IMEIGuard! Abaixo estão suas informações de login:

                        Usuário: {usuario}
                        Senha: {senha}
                    
                    Por favor, mantenha essas informações em local seguro e não compartilhe com ninguém. Caso tenha alguma dúvida ou precise de assistência, não hesite em entrar em contato conosco.
                    Além disso, é altamente importante que você altere sua senha no primeiro acesso. Isso ajudará a garantir a segurança da sua conta.
                    Acesse a aplicação web através do seguinte link: https://sigop.segup.pa.gov.br/
                    
                    Download Android: https://sigop.segup.pa.gov.br/download/apk
                    
                    Atenciosamente, Equipe de Suporte do IMEIGuard''')
    
    msg['Subject'] = 'Usuário para acesso ao IMEIGuard'
    msg['From'] = 'coletadiariasiac@gmail.com'
    msg['To'] = email

    servidor_email.send_message(msg)
    servidor_email.quit()

import secrets
def generate_secure_password(length=12):
    characters = "abcdefghijklmnopqrstuvwxyz0123456789"
    password = ''.join(secrets.choice(characters) for _ in range(length))
    return password

def luhn_checksum(card_number):
    def digits_of(n):
        return [int(d) for d in str(n)]
    digits = digits_of(card_number)
    odd_digits = digits[-1::-2]
    even_digits = digits[-2::-2]
    checksum = 0
    checksum += sum(odd_digits)
    for d in even_digits:
        checksum += sum(digits_of(d*2))
    return checksum % 10

def is_luhn_valid(card_number):
    return luhn_checksum(card_number) == 0

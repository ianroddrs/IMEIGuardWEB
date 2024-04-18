import datetime
from django.shortcuts import render,redirect
from .models import AppCelular, log_pesquisa, AuthUser 
from django.contrib.auth import logout,login, authenticate
from django.contrib.auth.forms import AuthenticationForm
from django.contrib.auth.decorators import login_required
from django.forms.models import model_to_dict


def loginView(request):
    if request.method == 'POST':
        form = AuthenticationForm(request, data=request.POST)
        if form.is_valid():
            user = authenticate(username=form.cleaned_data.get('username'), password=form.cleaned_data.get('password'))
            if user is not None:
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

@login_required
def resultado(request):
    user = AuthUser.objects.get(id=request.user.id)
    list_bops = []
    try:
        imei = request.GET.get('imei')
        if imei.isdigit():
            grupo1, grupo2, grupo3, grupo4 = imei[0:6], imei[6:8], imei[8:14], imei[14]
            consulta = AppCelular.objects.filter(relato__regex=f'{grupo1}.*{grupo2}.*{grupo3}.*{grupo4}').order_by('-data_registro')
            if consulta.count()>0:
                for i in consulta:
                    resultado_log = model_to_dict(i,fields=['nro_bop'])
                    list_bops.append(resultado_log['nro_bop'])
                log = log_pesquisa(usuario=user,pesquisa=imei,bop_resultado=list_bops)
                print(datetime.datetime.now())
            else:
                log = log_pesquisa(usuario=user,pesquisa=imei,bop_resultado= None)
            log.save()
        else:
            erro = 'O termo pesquisado não é um IMEI'
            return render(request, 'resultado.html', {'erro': erro})
    except ValueError:
        erro = 'Ocorreu um erro desconhecido. Por favor contate a equipe de suporte'
        return render(request, 'resultado.html', {'erro': erro})
    except:
        erro = 'Ocorreu um erro desconhecido. Por favor contate a equipe de suporte'
        log = log_pesquisa(usuario=user,pesquisa=imei,bop_resultado= None)
        log.save()
        return render(request, 'resultado.html', {'erro': erro})
    return render(request, 'resultado.html', {'resultado': consulta})


@login_required
def historico(request):
    user = AuthUser.objects.get(id=request.user.id)
    historico = log_pesquisa.objects.filter(usuario_id=user,data_pesquisa__lte=datetime.datetime.today()).order_by('-data_pesquisa')
    print(historico)
    return render(request, 'historico.html',{'historico':historico})
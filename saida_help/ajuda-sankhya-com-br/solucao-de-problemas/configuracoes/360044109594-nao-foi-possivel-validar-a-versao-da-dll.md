---
id: "360044109594"
titulo: "Não foi possível validar a versão da dll sqlora8. A seguinte pasta não foi encontrada: C:\\Program Files\\Borland\\Borland Shared\\BDE;\\ "
url: "https://ajuda.sankhya.com.br/hc/pt-br/articles/360044109594-N%C3%A3o-foi-poss%C3%ADvel-validar-a-vers%C3%A3o-da-dll-sqlora8-A-seguinte-pasta-n%C3%A3o-foi-encontrada-C-Program-Files-Borland-Borland-Shared-BDE"
trilha: "Solução de Problemas > Configurações"
atualizado_em: "2026-07-22T15:54:50Z"
rotulos: ["#criadoRoger", "#revisadohugo", "Configuração", "Erro ao Validar Versão da DLL sqlora8", "Erro", "BDE", "DLL", "Regedit"]
---

# Não foi possível validar a versão da dll sqlora8. A seguinte pasta não foi encontrada: C:\Program Files\Borland\Borland Shared\BDE;\ 

**![Imagem 1: MENSAGEM :](https://ajuda.sankhya.com.br/hc/article_attachments/18613025282839) MENSAGEM**:

Não foi possível validar a versão da dll sqlora8. A seguinte pasta não foi encontrada: C:\Program Files\Borland\Borland Shared\BDE;\

**![Imagem 2: CAUSA :](https://ajuda.sankhya.com.br/hc/article_attachments/18613025287063) CAUSA**:

Ocorre quando ao final do diretório de instalação do BDE, existe o carácter ;(ponto-e-virgula), se faz necessário retirar através do Regedit.

**![Imagem 3: SOLUÇÃO :](https://ajuda.sankhya.com.br/hc/article_attachments/18613000478103) SOLUÇÃO**:

![Imagem 4: Acesse o Editor de Registro do Windows, digite 'Regedit' na barra de pesquisa.](https://ajuda.sankhya.com.br/hc/article_attachments/18613025293847) Acesse o Editor de Registro do Windows, digite 'Regedit' na barra de pesquisa.

![Imagem 5: Acesse o Editor de Registro do Windows, digite 'Regedit' na barra de pesquisa.](https://ajuda.sankhya.com.br/hc/article_attachments/360063059033)

![Imagem 6: Acesse o caminho: \HKEY_LOCAL_MACHINE\SOFTWARE\WOW6432Node\Borland\Database Engine Nome do Valor: DLLPATH Dados do…](https://ajuda.sankhya.com.br/hc/article_attachments/18613025299479) Acesse o caminho:
\HKEY\_LOCAL\_MACHINE\SOFTWARE\WOW6432Node\Borland\Database Engine

Nome do Valor: **DLLPATH**
Dados do Valor:  **DE**: C:\Program Files\Borland\Borland Shared\BDE;\
**Para:** C:\Program Files\Borland\Borland Shared\BDE\

Ou seja retire o caracter ; (ponto-e-virgula).

[GIF animado: Imagem 7: -Caso o caminho seja outro e mesmo assim ao final tenha o carácter ';' faça o procedimento retirando o carácter apenas.](https://ajuda.sankhya.com.br/hc/article_attachments/360063059053)

-Caso o caminho seja outro e mesmo assim ao final tenha o carácter ';' faça o procedimento retirando o carácter apenas.

-Este processo deve ser feito em cada Computador, que ocorrer o incidente

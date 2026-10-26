---
id: "43549209455639"
titulo: "Erro de comunicação do TEF (Sitef, Auttar, Pay&Go) com navegadores Chrome, Firefox e Edge"
url: "https://ajuda.sankhya.com.br/hc/pt-br/articles/43549209455639-Erro-de-comunica%C3%A7%C3%A3o-do-TEF-Sitef-Auttar-Pay-Go-com-navegadores-Chrome-Firefox-e-Edge"
trilha: "Solução de Problemas > Varejo"
atualizado_em: "2026-09-30T15:59:11Z"
rotulos: ["Artigo criado KCS", "Varejo - KCS"]
---

# Erro de comunicação do TEF (Sitef, Auttar, Pay&Go) com navegadores Chrome, Firefox e Edge

**Situação**

O erro ocorre quando o usuário tenta realizar operações de TEF ou impressões via WebConnection utilizando navegadores modernos (como Google Chrome, Mozilla Firefox ou Microsoft Edge). Mesmo após instalar e configurar o componente, o sistema não o reconhece, impossibilitando a comunicação com o pinpad/TEF e a seleção de impressoras ou dispositivos.

**Solução**

**(1)**  Verifique se o seu ambiente Sankhya está acessível via "HTTPS". Caso ainda utilize "HTTP", solicite imediatamente à sua equipe de TI ou ao datacenter a migração do ambiente, pois esta é uma exigência de segurança dos navegadores.

**(2)**  Após a migração para HTTPS, acesse o sistema Sankhya pelo navegador desejado e realize novamente a configuração automática do componente.

**Artigo de apoio:** [WebConnection não encontrado](https://ajuda.sankhya.com.br/hc/pt-br/articles/36452312790423-Web-Connection-n%C3%A3o-encontrado-Erro-em-impress%C3%B5es-ou-no-login-de-usu%C3%A1rio-com-acesso-apenas-por-computadores-liberados)

**(3)** Certifique-se de que o WebConnection está devidamente instalado e atualizado no computador do caixa. As versões mais recentes estão disponíveis em: <https://downloads.sankhya.com.br>

Verifique se o ícone do WebConnection está ativo na barra de tarefas do Windows (área de ícones ocultos, próximo ao relógio).

**(4)** No Sankhya Om, acesse a tela **Configuração TEF** (Configurações » Cadastros » Configuração TEF). Confira se o parâmetro **TEFGATEWAY** está preenchido corretamente com o TEF utilizado pela empresa (ex: SiTef).

**Causa**

A causa principal do erro é que os navegadores modernos (Chrome, Firefox, Edge) passaram a bloquear, por padrão, a comunicação entre páginas web e aplicações externas quando o ambiente não utiliza um certificado de segurança válido (**"HTTPS"**). Ambientes configurados apenas com **"HTTP"** são considerados inseguros, impedindo a integração do sistema Sankhya com o **"WebConnection"** e, consequentemente, com o TEF (Sitef) e impressoras. A solução definitiva é a migração do ambiente para **"HTTPS"**, garantindo a conformidade com os padrões de segurança exigidos pelos navegadores atuais.

---
id: "360044348913"
titulo: "A licença de uso do sistema não pôde ser validada por falha na conexão com o serviço de validação"
url: "https://ajuda.sankhya.com.br/hc/pt-br/articles/360044348913-A-licen%C3%A7a-de-uso-do-sistema-n%C3%A3o-p%C3%B4de-ser-validada-por-falha-na-conex%C3%A3o-com-o-servi%C3%A7o-de-valida%C3%A7%C3%A3o"
trilha: "Solução de Problemas > Acessos/Banco de Dados"
atualizado_em: "2026-08-21T16:07:53Z"
rotulos: ["Configuração", "Segurança", "Licença Conexão Validação", "Erro", "Artigo atualizado KCS", "Plataforma - KCS", "SAS", "Conectividade"]
---

# A licença de uso do sistema não pôde ser validada por falha na conexão com o serviço de validação

**Mensagem**

LU0104: A licença de uso do sistema não pôde ser validada por falha na conexão com o serviço de validação.
Comunique o administrador do sistema para que seja verificada a conexão do servidor (SAS) com a internet e possíveis bloqueios nos endereços de acesso. Permanecendo a falha na conexão, algumas telas e recursos do sistema poderão ficar indisponíveis após o período de tolerância.

**Situação**

Ao tentar acessar o sistema ERP Sankhya, o usuário se depara com a mensagem de erro **"LU0104"**, que impede a validação da licença de uso. Esta situação pode ocorrer durante a tentativa de login ou ao executar operações que necessitam de validação de licença, como **"emissão de notas fiscais"** ou **"envios ao e-Social"**.

**Solução**

Para resolver o erro **"LU0104"**, siga as orientações abaixo:

**(1)** Valide as configurações de **"Firewall e Proxy"** do servidor:

- Certifique-se de que há conectividade com a internet no servidor;
- Verifique as regras de saída de rede;
- Confirme se o endereço do **"serviço SAS"** está liberado: https://grupo.sankhya.com.br;
- Certifique-se de que a **"porta 443"** (HTTPS) esteja desbloqueada;
- Certifique-se de que a **"porta 10050"** esteja liberada no Firewall/Proxy;
- Caso necessário, crie uma regra específica permitindo essa comunicação.

**(2)** Após ajustar as liberações de rede, force a recarga da licença:

- Acesse a tela **"Administração do Servidor"** (Configurações >> Avançado >> Administração do Servidor), aba **"Licença"**, e clique em **"Recarregar licença"**. Em seguida, saia do sistema e realize um novo acesso.
- Para clientes que utilizam o sistema MGE ou G1, acesse o executável **"MGEConfiguração"** ou **"JivaConf"** (INSERIR CAMINHO DA TELA): **"Utilitários >> Configurações do Servidor de acessos >> Recarregar Licença"**.

**(3)** Aguarde alguns minutos e tente novamente acessar o sistema, pois pode se tratar de uma instabilidade temporária no serviço de validação.

**(4)** Se o erro persistir, entre em contato com a equipe de TI da sua empresa para validar as configurações de rede e segurança conforme as orientações acima.

**Causa**

O erro **"LU0104"** ocorre quando o sistema não consegue estabelecer comunicação com o **"serviço de validação de licenças"** (SankhyaHub/JivaHub). As principais causas incluem:

- **Problemas de conectividade:** Instabilidade na conexão de internet do servidor ou falhas momentâneas na rede local;
- **Bloqueios de segurança:** Configurações de firewall ou proxy impedindo a comunicação com o serviço SAS;
- **Camadas de segurança:** Políticas de segurança da rede corporativa bloqueando o acesso aos servidores de validação;
- **Instabilidade temporária:** Falhas momentâneas no serviço de validação que normalmente são restabelecidas automaticamente.

**Observação:**

Este erro é diferente de problemas relacionados a **"pendências financeiras"** (LU0101) ou **"falta de licenças disponíveis"**. O **"LU0104"** está especificamente relacionado a falhas de comunicação com o serviço de validação. Estas configurações de rede devem ser sempre ajustadas com o apoio do TI da empresa.

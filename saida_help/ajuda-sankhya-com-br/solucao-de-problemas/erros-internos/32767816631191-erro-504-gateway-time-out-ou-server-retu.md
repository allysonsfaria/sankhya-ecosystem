---
id: "32767816631191"
titulo: "Erro \"504 Gateway Time-out\" ou \"Server returned HTTP response code: 403 \" – Causas, Diagnóstico e Soluções"
url: "https://ajuda.sankhya.com.br/hc/pt-br/articles/32767816631191-Erro-504-Gateway-Time-out-ou-Server-returned-HTTP-response-code-403-Causas-Diagn%C3%B3stico-e-Solu%C3%A7%C3%B5es"
trilha: "Solução de Problemas > Erros Internos"
atualizado_em: "2026-07-22T14:30:26Z"
rotulos: ["Configuração", "Relatórios", "Segurança", "Financeiro", "erro \"504 Gateway Time-out", "gateway", "proxy reverso", "firewall", "Server returned HTTP response code: 403", "timeout na comunicação entre servidores", "load balancer", "Erro"]
---

# Erro "504 Gateway Time-out" ou "Server returned HTTP response code: 403 " – Causas, Diagnóstico e Soluções

**MENSAGEM:**

Erro "504 Gateway Time-out" ou "Server returned HTTP response code: 403 "

**SITUAÇÃO:**

O erro **"504 Gateway Time-out"** e o **"Server returned HTTP response code: 403 "** podem surgir durante a execução de ações no sistema e está geralmente relacionado a um **timeout na comunicação entre servidores**, causado por um componente intermediário que atua como **gateway**. Esse gateway pode ser um **proxy reverso**, um **load balancer** ou até mesmo um **firewall** com políticas de tempo limite configuradas.

Diferente dos erros internos do sistema, o 504 e o 403 não são causados diretamente pelo Sankhya, mas por esse elemento intermediário da infraestrutura que não recebe uma resposta a tempo e, por isso, encerra a requisição.

#### O que é um Gateway?

Um gateway, **no contexto deste artigo**, é qualquer componente da infraestrutura de rede que fique **entre o navegador do usuário e o sistema Sankhya**. Ele é responsável por encaminhar, distribuir ou controlar as requisições feitas pelos usuários até que elas cheguem ao sistema de aplicação.

Os exemplos mais comuns de gateway são:

- **Proxy Reverso**: como Nginx ou Apache, que recebe as requisições do navegador e as repassa ao servidor do Sankhya (Wildfly), devolvendo a resposta ao usuário.
- **Load Balancer**: distribui requisições entre vários servidores para balancear a carga e melhorar o desempenho. Pode ter regras de timeout configuradas para impedir sobrecarga.
- **Firewall com políticas de timeout**: dispositivos de segurança que podem bloquear ou encerrar conexões se elas ultrapassarem um tempo limite pré-definido.

Todos esses componentes podem retornar um erro 504 caso **não recebam uma resposta do servidor de origem (Sankhya/Wildfly) dentro do tempo esperado**.

#### O que é o erro “504 Gateway Time-out” ou "Server returned HTTP response code: 403"?

O erro **504 Gateway Time-out** ou o **Server returned HTTP response code: 403** significa que o **gateway não recebeu uma resposta a tempo** do servidor de origem (neste caso, o servidor onde o Sankhya está rodando). Esse comportamento pode ocorrer em cenários onde:

- A ação executada no sistema está demorando além do tempo limite configurado no gateway;
- O servidor Sankhya está sobrecarregado e demora a responder;
- Há uma falha temporária de comunicação entre os componentes da rede.

**Importante**: Esse erro **não é gerado pelo Sankhya**, e sim pelo gateway que intermediou a requisição. Ele apenas informa que a comunicação entre os servidores expirou antes da conclusão da resposta.

**SOLUÇÃO:**

(1)**  Identifique se há um proxy reverso**

Verifique se o acesso ao sistema é feito por um **domínio público** (como por exemplo www.cliente-snk.com.br/mge) ou diretamente por um IP interno. Se for por domínio, é provável que exista um proxy reverso configurado.

Se não for o caso, revise também as configurações de Timeout do **Load Balance**r e/ou regras de **Firewall**.

Nesses casos, é essencial identificar quem é o responsável pela infraestrutura da empresa:

- **Servidor local**: contate o responsável pela área de redes/infraestrutura da empresa;
- **Servidor em nuvem**: registre um chamado com a empresa responsável pela hospedagem;
- **Servidor hospedado pela Sankhya**: abra um chamado junto ao **Service Desk**.

**Importante**: Caso não tenha informações claras ou um responsável direto, solicite apoio da **unidade responsável** para que ela analise o ambiente de infraestrutura.

(2)** Avalie se a rotina realmente deve demorar tanto tempo**

Antes de considerar o aumento do tempo limite no gateway, é importante revisar se a ação realizada dentro do Sankhya está demorando mais do que o normal.

**Exemplo:** se a geração de um relatório ou execução de uma rotina demora vários minutos, talvez seja necessário otimizar essa rotina, em vez de apenas estender o timeout.

(3)** Mesmo após ajustes no gateway, o erro persiste?**

Se a configuração do gateway foi ajustada e a rotina foi validada, mas o erro 504 continua ocorrendo, é necessário um diagnóstico mais aprofundado.

Neste caso, **abra um ticket junto ao Service Desk** para que nossa equipe técnica possa investigar se há algum fator no sistema que contribua para essa lentidão.

**CAUSA:**

Os erros citados ocorrem quando um **gateway (proxy reverso, load balancer ou firewall)** não recebe uma resposta a tempo do servidor Sankhya e, por isso, encerra a requisição.

Esse problema não está relacionado diretamente ao sistema, mas sim à **infraestrutura de rede ou hospedagem**. Por isso, é fundamental que acione os **responsáveis técnicos da infraestrutura ou rede**, para analisar os componentes intermediários e ajustar corretamente os tempos de timeout, se necessário.

---
id: "42429727729303"
titulo: "Configurações voz"
url: "https://ajuda.sankhya.com.br/hc/pt-br/articles/42429727729303-Configura%C3%A7%C3%B5es-voz"
trilha: "NEPPO: Personalização de atendimento > Omnichannel"
atualizado_em: "2026-08-11T15:53:05Z"
rotulos: ["sync_hc", "neppo", "neppo_291111163", "sync_hash_3860699e0841"]
---

# Configurações voz

Este manual é um guia completo e detalhado sobre o processo de configuração inicial e estruturação do canal de **Voz** na plataforma Neppo.

O objetivo é preparar todo o ambiente necessário, desde os usuários individuais até as filas de atendimento, para que os agentes possam r**eceber e gerenciar chamadas telefônicas** de forma organizada.

## CRIAÇÃO USUÁRIO

Para realizar a criação dos usuários na plataforma, no usuário Agente ou Supervisor Agente                 informe os dados:

Selecione **Registrar ligação telefônica?**
Selecione **Atender por voz** e escolha a opção **Neppo Voz Nuvem**
A opção **Desabilitar ramal omnichannel** deverá ser selecionada apenas nos casos em que  o usuário Neppo precisar usar um ramal externo para atender na plataforma.

Informe um ramal de atendimento de 4 dígitos
 Senha do canal de atendimento
 Nome efetivo do identificador de chamadas: Nome do agente ou supervisor/agente

![Imagem 1: Informe um ramal de atendimento de 4 dígitos Senha do canal de atendimento Nome efetivo do identificador de chamadas:…](https://ajuda.sankhya.com.br/hc/article_attachments/42637345637783)

Os demais itens não precisam ser preenchidos pois não são obrigatórios.

## GRUPO DE ATENDIMENTO

Após criar os usuários na plataforma, realize a configuração dos grupos, começando com o  grupo pai:
**(REALIZE ESSA CRIAÇÃO CASO O GRUPO NEPPO VOZ NÃO ESTEJA CONFIGURADO, CASO ESTEJA CRIE O GRUPO FILHO)**

- Informe o nome do grupo Neppo Voz e vincule a operação (preferencialmente crie uma operação específica para o Voz).
- Em Canais de atendimento não clique na opção do Voz, para que não crie uma fila no Fusion(sistema específico do Voz).

- Vincule o Bot Fila em Agente de Inicialização.

- Selecione um tipo de Gestão de fila, que não influenciará na gestão das ligações em si.

- Em Configurações do Grupo clique na opção Envio Ativo de Voz.

- Informe os dados obrigatórios em Temporizadores/Inatividade

- Associe todos os agentes que atenderão o Voz no grupo principal.

## CRIAÇÃO GRUPO FILHO

### Realize a criação dos grupos filhos:

- Em Nome do Grupo informe  NV + nome do setor/área  (Ex: NV Financeiro)

- Selecione a Operação

- Em Canais de Atendimento selecione o ícone do Voz

- Vincule o Bot Fila em Agente de Inicialização.

- Selecione um tipo de Gestão de fila, que não influenciará na gestão das ligações em si.

- Em Configurações do Grupo clique na opção Envio Ativo de Voz.

- Informe os dados obrigatórios em Temporizadores/Inatividade

- Associe todos os agentes que atenderão o Voz no grupo filho.

**(Antes de realizar a associação é necessário que os agentes estejam com o ramal cadastrado, senão não é realizada a associação correta na fila do Fusion)**

Em Configurações de Voz > Informações Gerais informe o ramal com  3 dígitos, no Fusion em Dial Plan> Dial Plan Manager  busque pelo número que deseja utilizar para verificar se o mesmo não está sendo utilizado.

![Imagem 2: Em Configurações de Voz > Informações Gerais informe o ramal com 3 dígitos, no Fusion em Dial Plan> Dial Plan Manager…](https://ajuda.sankhya.com.br/hc/article_attachments/42637360124183)

Caso tenha inclua a música de espera ou deixe como Default  e em Gravar informe Sim.

![Imagem 3: Caso tenha inclua a música de espera ou deixe como Default e em Gravar informe Sim.](https://ajuda.sankhya.com.br/hc/article_attachments/42637391166231)

Em Configurações de Chamada> Estratégia de toque da fila informe como ocorrerá a distribuição dos atendimentos.

- **Agente com Menos Chamadas:** O agente que tocará é aquele que teve menos chamadas.
- **Agente com Maior Ociosidade:** O agente que tocará é aquele que ficou ocioso por mais tempo, dependendo do seu nível de categoria.
- **Tocar Todos:** Todos os agentes tocam simultaneamente.
- **Aleatório:** Os agentes tocarão aleatoriamente, sem uma ordem específica.
- **Tocar Progressivamente:** Os agentes tocarão da mesma forma que de cima para baixo e progredirão até que cada agente termine tocando.
- **Round Robin:** Tocará o próximo agente disponível na fila.
- **Sequencialmente por Ordem do Agente:** Os agentes tocarão em sequência de acordo com a categoria e a ordem das categorias.
- **De Cima para Baixo:** O agente tocará em ordem, começando pelo número um.

Preenchidos os itens obrigatórios basta **SALVAR**.

Crie um horário,e vincule aos grupos (mantenha os status desativados).

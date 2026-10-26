---
id: "38859526944151"
titulo: "Novo Campo \"Data de Desembarque Realizada\" no Portal Follow Up"
url: "https://ajuda.sankhya.com.br/hc/pt-br/articles/38859526944151-Novo-Campo-Data-de-Desembarque-Realizada-no-Portal-Follow-Up"
trilha: "Sankhya Official Pack - SOP > ImpEx"
atualizado_em: "2026-07-22T14:01:02Z"
rotulos: ["Configuração", "Relatórios", "Transporte", "Portal Follow Up", "Rastreabilidade", "Tela Follow Up", "Data de Desembarque Realizada", "Novo campo Data de Desembarque Realizada", "Fluxo logístico", "Logística"]
---

# Novo Campo "Data de Desembarque Realizada" no Portal Follow Up

#### 1. Objetivo

Este documento orienta sobre a utilização do novo campo **''Data de Desembarque Realizada''** no **Portal Follow Up**.

A implementação visa permitir o controle exato do momento em que a mercadoria foi desembarcada, garantindo maior rastreabilidade e precisão nos relatórios de prazos.

#### 2. O que há de novo?

Atendendo à necessidade de maior controle do fluxo logístico, foi incluída uma nova funcionalidade na tela **''Follow-Up''**:

- **Nome do campo:** Data de Desembarque Realizada
- **Finalidade:** Permitir o registro manual da data efetiva em que o desembarque da carga ocorreu
- **Tipo de dado:** Data (calendário)

O preenchimento desse campo é realizado **manualmente pelo usuário**.

O campo não substitui nenhuma data existente no sistema, nem complementa diretamente a **''Data Prevista de Desembarque''**, sendo uma informação adicional com finalidade específica no processo. Enquanto **a data prevista representa uma estimativa** para fins de planejamento e acompanhamento, a **data realizada reflete o momento em que o evento ocorreu** de fato.

Além disso, a ''Data de Desembarque Realizada'' não interfere em cálculos do sistema, podendo ser utilizada em relatórios ou análises conforme a necessidade.

#### 3. Como utilizar?

O campo deve ser atualizado conforme a necessidade do processo, no momento em que a informação estiver disponível. O preenchimento é de responsabilidade do usuário que está executando a etapa correspondente no sistema.

O **campo não é obrigatório para a conclusão do processo**, **exceto quando houver alguma regra específica configurada que exija seu preenchimento**. Dessa forma, sua utilização não é necessária em todos os processos, sendo aplicada conforme o fluxo operacional.

Passo a passo:

**(1)** Acesse a tela de ''Follow Up''.

**(2)** Localize o pedido ou a carga correspondente.

**(3)** Clique no campo "Data de Desembarque Realizada".

**(4)** Selecione no calendário a data em que a operação de desembarque foi concluída.

**(5)** Salve a alteração (conforme o fluxo padrão da sua tela).

#### 4. Regras e Permissões

Para garantir a segurança e o controle das informações, devem ser observadas as seguintes regras:

- O **preenchimento do campo é manual** e deve ser realizado quando a informação de desembarque estiver disponível, não sendo alimentado automaticamente pelo sistema;
- O **campo permite edições posteriores**, desde que o **perfil de usuário possua as permissões necessárias** para alteração;
- O sistema pode registrar o usuário responsável pelas alterações, desde que o controle de log/auditoria esteja habilitado. Nesses casos, é possível consultar informações como quem realizou a alteração, quando ela ocorreu e, em determinadas configurações, o valor anterior;
- A utilização dessa data para rastreabilidade e comparação entre o planejado e o realizado depende das configurações adotadas. Por padrão, ela não é considerada em cálculos ou relatórios nativos do sistema, podendo ser utilizada em análises específicas conforme necessidade.

#### 5. Benefícios para a Operação

- ##### Controle Logístico: Fim da dependência de anotações externas (planilhas ou e-mails) para saber quando a carga chegou;
- ##### Fidelidade nos Relatórios: Maior clareza na análise de "gargalos" entre a chegada e a entrada da mercadoria;
- ##### Conferência Facilitada: Agilidade em auditorias e conferências de prazos com transportadoras e portos/aeroportos.

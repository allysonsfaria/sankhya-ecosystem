---
id: "37961432216855"
titulo: "Reprocessamento da Nota Fiscal de Serviço"
url: "https://ajuda.sankhya.com.br/hc/pt-br/articles/37961432216855-Reprocessamento-da-Nota-Fiscal-de-Servi%C3%A7o"
trilha: "Universidade Sankhya > Jornada Sankhya Tax"
atualizado_em: "2026-07-22T14:03:31Z"
rotulos: ["Configuração", "Parceiro", "Centro de Resultado", "TOP", "Financeiro", "NFS-e"]
---

# Reprocessamento da Nota Fiscal de Serviço

## Reprocessamento de NFSe capturadas

#### O que é o reprocessamento da NFSe e qual a importância dessa funcionalidade?

O reprocessamento da NFSe é o recurso que permite revisar e reenviar uma nota já integrada no Sankhya TAX. Ele é utilizado quando o documento entrou no sistema, mas foi identificado que os dados precisam ser corrigidos ou complementados para garantir consistência nos controles financeiros, contábeis ou gerenciais. Sua importância está em evitar que informações incorretas permaneçam registradas, assegurando a confiabilidade dos relatórios e a aderência às regras fiscais.

#### Quais problemas essa funcionalidade resolve?

- Correções em notas que foram integradas com dados incompletos.
- Ajustes de campos vinculados de forma incorreta (como TOP, Parceiro ou Serviço).
- Atualização de classificações fiscais ou contábeis que impactam relatórios.
- Regularização de documentos que poderiam distorcer custos, centros de resultado ou natureza de despesa.
- Redução de retrabalho e inconsistências causadas por alterações manuais em lançamentos posteriores.

#### Quais os riscos de não utilizar?

Sem o reprocessamento, os erros de integração permanecem refletidos nos controles da empresa, gerando relatórios inconsistentes, falhas em análises de custos e até riscos de não conformidade fiscal. Como a nota já está integrada, qualquer distorção tende a se propagar para rotinas financeiras e contábeis, exigindo correções manuais mais complexas. A ausência desse recurso compromete a agilidade e a segurança da gestão, além de aumentar a probabilidade de retrabalho em auditorias ou fechamentos.

#### Cenário de aplicação

A **Axis LTDA.** recebeu uma NFSe de um prestador de serviços de manutenção que foi capturada automaticamente pelo Sankhya TAX. A nota foi integrada, mas o analista percebeu que ela entrou vinculada à **TOP errada** e sem o **Centro de Resultado** definido, o que impactaria diretamente os relatórios de custos e o fechamento contábil.

Para corrigir a situação sem gerar lançamentos manuais ou distorcer informações financeiras, o analista executa o Reprocessamento de NFSe. Ele libera a nota já integrada, ajusta os campos incorretos e valida novamente o documento, garantindo que a nota seja reprocessada e integrada corretamente às rotinas financeiras e contábeis.

**Tarefa:** Assista ao vídeo de demonstração prática e, em sua base de testes, libere uma NFSe já integrada para reprocessamento. Ajuste campos como operação, negociação, fornecedor ou serviço prestado, valide o documento e confirme a integração atualizada no sistema. 

#### Demonstração prática no sistema

[Vídeo: tutorial do artigo](https://player.vimeo.com/video/1127582439)

#### É o momento de aplicar o conhecimento adquirido! Execute as movimentações no ERP Sankhya

1. **Para liberar a nota para reprocessamento**

- Acesse a tela **Captura e Importação de Nfse**
  **Menu:** Configurações » Rotinas » Captura e Importação de Nfse
- Na grade de resultados da tela Captura e Importação de Nfse, localize a coluna **Nota Integrada**.
- Clique sobre o número para ser direcionado à Central de Compras.
- No menu principal superior, acione o botão “**Remover**” representado pelo ícone de lixeira.
- Confirme que deseja excluir o documento e retorne à tela Captura e Importação de Nfse.
- Acione o botão “**Reprocessar**” para atualizar o status e integração da nota.
  Nesse momento ela sera apontada como  **Disp. para Reprocessamento**.

2. **Para reprocessar a nota**

- Na grade de notas capturadas dê um duplo clique sobre a nota liberada.
- Realize as alterações necessárias nas abas **Informações da Nota**, **Dados do fornecedor** e **Serviço Prestado**.
- Acione o botão “**Validar**” para que a nota seja reprocessada com os dados atualizados.

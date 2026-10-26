---
id: "37221775488279"
titulo: "E0068 Rejeição: Não é possível a substituição desta NFS-e pois a mesma possui registro de Evento de Solicitação de Análise Fiscal para Cancelamento de NFS-e aguardando resposta. Para mais informações, consultar a Administração Tributária Municipal do muni"
url: "https://ajuda.sankhya.com.br/hc/pt-br/articles/37221775488279-E0068-Rejei%C3%A7%C3%A3o-N%C3%A3o-%C3%A9-poss%C3%ADvel-a-substitui%C3%A7%C3%A3o-desta-NFS-e-pois-a-mesma-possui-registro-de-Evento-de-Solicita%C3%A7%C3%A3o-de-An%C3%A1lise-Fiscal-para-Cancelamento-de-NFS-e-aguardando-resposta-Para-mais-informa%C3%A7%C3%B5es-consultar-a-Administra%C3%A7%C3%A3o-Tribut%C3%A1ria-Municipal-do-muni"
trilha: "Solução de Problemas > Rejeições: NF-e / NFS-e / NFC-e - Reforma tributária "
atualizado_em: "2026-07-22T14:18:24Z"
rotulos: ["Fiscal", "Cancelamento", "Prefeituras", "NFS-e", "Erro", "Substituição de uma NFS-e", "Administração Tributária Municipal", "Processo administrativo em andamento", "Evento de solicitação de análise fiscal", "Cancelamento da nota que ainda está pendente", "Documentos Eletrônicos"]
---

# E0068 Rejeição: Não é possível a substituição desta NFS-e pois a mesma possui registro de Evento de Solicitação de Análise Fiscal para Cancelamento de NFS-e aguardando resposta. Para mais informações, consultar a Administração Tributária Municipal do muni

**MENSAGEM**

E0068 Rejeição: Não é possível a substituição desta NFS-e pois a mesma possui registro de Evento de Solicitação de Análise Fiscal para Cancelamento de NFS-e aguardando resposta. Para mais informações, consultar a Administração Tributária Municipal do município emissor da NFS-e.

**SITUAÇÃO**

Ao tentar realizar a **substituição de uma NFS-e** via webservice, o sistema retorna a rejeição E0068, informando que existe um **evento de solicitação de análise fiscal para cancelamento** da nota que ainda está pendente de resposta pela Administração Tributária Municipal.

**SOLUÇÃO**

**(1)** Aguarde o **retorno da Administração Tributária Municipal** sobre a solicitação de análise fiscal para cancelamento da NFS-e.

**(2)** Após a resposta da prefeitura, verifique se a solicitação de cancelamento foi **aprovada ou negada**:

- **Se aprovada:** a nota será cancelada e você poderá emitir uma nova NFS-e com as informações corretas, sem necessidade de substituição.
- **Se negada:** a solicitação de cancelamento será rejeitada e você poderá então realizar a substituição da NFS-e normalmente.

**(3)** Caso necessite de mais informações sobre o status da solicitação, entre em contato com o **setor de NFS-e da Prefeitura** do município emissor da nota fiscal.

**(4)** Se a solicitação de cancelamento foi realizada por engano e você deseja prosseguir com a substituição, solicite à prefeitura o **cancelamento da solicitação de análise fiscal** para liberar a substituição da NFS-e.

**CAUSA**

A rejeição ocorre porque existe um **processo administrativo em andamento** relacionado ao cancelamento da NFS-e. A Administração Tributária Municipal não permite a substituição de notas fiscais que possuem solicitações de análise fiscal pendentes, pois isso poderia gerar **conflito entre os processos** de cancelamento e substituição. É necessário aguardar a conclusão da análise fiscal antes de realizar qualquer alteração na nota.

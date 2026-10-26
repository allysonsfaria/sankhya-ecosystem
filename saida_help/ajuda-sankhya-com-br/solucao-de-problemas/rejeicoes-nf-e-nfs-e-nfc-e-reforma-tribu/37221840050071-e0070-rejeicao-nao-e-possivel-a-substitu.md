---
id: "37221840050071"
titulo: "E0070 Rejeição: Não é possível a substituição desta NFS-e pois já ocorreu uma manifestação de confirmação de serviço. Para mais informações, consultar a Administração Tributária Municipal do município emissor da NFS-e."
url: "https://ajuda.sankhya.com.br/hc/pt-br/articles/37221840050071-E0070-Rejei%C3%A7%C3%A3o-N%C3%A3o-%C3%A9-poss%C3%ADvel-a-substitui%C3%A7%C3%A3o-desta-NFS-e-pois-j%C3%A1-ocorreu-uma-manifesta%C3%A7%C3%A3o-de-confirma%C3%A7%C3%A3o-de-servi%C3%A7o-Para-mais-informa%C3%A7%C3%B5es-consultar-a-Administra%C3%A7%C3%A3o-Tribut%C3%A1ria-Municipal-do-munic%C3%ADpio-emissor-da-NFS-e"
trilha: "Solução de Problemas > Rejeições: NF-e / NFS-e / NFC-e - Reforma tributária "
atualizado_em: "2026-07-22T14:18:22Z"
rotulos: ["Fiscal", "Prefeituras", "NFS-e", "Regra de validação", "Erro", "Substituição de uma NFS-e", "Administração Tributária Municipal", "Administração Tributária Municipal do município emissor da NFS-e", "Tomador do serviço já manifestou a confirmação", "Manifestação de confirmação de serviço", "Documentos Eletrônicos"]
---

# E0070 Rejeição: Não é possível a substituição desta NFS-e pois já ocorreu uma manifestação de confirmação de serviço. Para mais informações, consultar a Administração Tributária Municipal do município emissor da NFS-e.

**MENSAGEM**

E0070 Rejeição: Não é possível a substituição desta NFS-e pois já ocorreu uma manifestação de confirmação de serviço. Para mais informações, consultar a Administração Tributária Municipal do município emissor da NFS-e.

**SITUAÇÃO**

O usuário tentou realizar a **substituição de uma NFS-e** que já possui manifestação de confirmação do serviço prestado registrada pelo tomador no sistema da prefeitura. Após a confirmação do serviço pelo tomador, a nota fiscal não pode mais ser substituída, resultando na rejeição E0070.

**SOLUÇÃO**

**(1)** Verifique no **portal da prefeitura** do município emissor se a NFS-e possui manifestação de confirmação do serviço pelo tomador.

**(2)** Caso a nota realmente possua a confirmação registrada, **não será possível realizar a substituição** da NFS-e via webservice ou pelo portal.

**(3)** Se houver necessidade de correção das informações da nota fiscal, realize o **cancelamento da NFS-e** informando um dos motivos permitidos:

- **Código 1** - Erro na emissão
- **Código 2** - Serviço não prestado
- **Código 4** - Duplicidade na nota

**(4)** Após o cancelamento, emita uma **nova NFS-e** com as informações corretas.

**(5)** Caso tenha dúvidas sobre a manifestação ou necessite de orientações específicas, **consulte a Administração Tributária Municipal** do município emissor da NFS-e para obter informações detalhadas sobre o processo.

**CAUSA**

A rejeição ocorre porque o **tomador do serviço já manifestou a confirmação** da prestação do serviço no sistema da prefeitura. Após essa manifestação, a legislação municipal impede a substituição da NFS-e para garantir a **integridade e segurança das informações fiscais** já validadas pelo tomador. Esta é uma regra de validação da Administração Tributária Municipal que visa evitar alterações em documentos fiscais já confirmados pelas partes envolvidas na transação.

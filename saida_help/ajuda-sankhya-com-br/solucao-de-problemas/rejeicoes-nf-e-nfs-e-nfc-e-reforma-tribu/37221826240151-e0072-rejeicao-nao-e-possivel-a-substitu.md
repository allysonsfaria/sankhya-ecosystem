---
id: "37221826240151"
titulo: "E0072 Rejeição: Não é possível a substituição desta NFS-e pois já ocorreu uma manifestação tácita da NFS-e. Para mais informações, consultar a Administração Tributária Municipal do município emissor da NFS-e."
url: "https://ajuda.sankhya.com.br/hc/pt-br/articles/37221826240151-E0072-Rejei%C3%A7%C3%A3o-N%C3%A3o-%C3%A9-poss%C3%ADvel-a-substitui%C3%A7%C3%A3o-desta-NFS-e-pois-j%C3%A1-ocorreu-uma-manifesta%C3%A7%C3%A3o-t%C3%A1cita-da-NFS-e-Para-mais-informa%C3%A7%C3%B5es-consultar-a-Administra%C3%A7%C3%A3o-Tribut%C3%A1ria-Municipal-do-munic%C3%ADpio-emissor-da-NFS-e"
trilha: "Solução de Problemas > Rejeições: NF-e / NFS-e / NFC-e - Reforma tributária "
atualizado_em: "2026-07-22T14:18:21Z"
rotulos: ["Prefeituras", "NFS-e", "Erro", "Administração Tributária Municipal", "Substituição de uma NFS-e via webservice", "Não pode mais ser substituída", "Manifestação tácita", "Não é possível substituir a nota fiscal", "Manifestação tácita da NFS-e.", "Documentos Eletrônicos"]
---

# E0072 Rejeição: Não é possível a substituição desta NFS-e pois já ocorreu uma manifestação tácita da NFS-e. Para mais informações, consultar a Administração Tributária Municipal do município emissor da NFS-e.

**MENSAGEM**

E0072 Rejeição: Não é possível a substituição desta NFS-e pois já ocorreu uma manifestação tácita da NFS-e. Para mais informações, consultar a Administração Tributária Municipal do município emissor da NFS-e.

**SITUAÇÃO**

Ao tentar realizar a **substituição de uma NFS-e via webservice**, o sistema retorna a rejeição E0072, informando que não é possível substituir a nota fiscal porque já ocorreu uma **manifestação tácita** por parte do tomador do serviço ou da Administração Tributária Municipal.

**SOLUÇÃO**

**(1)** Verifique junto à **Administração Tributária Municipal** do município emissor se houve alguma manifestação tácita registrada para a NFS-e que está tentando substituir.

**(2)** Caso tenha ocorrido a manifestação tácita, **não será possível realizar a substituição** da nota fiscal via webservice. Neste caso, será necessário:

- Cancelar a NFS-e original, informando um dos motivos permitidos:

**Código 1:** Erro na emissão

**Código 2:** Serviço não prestado

**Código 4:** Duplicidade na nota

- Emitir uma nova NFS-e com as informações corretas.

**(3)** Consulte a documentação específica do município para verificar as **regras e prazos** relacionados à manifestação tácita e substituição de notas fiscais de serviço.

**(4)** Caso o município não permita a substituição via webservice, acesse o **portal da Prefeitura** e verifique se é possível realizar o procedimento diretamente no sistema municipal.

**CAUSA**

A rejeição ocorre porque a **Administração Tributária Municipal** registrou uma manifestação tácita para a NFS-e que está sendo substituída. A manifestação tácita acontece quando o tomador do serviço ou a própria prefeitura aceita a nota fiscal, seja de forma expressa ou pelo decurso de prazo estabelecido pela legislação municipal. Uma vez ocorrida a manifestação tácita, **a nota não pode mais ser substituída**, apenas cancelada, conforme as regras estabelecidas pelo município emissor.

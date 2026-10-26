---
id: "37221726592663"
titulo: "E0058 Rejeição: Não poderá ocorrer a substituição de NFS-e com alteração da identificação do não emitente, conforme parametrização do município emissor da NFS-e."
url: "https://ajuda.sankhya.com.br/hc/pt-br/articles/37221726592663-E0058-Rejei%C3%A7%C3%A3o-N%C3%A3o-poder%C3%A1-ocorrer-a-substitui%C3%A7%C3%A3o-de-NFS-e-com-altera%C3%A7%C3%A3o-da-identifica%C3%A7%C3%A3o-do-n%C3%A3o-emitente-conforme-parametriza%C3%A7%C3%A3o-do-munic%C3%ADpio-emissor-da-NFS-e"
trilha: "Solução de Problemas > Rejeições: NF-e / NFS-e / NFC-e - Reforma tributária "
atualizado_em: "2026-07-22T14:18:26Z"
rotulos: ["Fiscal", "Portal de Vendas", "Prefeituras", "NFS-e", "Erro", "Identificação do tomador do serviço", "substituição de NFS-e", "Identificação do não emitente", "Parametrização do município emissor da NFS-e", "Município emissor da NFS-e", "Documentos Eletrônicos"]
---

# E0058 Rejeição: Não poderá ocorrer a substituição de NFS-e com alteração da identificação do não emitente, conforme parametrização do município emissor da NFS-e.

**MENSAGEM**

E0058 Rejeição: Não poderá ocorrer a substituição de NFS-e com alteração da identificação do não emitente, conforme parametrização do município emissor da NFS-e.

**SITUAÇÃO**

A rejeição ocorre ao realizar a substituição de uma NFS-e em que foram alterados os dados de identificação do tomador do serviço, em município que não permite esse tipo de alteração durante o processo de substituição.

**SOLUÇÃO**

**(1)** Acesse a tela **''Portal de Vendas''** (Comercial » Consulta » Portal de Vendas) e localize a nota fiscal de serviço que deseja subistituir.

**(2)** Ao preencher os dados da **nota substituta**, certifique-se de **manter exatamente as mesmas informações de identificação do tomador** que constam na nota original, incluindo:

- CPF ou CNPJ do tomador
- Razão social ou nome completo
- Endereço completo
- Demais dados cadastrais do tomador

**(3)** Realize apenas as **alterações permitidas pelo município**, que geralmente se referem a valores, descrição dos serviços, alíquotas ou outros dados que não envolvam a identificação do tomador.

**(4)** Caso seja **necessário alterar os dados do tomador**, verifique junto à prefeitura do município se existe outra forma de proceder, pois a substituição não será permitida neste cenário.

**(5)** Após confirmar que todos os dados do tomador estão **idênticos à nota original**, realize novamente o processo de substituição da NFS-e.

**CAUSA**

A rejeição ocorre porque o **município emissor da NFS-e possui parametrização específica** que impede a alteração dos dados de identificação do tomador do serviço durante o processo de substituição da nota fiscal. Esta regra visa **garantir a integridade fiscal** e evitar que substituições sejam utilizadas para modificar informações essenciais do prestador ou tomador do serviço, mantendo a **rastreabilidade e consistência** das operações fiscais registradas. A substituição de NFS-e deve ser utilizada apenas para **correção de dados secundários**, preservando a identificação das partes envolvidas na operação original.

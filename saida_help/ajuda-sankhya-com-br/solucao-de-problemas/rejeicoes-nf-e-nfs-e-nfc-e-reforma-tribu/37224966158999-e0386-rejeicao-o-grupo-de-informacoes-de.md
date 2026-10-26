---
id: "37224966158999"
titulo: "E0386 Rejeição: O grupo de informações de endereço da atividade de obra ocorrido no exterior não deve ser informado quando o município do local da prestação for informado na DPS."
url: "https://ajuda.sankhya.com.br/hc/pt-br/articles/37224966158999-E0386-Rejei%C3%A7%C3%A3o-O-grupo-de-informa%C3%A7%C3%B5es-de-endere%C3%A7o-da-atividade-de-obra-ocorrido-no-exterior-n%C3%A3o-deve-ser-informado-quando-o-munic%C3%ADpio-do-local-da-presta%C3%A7%C3%A3o-for-informado-na-DPS"
trilha: "Solução de Problemas > Rejeições: NF-e / NFS-e / NFC-e - Reforma tributária "
atualizado_em: "2026-07-22T14:16:21Z"
rotulos: ["Configuração", "Parceiro", "Cidades", "SEFAZ", "NFS-e", "Documento de Prestação de Serviços (DPS)", "Grupo de informações de endereço", "Município do local da prestação", "Endereço da atividade de obra no exterior", "Local de prestação do serviço"]
---

# E0386 Rejeição: O grupo de informações de endereço da atividade de obra ocorrido no exterior não deve ser informado quando o município do local da prestação for informado na DPS.

**MENSAGEM**

E0386 Rejeição: O grupo de informações de endereço da atividade de obra ocorrido no exterior não deve ser informado quando o município do local da prestação for informado na DPS.

**SITUAÇÃO**

O **Documento de Prestação de Serviços (DPS)** é emitido com o **município do local da prestação informado** e, ao mesmo tempo, com o **preenchimento do grupo de informações de endereço da atividade de obra no exterior**.

**SOLUÇÃO**

Para corrigir esta rejeição, siga os passos abaixo:

**(1)** Acesse a tela de **"Portal de Vendas"** (Comercial » Consulta » Portal de Vendas) e localize o documento que foi rejeitado.

- Ao selecionar e abrir o documento, o sistema direciona automaticamente para a tela **''Central de Vendas''** (Comercial » Rotinas » Central de Vendas).

**(2)** Verifique as informações de **local de prestação do serviço** e identifique qual situação se aplica ao seu caso:

- Se a prestação de serviço ocorreu **em território nacional**, mantenha o campo **"Cidade"** preenchido e **remova as informações do grupo de endereço da atividade de obra no exterior**.
- Se a prestação de serviço ocorreu **no exterior**, remova o campo "Cidade" e mantenha apenas as **informações do grupo de endereço da atividade de obra no exterior**.

**(3)** Caso a prestação seja no exterior, acesse a tela **''Empresa''** (Comercial » Preferências » Empresa).

**(4)** Na aba **''Documentos Fiscais Eletrônicos''**, sub-aba **''NFS-e''**, sub-aba **''CNAE Empresa''** verifique o campo **"Local de Tributação"** e selecione a opção **"Exterior"**.

**OBSERVAÇÃO:** Para que as opções de local de tributação sejam utilizadas, é necessário que o parâmetro **"Cidade do ISS conforme CNAE empresa? - CIDISSCNAEEMP"** esteja habilitado.

**(5)** No cadastro do **"Parceiro"** (Configurações » Cadastros » Parceiros), na aba **"Identificação"**, verifique se o campo **"Identificação de estrangeiro"** está preenchido com o número do passaporte ou outro documento legal para identificar a pessoa estrangeira.

**(6)** Confirme que o **endereço do parceiro** está configurado corretamente:

- Para operações no exterior, o campo **"Mun. domicílio fiscal"** deve estar preenchido com **"9999999"**.

**(7)**  Após realizar os ajustes necessários, **fature novamente o documento** e transmita para a Sefaz.

**OBSERVAÇÃO**: Esta configuração deve ser feita em conjunto com o responsável pelo faturamento da empresa, levando em consideração a forma com que a prefeitura trata cada CNAE para cada empresa contribuinte, conforme previsto na Lei Complementar nº 214/2025 da Reforma Tributária.

**CAUSA**

Esta rejeição é apresentada quando o sistema identifica uma **inconsistência nas informações de localização da prestação de serviço**. A Sefaz valida que, se o **município do local da prestação** está informado na DPS, significa que a prestação ocorreu em **território nacional**, e portanto, **não deve haver informações de endereço de obra no exterior**. A presença simultânea dessas duas informações conflitantes viola a regra de validação E0386, resultando na rejeição do documento.

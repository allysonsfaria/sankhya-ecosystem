---
id: "37225834374807"
titulo: "E0478 Rejeição: CNPJ do fornecedor informado na DPS é inválido"
url: "https://ajuda.sankhya.com.br/hc/pt-br/articles/37225834374807-E0478-Rejei%C3%A7%C3%A3o-CNPJ-do-fornecedor-informado-na-DPS-%C3%A9-inv%C3%A1lido"
trilha: "Solução de Problemas > Rejeições: NF-e / NFS-e / NFC-e - Reforma tributária "
atualizado_em: "2026-07-22T14:15:37Z"
rotulos: ["Fiscal", "Parceiro", "NF-e", "SEFAZ", "Erro", "Declaração de Prestação de Serviços (DPS)", "CNPJ do fornecedor", "CNPJ do fornecedor informado na DPS é inválido", "Dígito verificador (DV) inválido", "Rejeição E0478", "E0478 Rejeição"]
---

# E0478 Rejeição: CNPJ do fornecedor informado na DPS é inválido

**MENSAGEM**

E0478 Rejeição : CNPJ do fornecedor informado na DPS é inválido.

**SITUAÇÃO**

Ao emitir um **documento fiscal eletrônico** (NF-e ou NFC-e) que contenha informações da **Declaração de Prestação de Serviços (DPS)**, o sistema validou que o **CNPJ do parceiro** informado está **inválido**. A nota foi **rejeitada** com a mensagem de erro E0478, impedindo a autorização do documento.

**SOLUÇÃO**

Para corrigir a rejeição, siga o passo a passo abaixo:

**(1)** Acesse a tela **"Parceiros"** (Configurações » Cadastros » Parceiros) e localize o **cadastro do parceiro** vinculado à nota fiscal rejeitada.

**(2)** Na aba **"Identificação"**, verifique o campo **"CNPJ"** do fornecedor.

**(3)** Certifique-se de que o **CNPJ informado** atende aos seguintes critérios:

- Possui **14 dígitos numéricos**, sem pontos, traços ou espaços em branco;
- Não está preenchido com **zeros** (exemplo: 00000000000000);
- Possui **dígito verificador (DV) válido**.

**(4)** Caso o CNPJ esteja **incorreto, zerado ou com DV inválido**, consulte o **CNPJ correto** do fornecedor no site da **Receita Federal** ou no **SINTEGRA** e atualize o cadastro.

**(5)** Verifique também se a **situação cadastral** do fornecedor está **Ativa/Habilitada** junto à Receita Federal.

**(6)** Após corrigir o cadastro do fornecedor, acesse a tela [**"Central de Vendas"**](https://ajuda.sankhya.com.br/hc/pt-br/articles/360044612414-Central-de-Vendas) (Comercial » Rotinas » Central de Vendas) e localize a nota fiscal rejeitada.

**(7)** Redigite o **cabeçalho da nota** para que as informações atualizadas do parceiro sejam carregadas no documento.

**(8)** Gere um **novo lote** e transmita novamente o documento fiscal.

**CAUSA**

A rejeição ocorre quando o **CNPJ do parceiro** informado na **Declaração de Prestação de Serviços (DPS)** vinculada ao documento fiscal está **preenchido com zeros**, está **nulo** ou possui **dígito verificador (DV) inválido**. Ao validar a consistência do CNPJ durante o processamento do documento e, ao identificar irregularidades, retorna a rejeição E0478, impedindo a autorização da nota.

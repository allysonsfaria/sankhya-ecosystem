---
id: "37226987846295"
titulo: "E0675 Rejeição: Não é permitido a prestação de informações relativas aos tributos federais quando o emitente da DPS for identificado por um pessoa física (CPF)."
url: "https://ajuda.sankhya.com.br/hc/pt-br/articles/37226987846295-E0675-Rejei%C3%A7%C3%A3o-N%C3%A3o-%C3%A9-permitido-a-presta%C3%A7%C3%A3o-de-informa%C3%A7%C3%B5es-relativas-aos-tributos-federais-quando-o-emitente-da-DPS-for-identificado-por-um-pessoa-f%C3%ADsica-CPF"
trilha: "Solução de Problemas > Rejeições: NF-e / NFS-e / NFC-e - Reforma tributária "
atualizado_em: "2026-07-22T14:14:35Z"
rotulos: ["Configuração", "CNPJ", "NF-e", "SEFAZ", "Impostos", "CPF", "Alterar o cadastro para pessoa jurídica (CNPJ)", "Alíquotas de tributos federais", "ei Complementar nº 214/2025", "NF-e ou NFC-e com emitente pessoa física (CPF)", "Remover as informações de tributos federais"]
---

# E0675 Rejeição: Não é permitido a prestação de informações relativas aos tributos federais quando o emitente da DPS for identificado por um pessoa física (CPF).

**MENSAGEM**

E0675 Rejeição: Não é permitido a prestação de informações relativas aos tributos federais quando o emitente da DPS for identificado por um pessoa física (CPF).

**SITUAÇÃO**

Ao emitir uma **NF-e** ou **NFC-e** com **emitente pessoa física (CPF)**, o sistema apresenta a rejeição acima quando são informados dados relacionados aos **tributos federais** no documento fiscal.

**SOLUÇÃO**

Para resolver esta rejeição, é necessário **remover as informações de tributos federais** do documento fiscal ou **alterar o tipo de emitente** para pessoa jurídica. Siga os passos abaixo:

**(1)**  Acesse a tela [**"Empresas"**](https://ajuda.sankhya.com.br/hc/pt-br/articles/360045118293-Empresas) (Configurações » Cadastros » Empresas).

**(2)** Na aba **''Geral''**, verifique se o emitente está cadastrado como **pessoa física (CPF)**. Caso seja necessário emitir notas com informações de tributos federais, será preciso **alterar o cadastro para pessoa jurídica (CNPJ).**

**(3)** Caso o emitente precise permanecer como **pessoa física**, acesse a tela [**"Tipos de Operação - TOP"**](https://ajuda.sankhya.com.br/hc/pt-br/articles/360044603114-Tipos-de-Opera%C3%A7%C3%A3o-TOP) (Financeiro » Arquivos » Cadastros » Tipos de Operação - TOP) e revise as configurações tributárias do **TOP** utilizado na emissão do documento.

**(4)** Verifique se há **alíquotas de tributos federais** (como **PIS, COFINS, IPI**) configuradas no **TOP** ou nos produtos. Caso existam, será necessário **removê-las ou desabilitá-las** para emissões com emitente pessoa física.

**(5)** Acesse a tela **"Produtos"** (Configurações » Cadastros » Produtos » Produtos) e revise as **configurações tributárias dos produtos** incluídos no documento fiscal. Certifique-se de que não há informações de tributos federais vinculadas aos produtos quando o emitente for pessoa física.

**(6)** Após realizar os ajustes necessários, tente **emitir novamente o documento fiscal**. O sistema não deverá mais apresentar a rejeição **E0675**.

**CAUSA**

A rejeição **E0675** ocorre devido às **regras de validação da SEFAZ** estabelecidas pela **Lei Complementar nº 214/2025**, que implementa a **Reforma Tributária** no Brasil. Segundo a legislação, **pessoas físicas (CPF)** não podem prestar informações relativas aos **tributos federais** em documentos fiscais eletrônicos, como **NF-e** e **NFC-e**. Esta validação garante que apenas **pessoas jurídicas (CNPJ)** possam informar dados sobre tributos federais nos documentos fiscais, mantendo a conformidade com as normas fiscais vigentes.

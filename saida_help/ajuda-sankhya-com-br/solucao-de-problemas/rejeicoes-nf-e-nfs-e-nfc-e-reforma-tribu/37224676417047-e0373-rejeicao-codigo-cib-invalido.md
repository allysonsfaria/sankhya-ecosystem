---
id: "37224676417047"
titulo: "E0373 Rejeição: Código CIB inválido."
url: "https://ajuda.sankhya.com.br/hc/pt-br/articles/37224676417047-E0373-Rejei%C3%A7%C3%A3o-C%C3%B3digo-CIB-inv%C3%A1lido"
trilha: "Solução de Problemas > Rejeições: NF-e / NFS-e / NFC-e - Reforma tributária "
atualizado_em: "2026-07-22T14:16:26Z"
rotulos: ["Configuração", "NF-e", "SEFAZ", "Impostos", "Cadastro de Alíquotas IBS e CBS", "NF-e ou NFC-e", "Alíquotas de CBS", "Alíquotas de IBS", "Tabela oficial", "CIB inválido", "Novos tributos da Reforma Tributária", "Código de Identificação do Benefício Fiscal (CIB)"]
---

# E0373 Rejeição: Código CIB inválido.

**MENSAGEM**

E0373 Rejeição: Código CIB inválido.

**SITUAÇÃO**

A NF-e ou NFC-e foi emitida com informações dos tributos IBS e CBS, contendo um Código de Identificação do Benefício Fiscal (CIB) que não é reconhecido no layout do documento fiscal.

**SOLUÇÃO**

Para corrigir a rejeição e permitir a autorização do documento fiscal, siga os passos abaixo:

**(1)** Acesse as telas **''Alíquotas de IBS''** (Livros Fiscais » Cadastros » Aliquotas de IBS) e **''Alíquotas de CBS''** (Livros Fiscais » Cadastros » Aliquotas de CBS) e localize o **cadastro de alíquota** utilizado no documento fiscal rejeitado.

**(2)** Verifique se o campo **"Código de Identificação do Benefício Fiscal - CIB"** está preenchido corretamente:

- Confirme se o código informado corresponde a um **CIB válido e homologado** pela Sefaz;
- Consulte a **tabela oficial de códigos CIB** disponibilizada pela Receita Federal ou pelo Comitê Gestor do IBS para validar o código;
- Certifique-se de que o CIB está **vigente e aplicável** ao tipo de operação e produto da nota fiscal.

**(3)** Caso o código esteja **incorreto ou desatualizado**, corrija o campo **"Código de Identificação do Benefício Fiscal - CIB"** com o código válido correspondente ao benefício fiscal aplicável.

**(4)** Se o benefício fiscal **não se aplica** à operação, remova o código CIB do cadastro da alíquota, deixando o campo em branco.

**(5)** Retorne ao documento fiscal rejeitado e **redigite o cabeçalho** da nota para que as informações atualizadas sejam aplicadas.

**(6)** Gere um **novo lote de transmissão** e tente autorizar o documento fiscal novamente. 

**OBSERVAÇÃO:** O Código de Identificação do Benefício Fiscal (CIB) é obrigatório quando há **aplicação de benefícios fiscais** relacionados ao IBS e CBS, conforme previsto na **Lei Complementar nº 214/2025**. Certifique-se de que o código utilizado está **devidamente cadastrado e homologado** pelos órgãos competentes.

**CAUSA**

A rejeição E0373 é causada pelo **preenchimento incorreto ou ausência de validação** do campo **"Código de Identificação do Benefício Fiscal - CIB"** no cadastro de alíquotas IBS e CBS. Isso ocorre quando o código informado **não consta na tabela oficial** da Sefaz, está **desatualizado, inválido** ou foi **digitado incorretamente**, impedindo a validação do documento fiscal pela Receita Federal.

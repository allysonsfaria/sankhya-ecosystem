---
id: "37222437387927"
titulo: "E0162 Rejeição: Não é permitido ao não optante do Simples Nacional e o MEI preencherem o campo de indicação do regime de apuração dos tributos apurados"
url: "https://ajuda.sankhya.com.br/hc/pt-br/articles/37222437387927-E0162-Rejei%C3%A7%C3%A3o-N%C3%A3o-%C3%A9-permitido-ao-n%C3%A3o-optante-do-Simples-Nacional-e-o-MEI-preencherem-o-campo-de-indica%C3%A7%C3%A3o-do-regime-de-apura%C3%A7%C3%A3o-dos-tributos-apurados"
trilha: "Solução de Problemas > Rejeições: NF-e / NFS-e / NFC-e - Reforma tributária "
atualizado_em: "2026-07-22T14:17:48Z"
rotulos: ["Configuração", "Fiscal", "NF-e", "Simples Nacional", "Impostos", "Passos para resolver", "Erro", "Como Resolver", "Regime de Apuração dos Tributos do Simples Nacional", "MEI", "Regime de Apuração dos Tributos", "Não optante do Simples Nacional", "Optante pelo SIMPLES", "Código do Regime Tributário (CRT)", "Regime Tributário"]
---

# E0162 Rejeição: Não é permitido ao não optante do Simples Nacional e o MEI preencherem o campo de indicação do regime de apuração dos tributos apurados

**MENSAGEM**

E0162 Rejeição: Não é permitido ao não optante do Simples Nacional e o MEI preencherem o campo de indicação do regime de apuração dos tributos apurados

**SITUAÇÃO:**

A nota fiscal é emitida por empresa configurada como **não optante pelo Simples Nacional** ou **MEI**, contendo o campo **Regime de Apuração dos Tributos do Simples Nacional** preenchido.

**SOLUÇÃO**

Para corrigir esta rejeição, siga os passos abaixo:

##### 1. Verifique o Regime Tributário da Empresa

**(1)** Acesse a tela **''Empresas''** (Configurações » Cadastros » Empresas).

**(2)** Na aba **''Naturezas''**, verifique os seguintes campos:

- **''Optante pelo SIMPLES''**: Esta marcação deve estar desmarcada se a empresa não é optante pelo Simples Nacional.
- **''Cód. Regime Tribut''**: Deve estar configurado como Regime Normal para empresas não optantes.

##### 2. Ajuste o Campo de Partilha do Simples Nacional

**(1)** Ainda na aba "Naturezas":

- Localize o campo **''Tipo de Partilha/Anexo SN''**.
- Certifique-se de que este campo está **vazio** ou **sem preenchimento**.

**IMPORTANTE:** Se a empresa não é optante pelo Simples Nacional, **nenhum campo relacionado ao Simples deve estar preenchido**.

##### 3. Verifique as Preferências da Empresa

**(1)** Acesse a tela **''Empresa''** (Comercial » Preferências » Empresa).

**(2)** Na aba **"Documentos Fiscais Eletrônicos"**, sub-aba **"NFS-e''** sub-aba **''Geral"**:

- Verifique o campo **''Regime de Apuração dos Tributos do Simples Nacional''**.
- Este campo deve estar **vazio** ou **não preenchido** para empresas não optantes.

##### 4. Confirme com o Contador

Antes de realizar qualquer alteração, é fundamental:

Consultar o **contador da empresa**.

- Verificar no site do **SINTEGRA** qual é o regime tributário correto do CNPJ.
- Confirmar se a empresa realmente não é optante pelo Simples Nacional.

##### 5. Gere Novamente a Nota Fiscal

Após realizar os ajustes:

- Gere o lote da NF-e novamente;
- Valide no XML se as correções foram aplicadas;
- Verifique se a tag **CRT** está com o valor correto (**3 – Regime Normal**).

#### Resumo das Configurações

| Tipo de Empresa | Optante pelo SIMPLES | Cód. Regime Tribut. | Tipo de Partilha SN |
| --- | --- | --- | --- |
| Simples Nacional | Marcado | Simples Nacional | Preenchido |
| Regime Normal | Desmarcado | Regime Normal | Vazio |
| MEI | Desmarcado | Regime Normal | Vazio |

**CAUSA**

O erro ocorre devido a uma inconsistência entre:

- O **Código do Regime Tributário (CRT)** cadastrado para a empresa;
- O preenchimento do campo **Regime de Apuração dos Tributos** na emissão da nota fiscal.

Empresas com regime tributário configurado como **Regime Normal** não devem possuir informações relacionadas ao **Simples Nacional** preenchidas no documento fiscal.

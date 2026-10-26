---
id: "37099296097559"
titulo: "1073 Rejeição: Total de IS informado indevidamente [nItem: 999]"
url: "https://ajuda.sankhya.com.br/hc/pt-br/articles/37099296097559-1073-Rejei%C3%A7%C3%A3o-Total-de-IS-informado-indevidamente-nItem-999"
trilha: "Solução de Problemas > Rejeições: NF-e / NFS-e / NFC-e - Reforma tributária "
atualizado_em: "2026-07-22T14:47:30Z"
rotulos: ["Produtos", "Configuração", "NF-e", "SEFAZ", "Impostos", "Reforma Tributária", "CST (Código de Situação Tributária)", "IS informado indevidamente", "Total do Imposto Seletivo (IS)", "grupo de Imposto Seletivo (IS)"]
---

# 1073 Rejeição: Total de IS informado indevidamente [nItem: 999]

**MENSAGEM**

1073 Rejeição: Total de IS informado indevidamente [nItem: 999]

**SITUAÇÃO**

Ao tentar emitir uma Nota Fiscal Eletrônica (NF-e) ou Nota Fiscal de Consumidor Eletrônica (NFC-e), o sistema está incluindo o grupo de Imposto Seletivo (IS) indevidamente para um produto ou operação que não deveria ter esse imposto, resultando na rejeição do documento fiscal pela SEFAZ.

**SOLUÇÃO**

**(1)** Acesse a tela **“Produtos”** (Configurações » Cadastros » Produtos » Produtos) e verifique a classificação tributária configurada para o Imposto Seletivo (IS) do produto.

**(2)** Em seguida, acesse a tela [**"Tipos de Operação - TOP"**](https://ajuda.sankhya.com.br/hc/pt-br/articles/360044603114-Tipos-de-Opera%C3%A7%C3%A3o-TOP) (Comercial » Arquivo » Cadastros » Tipos de Operação - TOP) e verifique se a operação está corretamente configurada para aplicar o Imposto Seletivo.

**(3)** Na aba **"NF-e/NFC-e/CF-e"**, confirme se a configuração do Imposto Seletivo está de acordo com a classificação tributária do produto. 

**(4)** Acesse a tela [**''Assistente de Configuração Integral da Reforma Tributária''**](https://ajuda.sankhya.com.br/hc/pt-br/articles/36231337491479-Assistente-de-Configura%C3%A7%C3%A3o-da-Tributa%C3%A7%C3%A3o-integral-IBS-e-CBS-Reforma-Tribut%C3%A1ria) (Livros Fiscais » Cadastros » Assistente de Configuração Integral da Reforma Tributária) e verifique se as configurações relacionadas ao Imposto Seletivo estão corretas.

**(5)** Certifique-se de que **CST** (**Código de Situação Tributária**) do Imposto Seletivo esteja corretamente configurado para o produto e a operação correspondente.

**(6)** Por fim, confira se o **NCM do produto** está correto e se o item não está listado entre os produtos sujeitos ao Imposto Seletivo.

**(7)** Após realizar todas as correções, emita a nota fiscal novamente.

**CAUSA**

A rejeição **1073** ocorre quando o sistema informa o **Total do Imposto Seletivo (IS)** para um produto ou operação que não deveria ser tributado, de acordo com as regras de validação da SEFAZ. Segundo a **regra UB01-10**, o uso do Imposto Seletivo não é permitido para determinadas classificações tributárias (`cClassTribIS`).

Essa inconsistência pode ocorrer devido a:

- **Configuração incorreta da classificação tributária do produto**;
- **Configuração inadequada do Tipo de Operação (TOP)** em relação ao Imposto Seletivo;
- **Uso de CST do Imposto Seletivo incompatível** com a operação;
- **Produto com NCM não sujeito ao Imposto Seletivo**, mas que está sendo tributado indevidamente.

A implementação do Imposto Seletivo faz parte da **Reforma Tributária**, conforme a **Lei Complementar nº 214/2025**, e sua aplicação deve seguir estritamente as regras definidas pela legislação.

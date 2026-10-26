---
id: "37095779024151"
titulo: "1151 Rejeição: Grupo IBS/CBS Monofásico informado indevidamente [nItem: 999]"
url: "https://ajuda.sankhya.com.br/hc/pt-br/articles/37095779024151-1151-Rejei%C3%A7%C3%A3o-Grupo-IBS-CBS-Monof%C3%A1sico-informado-indevidamente-nItem-999"
trilha: "Solução de Problemas > Rejeições: NF-e / NFS-e / NFC-e - Reforma tributária "
atualizado_em: "2026-07-22T14:21:34Z"
rotulos: ["Configuração", "NF-e", "SEFAZ", "Impostos", "Erro", "Grupo IBS/CBS informado indevidamente", "IBS/CBS Monofásico", "Aliquotas Monofásicas", "Tabela de Indicadores de CST do IBS e da CBS"]
---

# 1151 Rejeição: Grupo IBS/CBS Monofásico informado indevidamente [nItem: 999]

**MENSAGEM**

1151 Rejeição: Grupo IBS/CBS Monofásico informado indevidamente [nItem: 999]

**SITUAÇÃO**

Esta rejeição ocorre quando o contribuinte tenta emitir uma NF-e ou NFC-e informando o grupo **IBS/CBS Monofásico** em um item cujo CST (Código de Situação Tributária) **não permite essa informação** (`ind_gIBSCBSMono = 0`).

Mesmo que o CST não autorize, se o grupo Monofásico for informado, o documento fiscal será rejeitado.

**SOLUÇÃO**

**(1)** Acesse a tela **''Aliquotas Monofásicas''** (Livros Fiscais » Cadastros » Aliquotas Monofásicas) e verifique o CST do item rejeitado.

**(2)** Em seguida, consulte a **“Tabela de Indicadores de CST do IBS e da CBS”**, disponibilizada no site do governo.

**(3)** Verifique se o CST utilizado permite a informação do grupo IBS/CBS Monofásico (`ind_gIBSCBSMono = 1`).

**(4)** Caso o CST não permita o uso do grupo IBS/CBS Monofásico:

- Altere o CST do IBS/CBS para um que permita a tributação monofásica, se a operação realmente exigir este regime.
- Remova as informações do grupo IBS/CBS Monofásico do item, se a operação não utilizar tributação monofásica.

**(5)** Acesse a tela [**''Tipo de Operação - TOP''**](https://ajuda.sankhya.com.br/hc/pt-br/articles/360044603114-Tipos-de-Opera%C3%A7%C3%A3o-TOP) (Comercial » Arquivo » Cadastros » Tipos de Operação - TOP) e altere o CST e selecione a operação utilizada na nota fiscal.

**(6)** Na aba **''NF-e/NFC-e/CF-e''**, localize a seção de configuração do IBS/CBS e ajuste o CST conforme necessário para a operação.

**(7)** Se for necessário remover o grupo IBS/CBS Monofásico, acesse o [**“Assistente de Configuração Integral da Reforma Tributária”**](https://ajuda.sankhya.com.br/hc/pt-br/articles/36231337491479-Assistente-de-Configura%C3%A7%C3%A3o-da-Tributa%C3%A7%C3%A3o-integral-IBS-e-CBS-Reforma-Tribut%C3%A1ria) (Livros Fiscais » Cadastros » Assistente de Configuração Integral da Reforma Tributária) e **ajuste as configurações do item** conforme necessário.

**(8)** Após realizar todas as alterações, emita novamente a nota fiscal.

**CAUSA**

A rejeição é causada pela regra de validação **UB13-39 da SEFAZ**, que verifica se o CST do IBS/CBS informado possui o indicador `ind_gIBSCBSMono = 0`. Quando este indicador é zero, o grupo **gIBSCBSMono** (id: UB84, grupo: imposto/IBSCBS/gIBSCBSMono) **não deve ser informado** no documento fiscal.

Essa validação faz parte da **Lei Complementar nº 214/2025 (Reforma Tributária)**. A tributação monofásica é um regime especial aplicável apenas a determinados produtos e operações, podendo ser usada somente quando o CST permitir expressamente.

Cada CST possui indicadores específicos que determinam quais grupos podem ser informados. Se o documento fiscal contém informações incompatíveis com o CST utilizado, a SEFAZ rejeita o envio.

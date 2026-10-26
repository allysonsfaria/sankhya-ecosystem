---
id: "37095677180183"
titulo: "1018 Rejeição: Unidade tributável (uTrib) e Quantidade tributável (qTrib) do imposto seletivo não informados [nItem: 999]"
url: "https://ajuda.sankhya.com.br/hc/pt-br/articles/37095677180183-1018-Rejei%C3%A7%C3%A3o-Unidade-tribut%C3%A1vel-uTrib-e-Quantidade-tribut%C3%A1vel-qTrib-do-imposto-seletivo-n%C3%A3o-informados-nItem-999"
trilha: "Solução de Problemas > Rejeições: NF-e / NFS-e / NFC-e - Reforma tributária "
atualizado_em: "2026-07-22T14:21:37Z"
rotulos: ["Produtos", "Configuração", "NF-e", "SEFAZ", "Impostos", "Unidades Alternativas", "Reforma Tributária", "Assistente de Configuração Integral da Reforma Tributária", "Imposto Seletivo (IS)", "Quantidade tributável (qTrib)", "Unidade tributável (uTrib)"]
---

# 1018 Rejeição: Unidade tributável (uTrib) e Quantidade tributável (qTrib) do imposto seletivo não informados [nItem: 999]

**MENSAGEM**

1018 Rejeição: Unidade tributável (uTrib) e Quantidade tributável (qTrib) do imposto seletivo não informados [nItem: 999]

**SITUAÇÃO**

A nota fiscal foi emitida com produtos sujeitos ao Imposto Seletivo, sem o preenchimento das informações de unidade tributável e quantidade tributável do imposto seletivo nos itens do documento.

**SOLUÇÃO**

Para resolver esta rejeição, siga os passos abaixo:

**(1)** Acesse o cadastro de **"Produtos"** (Configurações » Cadastros » Produtos » Produtos) e localize o produto que está gerando a rejeição.

**(2)** Na aba **''Unidades Alternativas''**, verifique se no campo **''Unidade''** há uma unidade alternativa configurada para o produto. Caso não exista, cadastre uma unidade alternativa adequada para tributação do Imposto Seletivo.

**(3)** Marque a opção **"Unidade de Tributação"** para que o sistema utilize esta unidade para gerar as tags **uTrib** e **qTrib** no XML da nota fiscal.

**(4)** Acesse a tela [**"Tipos de Operação - TOP"**](https://ajuda.sankhya.com.br/hc/pt-br/articles/360044603114-Tipos-de-Opera%C3%A7%C3%A3o-TOP) (Comercial » Arquivo » Cadastros » Tipos de Operação - TOP) e verifique se o tipo de operação utilizado está configurado corretamente para operações com Imposto Seletivo.

**(5)** Acesse a tela **''Assistente de Configuração Integral da Reforma Tributária''** (Livros Fiscais » Cadastros » Assistente de Configuração Integral da Reforma Tributária) e verifique se as configurações do Imposto Seletivo estão corretas para o produto em questão.

**(6)** Certifique-se de que o **"CSTIS"** (Código de Situação Tributária do Imposto Seletivo) informado exige o grupo do Imposto Seletivo e está corretamente configurado.

**(7)** Ao emitir a nota fiscal, verifique se os campos de **"Unidade Tributável"** e **"Quantidade Tributável"** do Imposto Seletivo estão sendo preenchidos corretamente para cada item sujeito ao IS.

 **CAUSA**

A rejeição 1018 ocorre devido à **ausência de informações obrigatórias** para o cálculo do Imposto Seletivo. Conforme a regra de validação UB08-10 da SEFAZ, quando o CSTIS (Código de Situação Tributária do Imposto Seletivo) informado exige o grupo do Imposto Seletivo (grupo: imposto/IS), é obrigatório informar a unidade tributável (tag: imposto/IS/uTrib) e a quantidade tributável (tag: imposto/IS/qTrib), não podendo estas informações estarem ausentes ou com valor zero.

Esta validação está relacionada às mudanças introduzidas pela Reforma Tributária (Lei Complementar nº 214 de 16 de janeiro de 2025), que estabelece novos requisitos para a tributação de produtos sujeitos ao Imposto Seletivo.

---
id: "37099160400791"
titulo: "1108 Rejeição: Não informada a Tributação Monofásica Retida Anteriormente [nItem: 999]"
url: "https://ajuda.sankhya.com.br/hc/pt-br/articles/37099160400791-1108-Rejei%C3%A7%C3%A3o-N%C3%A3o-informada-a-Tributa%C3%A7%C3%A3o-Monof%C3%A1sica-Retida-Anteriormente-nItem-999"
trilha: "Solução de Problemas > Rejeições: NF-e / NFS-e / NFC-e - Reforma tributária "
atualizado_em: "2026-07-22T14:19:57Z"
rotulos: ["Configuração", "NF-e", "SEFAZ", "Impostos", "Combustível", "Tributação Monofásica", "Tributação Monofásica Retida Anteriormente", "Tributação Monofásica de Combustível", "Classificação Tributária", "classificação tributária do produto", "Tributação Monofásica de Combustível cobrada anteriormente"]
---

# 1108 Rejeição: Não informada a Tributação Monofásica Retida Anteriormente [nItem: 999]

**MENSAGEM**

1108 Rejeição: Não informada a Tributação Monofásica Retida Anteriormente [nItem: 999]

**SITUAÇÃO**

O documento fiscal foi emitido com produto enquadrado em tributação monofásica de combustível com cobrança anterior, porém sem o preenchimento das informações correspondentes a esse tipo de tributação no documento.

**SOLUÇÃO**

Para resolver esta rejeição, siga os passos abaixo:

**(1)** Acesse a tela **''Assistente de Configuração Integral da Reforma Tributária''** (Livros Fiscais » Cadastros » Assistente de Configuração Integral da Reforma Tributária).

**(2)** Verifique se o produto está configurado corretamente na **"Classificação Tributária"** que exige a informação da Tributação Monofásica Retida Anteriormente.

**(3)** Acesse a tela **"Produtos"** (Configurações » Cadastros » Produtos » Produtos).

**(4)** Na aba **''Impostos''**, verifique se o campo **"Classificação Substituição Tributária"** está configurado corretamente para o produto que está sendo comercializado.

**(5)** Acesse a tela **"Tipos de Operação - TOP"** (Comercial » Arquivo » Cadastros » Tipos de Operação - TOP) e verifique na aba **"NF-e/NFC-e/CF-e"** se as configurações relacionadas à tributação monofásica estão corretas.

**(6)** Ao emitir o documento fiscal, certifique-se de que as informações sobre a Tributação Monofásica Retida Anteriormente estejam sendo informadas corretamente no grupo correspondente (ID: UB94). 

**CAUSA**

A rejeição ocorre devido à **ausência de informações obrigatórias** sobre a Tributação Monofásica Retida Anteriormente (ID: UB94) para produtos que exigem essa tributação. Conforme o artigo 180 da Lei Complementar 214/2025, quando a classificação tributária do produto possui o indicador que exige Tributação Monofásica de Combustível cobrada anteriormente (ind\_gMonoRet = 1), é obrigatório informar os dados dessa tributação no documento fiscal.

Esta validação é realizada pela Sefaz para garantir o correto recolhimento dos tributos monofásicos sobre combustíveis que já foram cobrados em etapas anteriores da cadeia de comercialização, assegurando a conformidade fiscal e evitando a bitributação.

---
id: "37099462257175"
titulo: "1093 Rejeição: Total da CBS monofásica difere da soma dos itens"
url: "https://ajuda.sankhya.com.br/hc/pt-br/articles/37099462257175-1093-Rejei%C3%A7%C3%A3o-Total-da-CBS-monof%C3%A1sica-difere-da-soma-dos-itens"
trilha: "Solução de Problemas > Rejeições: NF-e / NFS-e / NFC-e - Reforma tributária "
atualizado_em: "2026-07-22T14:19:45Z"
rotulos: ["Configuração", "NF-e", "SEFAZ", "Impostos", "TOP", "Passos para resolver", "Erro", "Como Resolver", "Alíquotas de CBS", "Valor total da CBS monofásica", "soma dos itens", "Total da CBS monofásica", "valores da CBS monofásica"]
---

# 1093 Rejeição: Total da CBS monofásica difere da soma dos itens

**MENSAGEM**

1093 Rejeição: Total da CBS monofásica difere da soma dos itens

**SITUAÇÃO**

O total de CBS monofásica informado na NF-e ou NFC-e não corresponde ao somatório dos valores de CBS monofásica dos respectivos itens do documento fiscal.

**SOLUÇÃO**

Para corrigir esta rejeição, siga os passos abaixo:

**(1)** Acesse a tela **"Tipos de Operação - TOP"** (Comercial » Arquivo » Cadastros » Tipos de Operação - TOP).

**(2)** Localize e selecione a TOP utilizada na emissão do documento fiscal rejeitado.

**(3)** Na aba **''Impostos''**, na sessão **''Reforma Tributária''**, verifique se o campo **''Tem CBS''** está habilitado.

- Habilite o campo para garantir que o sistema calcule corretamente o valor total com base nos itens.

**(4)** Salve as alterações.

**(5)** Inutilize a numeração da NF-e rejeitada.

**(6)** Exclua o documento fiscal rejeitado.

**(7)** Realize um novo lançamento do documento fiscal para que o sistema aplique as novas configurações de proporcionalidade. 

 **CAUSA**

A rejeição ocorre devido à validação UB105-10 da SEFAZ, que verifica se o valor total da CBS Monofásica do documento é igual à soma dos valores da CBS Monofásica de cada item.

Conforme a regra, o valor total da CBS Monofásica do item (vTotCBSMonoItem) deve ser resultante da fórmula:

```
vTotCBSMonoItem = vCBSMono + vCBSMonoReten - vCBSMonoDif.
```

Quando o sistema não está configurado para calcular proporcionalmente os valores da CBS monofásica, pode ocorrer divergência entre o valor total informado no documento e a soma dos valores dos itens, resultando na rejeição do documento fiscal pela SEFAZ.

---
id: "37095551270935"
titulo: "1011 Rejeição: Não é permitido uso do Imposto Seletivo para esta classificação da operação [nItem: 999]"
url: "https://ajuda.sankhya.com.br/hc/pt-br/articles/37095551270935-1011-Rejei%C3%A7%C3%A3o-N%C3%A3o-%C3%A9-permitido-uso-do-Imposto-Seletivo-para-esta-classifica%C3%A7%C3%A3o-da-opera%C3%A7%C3%A3o-nItem-999"
trilha: "Solução de Problemas > Rejeições: NF-e / NFS-e / NFC-e - Reforma tributária "
atualizado_em: "2026-07-22T14:21:42Z"
rotulos: ["Configuração", "NF-e", "SEFAZ", "Impostos", "NCM", "Erro", "Reforma Tributária", "Assistente de Configuração Integral da Reforma Tributária", "Imposto Seletivo", "reforma Tributária (Lei Complementar nº 214/2025)", "Classificação tributária do Imposto Seletivo (cClassTribIS)"]
---

# 1011 Rejeição: Não é permitido uso do Imposto Seletivo para esta classificação da operação [nItem: 999]

**MENSAGEM**

1011 Rejeição: Não é permitido uso do Imposto Seletivo para esta classificação da operação [nItem: 999]

**SITUAÇÃO**

Esta rejeição ocorre quando o usuário tenta emitir uma NF-e ou NFC-e incluindo o grupo de Imposto Seletivo (IS) para um item cuja classificação tributária não permite a aplicação deste imposto. O sistema da Sefaz identifica uma incompatibilidade entre a classificação tributária do Imposto Seletivo (cClassTribIS) informada no documento fiscal e a utilização do grupo IS.

**SOLUÇÃO**

Para resolver esta rejeição, siga os passos abaixo:

**(1)** Verifique a classificação tributária do Imposto Seletivo (cClassTribIS) utilizada no item rejeitado e confirme se este produto realmente deve ser tributado pelo Imposto Seletivo.

**(2)** Acesse a tela **"Produtos"** (Configurações » Cadastros » Produtos » Produtos) e localize o produto que gerou a rejeição.

**(3)** Na aba **''Impostos''**, verifique se o campo **''NCM''** está informado corretamente conforme o produto, e se este NCM está sujeito á tributação do Imposto Seletivo conforme a legislação vigente.

**(4)** Acesse a tela **''Assistente de Configuração Integral da Reforma Tributária''** (Livros Fiscais » Cadastros » Assistente de Configuração Integral da Reforma Tributária), e verifique as configurações de tributação do **Imposto Seletivo** para o produto em questão.

**(5)** Caso o produto não deva ser tributado pelo Imposto Seletivo, remova o grupo IS da nota fiscal, ajustando a configuração tributária do item.

**(6)** Se o produto deve ser tributado pelo Imposto Seletivo, verifique se a classificação tributária (cClassTribIS) está corretamente configurada de acordo com a operação realizada.

**(7)** Após realizar os ajustes necessários, tente emitir a nota fiscal novamente.

**CAUSA**

Esta rejeição ocorre devido à implementação das regras de validação da Reforma Tributária (Lei Complementar nº 214/2025), especificamente a regra **UB01-10**, que verifica a compatibilidade entre a classificação tributária do Imposto Seletivo (cClassTribIS) e a aplicação deste imposto no documento fiscal.

O Imposto Seletivo (IS) é aplicável apenas a produtos específicos, conforme determinado pela legislação. Quando o sistema identifica que o grupo IS foi informado para um item cuja classificação tributária não permite a aplicação deste imposto, a nota é rejeitada.

A causa específica é a tentativa de utilizar o grupo de Imposto Seletivo (IS) para uma classificação tributária (cClassTribIS) que não está habilitada para receber este tipo de tributação, gerando incompatibilidade entre a classificação informada e a aplicação do imposto.

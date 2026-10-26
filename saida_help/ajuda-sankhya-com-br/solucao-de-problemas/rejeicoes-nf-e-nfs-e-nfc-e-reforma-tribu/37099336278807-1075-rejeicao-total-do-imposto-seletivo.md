---
id: "37099336278807"
titulo: "1075 Rejeição: Total do Imposto Seletivo difere da soma dos itens"
url: "https://ajuda.sankhya.com.br/hc/pt-br/articles/37099336278807-1075-Rejei%C3%A7%C3%A3o-Total-do-Imposto-Seletivo-difere-da-soma-dos-itens"
trilha: "Solução de Problemas > Rejeições: NF-e / NFS-e / NFC-e - Reforma tributária "
atualizado_em: "2026-07-22T14:19:49Z"
rotulos: ["Configuração", "NF-e", "SEFAZ", "Impostos", "Passos para resolver", "Erro", "Como Resolver", "Reforma Tributária", "NF-e ou NFC-e", "Alíquotas de IBS", "Imposto Seletivo", "Valores de IS calculados", "Imposto Seletivo difere da soma"]
---

# 1075 Rejeição: Total do Imposto Seletivo difere da soma dos itens

**MENSAGEM**

1075 Rejeição: Total do Imposto Seletivo difere da soma dos itens

**SITUAÇÃO**

Ao emitir uma **NF-e (modelo 55)** ou **NFC-e (modelo 65)** com produtos sujeitos ao **Imposto Seletivo (IS)**, o **sistema identificou uma divergência entre o valor total do IS informado no rodapé da nota e o somatório dos valores de IS calculados em cada item**.

**SOLUÇÃO**

Para corrigir esta rejeição, siga os passos abaixo:

**(1)** Acesse a tela **''Produtos''** (Configurações » Cadastros » Produtos » Produtos) e certifique-se de que a **Classificação Tributária do IS** esteja corretamente definida para cada item sujeito ao IS.

**(2)** Acesse a tela **''Assistente de Configuração Integral da Reforma Tributária''** (Livros Fiscais » Cadastros » Assistente de Configuração Integral da Reforma Tributária) e verifique se as alíquotas percentuais (pIS) e específicas (pISEspec) estão cadastradas corretamente.

**(3)** Revise o **CST do Imposto Seletivo** aplicado a cada item da nota fiscal. Certifique-se de que o código utilizado seja compatível com a operação e esteja corretamente configurado.

**(4)** Caso esteja realizando lançamentos manuais do IS, recalcule o valor do imposto para cada item utilizando a fórmula correta:

- **Para alíquota percentual:** vIS = vBCIS \* (pIS / 100)
- **Para alíquota específica:** vIS = qTrib \* pISEspec

Onde:

```
vIS = Valor do Imposto Seletivo vBCIS = Base de cálculo do IS pIS = Alíquota percentual do IS qTrib = Quantidade tributável pISEspec = Alíquota específica do IS
```

**(5)** Após as correções, verifique se o valor total do IS no rodapé da nota corresponde exatamente à soma dos valores de IS de todos os itens. O sistema deve calcular automaticamente este total como:

```
vTotalIS = Σ(vIS de todos os itens).
```

**CAUSA**

Esta rejeição ocorre quando o **valor total do Imposto Seletivo (IS)** **informado no grupo de totais da NF-e ou NFC-e é diferente do somatório dos valores de IS calculados em cada item da nota fiscal**. A divergência pode ser causada por:

- Erros de arredondamento no cálculo manual do IS;
- Configuração incorreta das alíquotas do IS (percentual ou específica);
- Inconsistência na base de cálculo do IS utilizada para cada item;
- Falha na totalização automática dos valores de IS no documento fiscal;
- Classificação tributária do IS incorreta ou incompatível com a operação.

A validação é realizada pela SEFAZ para garantir a consistência dos valores declarados no documento fiscal, assegurando que o total do Imposto Seletivo corresponda exatamente à soma dos valores calculados para cada item, conforme estabelecido pela Lei Complementar 214 de 16 de janeiro de 2025.

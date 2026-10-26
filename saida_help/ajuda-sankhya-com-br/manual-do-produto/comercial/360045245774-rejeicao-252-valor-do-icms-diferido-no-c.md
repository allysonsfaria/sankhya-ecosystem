---
id: "360045245774"
titulo: "Rejeição 252 - Valor do ICMS Diferido no CST=51 difere do produto Valor ICMS Operação"
url: "https://ajuda.sankhya.com.br/hc/pt-br/articles/360045245774-Rejei%C3%A7%C3%A3o-252-Valor-do-ICMS-Diferido-no-CST-51-difere-do-produto-Valor-ICMS-Opera%C3%A7%C3%A3o"
trilha: "Manual do Produto > Comercial e Vendas > Comercial > Comercial"
atualizado_em: "2026-07-29T14:33:49Z"
rotulos: ["Configuração", "NF-e", "XML", "SEFAZ", "Impostos", "CST", "Rejeição 252 - Valor do ICMS Diferido no CST=51 difere do produto Valor ICMS Operação", "Cálculo de ICMS", "Diferimento Total ou Parcial", "Emissão de NF-e com CST-51"]
---

# Rejeição 252 - Valor do ICMS Diferido no CST=51 difere do produto Valor ICMS Operação

```
![Imagem 1](https://ajuda.sankhya.com.br/hc/article_attachments/42312120868247) Módulo: Comercial > Avançado > Certificações
```

---

Para emissão de NF-e com CST-51 - Diferimento, onde a TOP está definida no campo **"Cálculo de ICMS, IPI E ISS"** com a opção **"Não calcula e digita"**, é necessário que o valor informado no campo **"Valor"** dos impostos do item seja menor que o valor resultante do cálculo (Base de ICMS x Alíq. ICMS), caracterizando assim, o diferimento total ou parcial.

Inserindo "0,00" no campo Valor dos impostos do item caracteriza o diferimento total, e valores maiores do que 0,00 e menor que o resultado do cálculo caracteriza o diferimento parcial.

Desta forma, deve-se habilitar o parâmetro **"Processa Dif. ICMS Digitado para XML NF-e - DIFICMDIGXMLNFE"** para evitar as rejeições abaixo:

- Rejeição: Valor do ICMS da Operação no CST=51 difere do produto BC e Alíquota;
- Rejeição: Valor do ICMS Diferido no CST=51 difere do produto Valor ICMS Operação e percentual diferimento;
- Rejeição: Valor do ICMS no CST=51 não corresponde a diferença do ICMS operação e ICMS diferido.

**Observação:** O valor do ICMS informado no item seguirá a regra de cálculo abaixo quando a TOP estiver definida com Não calcula e digita no campo Cálculo de ICMS, IPI e ISS:

- **Cálculo ICMS integral:** Base Calc ICMS x Aliq.ICMS = <vICMSOp> (arredondamento para 2 casas decimais);
- **Cálculo do ICMS diferido:** (Base Calc ICMS x Aliq.ICMS) x % Diferimento = <vICMSDif> (arredondamento para 2 casas decimais);
- **Cálculo do ICMS:** vICMSOp - vICMSDif = <vICMS> (arredondamento para 2 casas decimais, esse valor deve ser digitado no campo Valor da TGFDIN.

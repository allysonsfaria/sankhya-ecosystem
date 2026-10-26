---
id: "34151349615895"
titulo: "Valor unitário da NF-e diferente do Valor unitário informado no item da central"
url: "https://ajuda.sankhya.com.br/hc/pt-br/articles/34151349615895-Valor-unit%C3%A1rio-da-NF-e-diferente-do-Valor-unit%C3%A1rio-informado-no-item-da-central"
trilha: "Dúvidas Frequentes > Vendas"
atualizado_em: "2026-07-22T14:27:27Z"
rotulos: ["Configuração", "NF-e", "XML", "SEFAZ", "Impostos", "Parâmetros", "Preferências", "DIVTOTQTDNFE", "no item da central", "Valor unitário da NF-e", "diferente do Valor unitário informado", "vProd", "qCom", "vUnCom"]
---

# Valor unitário da NF-e diferente do Valor unitário informado no item da central

**MENSAGEM:**

O valor unitário exibido na NF-e impressa é diferente do valor informado originalmente na central, mesmo que a quantidade e o valor total do item estejam corretos.

**SITUAÇÃO:**

Ao informar um valor unitário específico em um item de lançamento na central e aprovar a nota, o usuário percebe que o valor unitário impresso na NF-e difere do valor originalmente informado. Apesar disso, a **quantidade** e o **valor total do item** permanecem corretos.

**SOLUÇÃO:**

O ajuste do valor unitário é controlado pelo parâmetro **“DIVTOTQTDNFE”** (divide VLRTOT do item pela QTDNEG no XML da NFE). Siga os passos abaixo para entender e ajustar o comportamento:

**(1)** Acesse a tela **''Parâmetros''** (Configurações» Avançado» Preferências» Parâmetros);

**(2)** Localize o parâmetro DIVTOTQTDNFE;

**(3)** Mantenha o parâmetro ativado para que o sistema divida a tag **<vProd>** (valor total do produto) pela tag **<qCom>** (quantidade) no XML da NF-e, ajustando o valor unitário conforme o limite de casas decimais permitido pela SEFAZ.

**(4)** Caso seja necessário desligar o parâmetro, o valor unitário no XML será idêntico ao informado na central, porém aumenta o risco de rejeição fiscal.

**(5)** Evite trabalhar com quantidades excessivas de casas decimais para minimizar ajustes automáticos.

**Exemplo prático:**

- Quantidade do item na central: **1,102960**
- Valor unitário do item na central: **346,50**
- Valor total do item na central: **35,68**
- No XML:

  **<qCom>:** 0,103 (máximo 3 casas decimais)

  **<vProd>:** 35,68 (fixo com 2 casas decimais)

  **<vUnCom>**: ajustado para 346,37 para garantir que 0,103 × 346,37 = 35,67711 → arredondado = 35,68

O ajuste é feito “para baixo” para garantir que o total não seja ultrapassado após arredondamento.

**Boas práticas:**

- Evite trabalhar com quantidades excessivas de casas decimais.
- Mantenha o parâmetro ativado para prevenir rejeições fiscais na SEFAZ.

**CAUSA**

O valor unitário impresso na NF-e difere do informado na central devido ao ajuste automático realizado pelo parâmetro ''**DIVTOTQTDNFE''**, que recalcula o valor unitário no XML para se enquadrar nas regras de arredondamento e casas decimais exigidas pela SEFAZ. Esse processo garante que o valor total do produto no XML permaneça exato e não gere rejeições fiscais, mesmo que o valor unitário impresso não seja exatamente igual ao informado originalmente.

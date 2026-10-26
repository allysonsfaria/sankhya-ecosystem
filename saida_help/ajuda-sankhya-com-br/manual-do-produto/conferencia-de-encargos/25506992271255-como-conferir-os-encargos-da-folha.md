---
id: "25506992271255"
titulo: "Como conferir os encargos da folha"
url: "https://ajuda.sankhya.com.br/hc/pt-br/articles/25506992271255-Como-conferir-os-encargos-da-folha"
trilha: "Manual do Produto > Pessoas+ > Encargos e Obrigações Legais > Conferência de Encargos"
atualizado_em: "2026-10-02T15:55:28Z"
rotulos: ["Conferência", "Configuração", "Eventos", "Cálculo", "Impostos", "Folha", "INSS", "eSocial", "ID: br.com.sankhya.rh.CalculoIndFolha", "Conferência de Encargos", "Desconto simplificado", "Conferência Individual da Folha", "Contribuição Sindical", "FGTS", "Eventos que compõem bases", "FPCONFENCGARGOS", "IRRF"]
---

# Como conferir os encargos da folha

```
 Versão disponível: A partir da 5.18 Pessoal+
```

---

![Imagem 1: Para utilização dessa funcionalidade é necessário ligar o parâmetro "Habilita conferência encargos? - FPCONFENCGARGOS"…](https://ajuda.sankhya.com.br/hc/article_attachments/25528091528087) Para utilização dessa funcionalidade é necessário ligar o parâmetro **"Habilita conferência encargos? - FPCONFENCGARGOS"**. A partir da versão 5.18 do Pessoal+, já estará ativo automaticamente.

Através da [Medida Provisória 1.171/2023](https://www.planalto.gov.br/ccivil_03/_ato2023-2026/2023/Mpv/mpv1171.htm), foi inserido o desconto simplificado como alternativa de dedução da base do imposto de renda, de modo que a dedução corresponda a 25% do limite da faixa da alíquota zero, caso este valor seja benéfico ao funcionário.

### Demonstrativo de valores para eSocial

Após realizar o [cálculo](https://ajuda.sankhya.com.br/hc/pt-br/articles/20441795691031) da folha, durante a conferência dos valores, na aba [Folha](https://ajuda.sankhya.com.br/hc/pt-br/articles/20441795691031-C%C3%A1lculos#AbaFolha), seção **"eSocial"** serão apresentados os demonstrativos dos valores apurados para o cálculo em comparação aos valores apurados para o eSocial.

![Imagem 2: Após realizar o cálculo da folha, durante a conferência dos valores, na aba Folha , seção "eSocial" serão apresentados…](https://ajuda.sankhya.com.br/hc/article_attachments/25510114914583)

Os valores dos campos **"INSS"**, **"FGTS"** e **"Contribuição Sindical"** serão apresentados ao lado do valor correspondente à sua base de cálculo, e, se houver, também será exibido o valor da diferença entre elas separadas pelo tipo de tributação. Lembrando que, as linhas por tributação só serão exibidas quando o seu valor for maior que zero.

Ao passar o mouse sobre os valores, surgirá a descrição informando do que se trata o valor e se é referente ao eSocial ou apuração do cálculo.

[GIF animado: Imagem 3: Ao passar o mouse sobre os valores, surgirá a descrição informando do que se trata o valor e se é referente ao eSocial…](https://ajuda.sankhya.com.br/hc/article_attachments/25510114917655)

**Observação:** para apuração desses valores são consideradas as configurações de cada um dos [Eventos](https://ajuda.sankhya.com.br/hc/pt-br/articles/4405026143767) utilizados no cálculo, então caso haja divergência nos valores apurados entre o cálculo e o eSocial, tratam-se de configurações divergentes nos eventos do cálculo.

### Demonstrativo de apuração da base de IRRF

Ao acessar a seção **"Bases"** e clicar no botão **"Eventos que compõem"**, serão demonstrados os eventos que compõem a base de IRRF e os valores deduzidos no cálculo da base.

![Imagem 4: Ao acessar a seção "Bases" e clicar no botão "Eventos que compõem" , serão demonstrados os eventos que compõem a base…](https://ajuda.sankhya.com.br/hc/article_attachments/25510172510103)

Pode-se observar também que na parte inferior do pop-up é informado o que foi mais benéfico neste cálculo para a apuração da base de IRRF, se seriam os descontos legais ou se seria o desconto simplificado. Assim, caso exista um evento de desconto simplificado no cálculo será apresentada a seguinte informação:

**"O valor da soma das deduções legais foi MENOR que o valor desconto simplificado (evento valor do desconto simplificado), portanto foi deduzido o DESCONTO SIMPLIFICADO para encontrar a base de cálculo."**

Se o desconto simplificado não estiver no cálculo individual, a informação abaixo será exibida:

**"O valor da soma das deduções legais foi MAIOR que o valor desconto simplificado e portanto foram deduzidas as deduções legais para encontrar a base de cálculo."**

**Observação:** os eventos de desconto simplificado têm as seguintes identificações:

- 202 - Dedução Simplificada de IRRF;
- 203 - Dedução Simplificada de IRRF de 13°;
- 204 - Dedução Simplificada de IRRF de Férias.

![Imagem 5: 204 - Dedução Simplificada de IRRF de Férias.](https://ajuda.sankhya.com.br/hc/article_attachments/25510172513559)

**Importante:** nos casos em que houver mais de um pagamento no mesmo período de apuração, ou seja, tenha recomposição de bases para o cálculo de IRRF, neste pop-up também serão demonstrados os valores da folha que está recompondo a base.

![Imagem 6: Importante: nos casos em que houver mais de um pagamento no mesmo período de apuração, ou seja, tenha recomposição de…](https://ajuda.sankhya.com.br/hc/article_attachments/25510172521879)

[[voltar ao topo]](https://ajuda.sankhya.com.br/hc/pt-br/articles/25506992271255-Como-conferir-os-encargos-da-folha#top)

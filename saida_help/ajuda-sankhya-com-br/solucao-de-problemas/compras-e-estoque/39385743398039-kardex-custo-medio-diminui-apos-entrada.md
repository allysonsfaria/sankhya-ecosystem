---
id: "39385743398039"
titulo: "Kardex: custo médio diminui após entrada de bonificação com valor zero"
url: "https://ajuda.sankhya.com.br/hc/pt-br/articles/39385743398039-Kardex-custo-m%C3%A9dio-diminui-ap%C3%B3s-entrada-de-bonifica%C3%A7%C3%A3o-com-valor-zero"
trilha: "Solução de Problemas > Compras e Estoque"
atualizado_em: "2026-10-07T03:21:20Z"
rotulos: ["Custos", "Configuração", "Relatórios", "TOP", "Estoque", "Artigo criado KCS", "CVE - KCS"]
---

# Kardex: custo médio diminui após entrada de bonificação com valor zero

**Situação**

Ao lançar notas fiscais de bonificação de entrada (produto recebido sem valor), os valores apresentados no relatório **"Kardex"** (Comercial » Relatórios » Kardex) podem parecer divergentes: a quantidade em estoque aumenta, mas o valor total do estoque não acompanha, e o custo médio do produto diminui.

**Solução**

O tratamento da bonificação no custo é definido pelo campo **Precifica** da TOP usada na nota de entrada. Antes de alterar, defina com a contabilidade da empresa se a bonificação deve ou não reduzir o custo médio.

Acesse a tela **"Tipos de Operação - TOP"** (Comercial » Arquivo » Cadastros) e localize a TOP utilizada na bonificação de entrada.
 Na aba **Geral**, grupo **Preço/custo**, confira o campo **Precifica**:

- **Atualiza custo e preço de venda** ou **Atualiza somente custo**: a bonificação entra no custo médio com o valor da nota. Com valor zero, o custo médio diminui. Essa é a configuração aceita pela verificação do Kardex.
- **Atualiza custo pelo agendador**: mesmo efeito, mas o custo só é atualizado quando o agendador de recálculo de custos é executado.
- **Não atualiza custo nem preço de venda**: a bonificação não altera o custo médio, e o Kardex mostra a entrada pelo custo médio do dia. **Atenção:** a verificação do Kardex aponta essa TOP como inconsistente, porque as unidades recebidas sem custo passam a ser avaliadas pelo custo médio, como se tivessem sido compradas.

Salve a alteração. O sistema cria uma nova versão da TOP, que vale apenas para as notas lançadas a partir desse momento. As notas já lançadas continuam com a configuração anterior.
 Se for preciso refazer o custo de um período, use a tela **"Recálculo de Custos"** (Comercial » Avançado). O recálculo usa a configuração da TOP gravada em cada nota, por isso não muda o tratamento das bonificações já lançadas.
 Na tela **Kardex**, clique em **Verificar**. A conferência analisa o saldo de estoque, as TOPs de entrada que não atualizam custo e as alterações em parâmetros de custo, e indica a correção sugerida.

**(7)** Gere o Kardex novamente para confirmar os valores.

**Causa**

O custo médio é o valor total do estoque dividido pela quantidade. Quando a TOP da bonificação de entrada atualiza custo, as unidades recebidas entram nessa conta com o valor da nota. Se o valor é zero, a quantidade aumenta, o valor total não, e o custo médio diminui. **Esse é o comportamento padrão do sistema.**

Na bonificação de saída (produto enviado ao cliente), o custo não é alterado: o Kardex sempre valoriza as saídas pelo custo médio, mesmo quando a nota tem valor zero. O campo **Financeiro** da TOP não interfere no custo médio nem nos valores do Kardex.

---
id: "360044606354"
titulo: "Descontos Financeiros por Parceiro"
url: "https://ajuda.sankhya.com.br/hc/pt-br/articles/360044606354-Descontos-Financeiros-por-Parceiro"
trilha: "Manual do Produto > Configurações e Cadastros > Configurações"
atualizado_em: "2026-07-29T13:53:58Z"
rotulos: ["manual", "Configuração", "Descontos Financeiros", "Descontos Financeiros por Parceiro", "USADESCFIN", "br.com.sankhya.com.avancado.descontofinanceiroporparceiro", "Descontos Financeiros por Parceiro manual", "Desconto", "Parâmetros", "Financeiro", "Personalização", "Descontos financeiros", "parceiro"]
---

# Descontos Financeiros por Parceiro

```
![Imagem 1](https://ajuda.sankhya.com.br/hc/article_attachments/42310845416215) Módulo: Configurações > Avançado
```

---

|  | ![Imagem 2](https://ajuda.sankhya.com.br/hc/article_attachments/42310829145367) | Essa é uma tela apenas de cadastro que foi migrada para o Sankhya Om, portanto, a inserção de descontos no financeiro ainda não está presente no sistema e deverá ser realizada por meio de regras de personalização (botão de ação). |  |
| --- | --- | --- | --- |

---

Cadastre nessa tela possíveis descontos para um parceiro e/ou filial, sendo que, eles poderão ser disponibilizados por aniversário, inauguração, assiduidade, entre outros. 

![Imagem 3: Cadastre nessa tela possíveis descontos para um parceiro e/ou filial, sendo que, eles poderão ser disponibilizados por…](https://ajuda.sankhya.com.br/hc/article_attachments/1500000091501)

Esta tela só estará habilitada para utilização se o parâmetro **"Usar Desconto Financeiro por Parceiro - USADESCFIN"** estiver habilitado. Caso o referido parâmetro esteja desligado, ao abrir a tela, o sistema exibirá a mensagem exibida na imagem abaixo.

**"O parâmetro USADESCFIN não está configurado para usar esta opção".**

Com este aviso, será possível habilitá-la, dando continuidade normalmente aos cadastros.

Na aba **"Descontos por** **Período"**, você deve cadastrar o **"Parceiro"** que receberá o desconto, informando a **"Data Início"** e a **"Data Fim"** juntamente com o **"Valor de desconto"** e/ou o **"Percentual de Desconto"** a ser concedido na operação.

**Observação:** o sistema só permitirá a criação de um desconto financeiro por parceiro se a data de início for até 30 dias antes da sua data de criação. Por exemplo, suponhamos que hoje seja 25/08/2021, e você deseja criar um desconto financeiro, para isso, a Data Início deverá ser igual ou superior a 26/07/2021.

Através do botão ![Imagem 4: Através do botão "Outras Opções..." , você poderá duplicar (entenda-se por duplicar, a possibilidade de aproveitar os…](https://ajuda.sankhya.com.br/hc/article_attachments/16242344017687) **"Outras** **Opções..."**, você poderá duplicar (entenda-se por duplicar, a possibilidade de aproveitar os campos já preenchidos para determinado Parceiro ou Filial e reutilizá-los, otimizando assim o trabalho) o desconto através das opções **"Duplicar para um Parceiro..."** ou **"Duplicar para Filiais"**.

Ao selecionar Duplicar para um Parceiro..., o sistema duplicará os dados dos campos da aba Descontos por Período, com exceção do campo Parceiro, pois, neste campo, você deve informar o novo parceiro para o qual o desconto será copiado. Após a indicação do parceiro, salve o registro.

Caso seja selecionado a opção Duplicar para Filiais, o sistema abrirá uma tela contendo as filiais para que seja selecionada aquela que receberá o desconto.

![Imagem 5: Caso seja selecionado a opção Duplicar para Filiais , o sistema abrirá uma tela contendo as filiais para que seja…](https://ajuda.sankhya.com.br/hc/article_attachments/1500000091521)

Caso você queira selecionar somente algumas das filiais que estão sendo apresentadas, é possível realizar a seleção pressionando a tecla **"Ctrl"** do teclado e clicando sobre o item. Para marcar ou desmarcar todos os itens, você pode fazer por meio dos botões ![Imagem 6: Caso você queira selecionar somente algumas das filiais que estão sendo apresentadas, é possível realizar a seleção…](https://ajuda.sankhya.com.br/hc/article_attachments/16242394907799) **"Marcar Todas"** e ![Imagem 7: Caso você queira selecionar somente algumas das filiais que estão sendo apresentadas, é possível realizar a seleção…](https://ajuda.sankhya.com.br/hc/article_attachments/16242403097239) **"Desmarcar Todas"**.

Caso não existam filiais cadastradas para o Parceiro, o sistema exibirá a mensagem:

**"Não encontramos filiais para este código de Matriz."**

### Parâmetros que influenciam nessa rotina

**Considerar desconto financeiro p/ tag vLiq NF-e? - VDESCFINVLIQNFE**: ao habilitar este parâmetro, o Valor de desconto financeiro irá subtrair o Vlr. Desdobramento e gerar o valor líquido do financeiro, não alterando o valor da nota na [Central de Vendas](https://ajuda.sankhya.com.br/hc/pt-br/articles/360044612414).

**Cálculo de Juro obrigatório - JUROOBRIG:** Se estiver ligado, manterá o valor dos juros quando um título for estornado. Se estiver desligado, o valores de juros serão limpos ao estornar. Este parâmetro deve estar ligado para que seja feita a impressão do Valor Líquido na linha digitável do boleto.

**Calcula valor líquido boleta? - VLRLIQBOL**: este parâmetro gera o valor total da duplicata líquida. O Valor Líquido é o Vlr. Desdobramento, aplicando sobre ele tudo que afeta o valor a ser pago, como juros, multa, descontos, impostos retidos (do próprio financeiro e outros impostos). Ele influencia apenas na emissão de boletos e assim como o parâmetro Cálculo de Juro obrigatório - JUROOBRIG, também deve estar ligado para que seja possível a impressão do Valor Líquido na linha digitável do boleto.

[[Voltar ao topo]](https://ajuda.sankhya.com.br/hc/pt-br/articles/360044606354-Descontos-Financeiros-por-Parceiro#top)

---
id: "44012484432791"
titulo: "[Routing] - Formula para Calculo de Custo com base no Valor"
url: "https://ajuda.sankhya.com.br/hc/pt-br/articles/44012484432791--Routing-Formula-para-Calculo-de-Custo-com-base-no-Valor"
trilha: "Lincros > Roteirizador"
atualizado_em: "2026-10-05T19:29:58Z"
rotulos: ["sync_hc", "lincros", "lincros_13433555", "sync_hash_0dcf70d7fec7"]
---

# [Routing] - Formula para Calculo de Custo com base no Valor

**Menu**: Cadastro > Transportadoras

**Objetivo**: Cadastrar formula para calculo de custo baseado em valores

**Considerações**:

- Possuir transportadoras cadastradas para o deposito;
- Possuir “Tipos de Veículos” cadastrados
- Fórmulas adicionadas aumentam o tempo de cálculo da rota
- Pedágio OSM ativo no depósito prolonga o tempo de cálculo

**Cadastro de fórmula com base em percentual**:

1. Acesse Cadastros > Transportadoras, localize a transportadora desejada e clique em editar (ícone lápis)

   ![Imagem 1: Acesse Cadastros > Transportadoras, localize a transportadora desejada e clique em editar (ícone lápis)](https://ajuda.sankhya.com.br/hc/article_attachments/44012442180503)
2. Na lateral esquerda, você encontrará os "Tipos de Veículos", e na lateral direita, a coluna "Fórmula". Para cada tipo de veículo, é necessário cadastrar a fórmula individualmente. Para isso, vá até a coluna "Fórmula" correspondente e clique no ícone de calculadora para aplicar a fórmula desejada.

   ![Imagem 2: Na lateral esquerda, você encontrará os "Tipos de Veículos", e na lateral direita, a coluna "Fórmula". Para cada tipo…](https://ajuda.sankhya.com.br/hc/article_attachments/44012442303383)
3. Ao selecionar a opção "Fórmula" para um determinado tipo de veículo, será aberta uma tela com as informações da Transportadora e do Tipo de Veículo. Logo abaixo, estarão os campos "Variáveis" e "Fórmula", onde você poderá configurar os cálculos necessários.

   ![Imagem 3: Ao selecionar a opção "Fórmula" para um determinado tipo de veículo, será aberta uma tela com as informações da…](https://ajuda.sankhya.com.br/hc/article_attachments/44012484933271)
4. Primeiro, no campo "Variáveis", selecione a opção "Valor".

   ![Imagem 4: Primeiro, no campo "Variáveis", selecione a opção "Valor".](https://ajuda.sankhya.com.br/hc/article_attachments/44012493546391)

5.Após selecionar a variável, complete a fórmula multiplicando pelo percentual desejado, seguido da letra "M", dentro dos parênteses. Exemplo: (Valor \* (0.10M)). Em seguida, insira a fórmula no campo "Fórmula" e clique em Confirmar para salvar as informações corretamente.

![Imagem 5: 5.Após selecionar a variável, complete a fórmula multiplicando pelo percentual desejado, seguido da letra "M", dentro…](https://ajuda.sankhya.com.br/hc/article_attachments/44012462517143)

**Observação:** O valor 0.10 na fórmula pode ser ajustado conforme necessário, pois representa a porcentagem utilizada no cálculo. Por exemplo, 0.10 equivale a 10% do valor da mercadoria da rota, ou seja, o custo da rota será calculado como 10% do valor total transportado. Se desejar um percentual diferente, basta substituir 0.10 pelo valor correspondente (ex: 0.15 para 15%, 0.05 para 5% etc.).

6. Após inserir e salvar a fórmula de cálculo de custo, você poderá criar sessões com os custos aplicados.

Após iniciar a sessão, você poderá validar os valores de custo na lateral direita. Ao selecionar uma rota, serão exibidas as informações detalhadas da rota, incluindo os custos individuais associados a ela.

![Imagem 6: Após iniciar a sessão, você poderá validar os valores de custo na lateral direita. Ao selecionar uma rota, serão…](https://ajuda.sankhya.com.br/hc/article_attachments/44012485336983)

Na sessão da lateral esquerda, também é possível analisar os custos totais de todas as rotas da sessão, caso haja mais de uma rota com custos.

![Imagem 7: Na sessão da lateral esquerda, também é possível analisar os custos totais de todas as rotas da sessão, caso haja mais…](https://ajuda.sankhya.com.br/hc/article_attachments/44012476450327)

## Cadastro de fórmula com base no valor do setor:

1. O primeiro cadastro a ser realizado é no setor. É necessário definir o "Valor Fórmula" do setor. Para isso, acesse Cadastros > Setor > Editar (ícone de lápis). Uma janela com várias opções será aberta. No campo "Valor Fórmula", informe o valor que será utilizado para calcular o custo da rota. O custo será calculado multiplicando o valor informado neste campo pelo valor das mercadorias da rota.

   ![Imagem 8: O primeiro cadastro a ser realizado é no setor. É necessário definir o "Valor Fórmula" do setor. Para isso, acesse…](https://ajuda.sankhya.com.br/hc/article_attachments/44012449082135)

   ![Imagem 9: O primeiro cadastro a ser realizado é no setor. É necessário definir o "Valor Fórmula" do setor. Para isso, acesse…](https://ajuda.sankhya.com.br/hc/article_attachments/44012476716183)
2. Em Cadastros > Transportadoras, abra a mesma opção de fórmulas para cadastrar a fórmula com base no valor descrito no setor. Para isso, selecione a transportadora, clique em Editar, depois selecione o tipo de veículo e clique em Fórmula.

   ![Imagem 10: Em Cadastros > Transportadoras, abra a mesma opção de fórmulas para cadastrar a fórmula com base no valor descrito no…](https://ajuda.sankhya.com.br/hc/article_attachments/44012463307159)

3.Primeiro, no campo "Variáveis", selecione a opção "ValorSetor".

![Imagem 11: 3.Primeiro, no campo "Variáveis", selecione a opção "ValorSetor".](https://ajuda.sankhya.com.br/hc/article_attachments/44012494512919)

4. Após selecionar a variável "ValorSetor", na fórmula, digite o seguinte: **\_Valor\_\*\_ValorSetor\_** e clique em Confirmar.

![Imagem 12: 4. Após selecionar a variável "ValorSetor", na fórmula, digite o seguinte: _Valor_*_ValorSetor_ e clique em Confirmar.](https://ajuda.sankhya.com.br/hc/article_attachments/44012449635863)

Após inserir a fórmula de cálculo de custo, você poderá criar sessões e os dados serão exibidos conforme o exemplo anterior. No entanto, neste caso, os cálculos serão realizados com base na fórmula do setor (considerando o valor informado no setor), em vez do percentual informado na fórmula.

"Em atenção ao cumprimento de nossas políticas de segurança da informação e privacidade, alguns dados serão ocultados e protegidos"

---
id: "360044595774"
titulo: "Balancete Comparativo"
url: "https://ajuda.sankhya.com.br/hc/pt-br/articles/360044595774-Balancete-Comparativo"
trilha: "Manual do Produto > Fiscal e Contábil > Contábil > Contabilidade"
atualizado_em: "2026-07-29T16:01:43Z"
rotulos: ["AJUDA DO SKW", "manual", "Configuração", "Relatórios", "Projeto", "Centro de Resultado", "br.com.sankhya.mgecontab.balancetecomparativo", "Balancete Comparativo manual", "Contabilidade", "Financeiro", "Análise Detalhada com o Balancete Comparativo"]
---

# Balancete Comparativo

```
![módulo](https://ajuda.sankhya.com.br/guide-media/01H3C7W10NKRZHPYYX9G5YF38M) Módulo: Contabilidade > Consultas
```

---

O Balancete Comparativo é um demonstrativo que vai exibir a análise das variações de conta contábil durante um determinado período.

**Nota:** O relatório gerado nessa tela mostrará o saldo atual de cada conta considerando um período de 12 meses a partir da Referência selecionada. As opções de configurações dessa tela funcionam da mesma forma que as opções do [Balancete de Verificação](https://ajuda.sankhya.com.br/hc/pt-br/articles/360044607774-Balancete-de-Verifica%C3%A7%C3%A3o).

![Imagem 2: Nota: O relatório gerado nessa tela mostrará o saldo atual de cada conta considerando um período de 12 meses a partir…](https://ajuda.sankhya.com.br/hc/article_attachments/360104071453)

Na parte superior da tela, serão apresentados o código e a descrição da Razão Social da Empresa selecionada. Ao clicar na descrição, você pode escolher outra empresa para análise dos dados.

Você pode utilizar o botão ![visualizar](https://ajuda.sankhya.com.br/hc/article_attachments/15437558719511)**"Visualizar Relatório"** depois que as marcações e campos desejados forem configurados; sendo que, eles serão detalhados no decorrer desse artigo.

Para a geração do relatório, defina qual a data de **"Referência"** em que ele será gerado.

**Seção Conta Contábil**

No campo **"Considerar"**, determine o critério para apresentação das contas contábeis dentre as opções:

- **Todas:** Ao selecionar esta, todas as contas contábeis serão impressas no relatório.
- **Intervalo:** Quando essa opção for escolhida, os campos **"Inicial"** e **"Final"** serão habilitados e neles você informará o intervalo de contas para que o Balancete Comparativo seja gerado com base no que for definido.
- **Conta Reduzida:** Essa opção vai habilitar o campo **"Cód. Reduzido"** que, ao ser preenchido, o Balancete Comparativo será gerado somente com a conta informada nele.

**Seção Centro de Resultado**

Essa seção será habilitada, apenas se na tela [Preferências de Contabilidade da Empresa](https://ajuda.sankhya.com.br/hc/pt-br/articles/360044608114-Empresa), aba [Lançamentos](https://ajuda.sankhya.com.br/hc/pt-br/articles/360044608114-Empresa#abalanamentos), a marcação **"Utiliza Centro de resultado"** for selecionada.

Preencha nos campos dessa seção, o intervalo de Centros de Resultado que deverão ser apresentados no Balancete Comparativo.

**Seção Projeto**

Essa seção será disponibilizada apenas se na tela Preferências de Contabilidade da Empresa, aba Lançamentos, a marcação **"Utiliza Projeto"** estiver realizada. Assim, você pode informar nela o intervalo dos projetos que deverão ser exibidos no Balancete Comparativo.

**Seção Parâmetros de Impressão**

Nessa seção, temos algumas marcações que influenciarão na geração do relatório do Balancete Comparativo, são elas:

Quando a marcação **"Imprimir contas sem movimento e com saldo atual igual a zero"** estiver habilitada, as contas sem movimento em que o saldo atual é igual a zero serão exibidas no demonstrativo.

Referente à marcação **"Imprimir contas com movimento e com saldo atual igual a zero"**, quando selecionada, teremos as contas com movimento e com saldo atual igual a zero geradas no relatório.

Ao efetuar a marcação **"Imprimir contas sem movimento e com saldo atual diferente de zero"**, as contas sem movimentos e aquelas que possuem o saldo atual diferente de zero irão para o Balancete Comparativo.

**Observação:** Se você selecionar as três últimas marcações acima, o sistema utilizará a referência da Empresa selecionada para a busca do saldo atual, conforme configuração realizada nas Preferências de Contabilidade da Empresa, aba [Exercício](https://ajuda.sankhya.com.br/hc/pt-br/articles/360044608114-Empresa#abaexerccio), campo **"Referência"**, de modo que, se a empresa estiver com a referência de um ano contábil diferente do ano contábil informado no período, o sistema pesquisará pelo saldo da referência atual configurada para a busca do saldo atual.

Quando você habilitar a marcação **"Imprimir D/C nos saldos"**, serão impressos os caracteres D (Débito) ou C (Crédito) para os saldos das contas.

Ao selecionar a marcação **"Saltar folha na quebra de grau 1"**, todas as contas a serem impressas cujo grau 1 for diferente da conta anteriormente impressa, automaticamente ocorrerá um salto de página. Caso contrário, a impressão do relatório será contínua.

Se a marcação **"Imprimir em ordem alfabética o último grau"** for selecionada, em todas as contas impressas que o grau for igual ao Grau do Balancete, a impressão será realizada por ordem alfabética de suas descrições.

No campo **"Data e Hora da Emissão"**, serão apresentadas a data e hora atual da emissão do relatório; e caso seja necessário, você pode modificá-lo manualmente.

Quando a marcação **"Imprime Logomarca"** for realizada, a logomarca será gerada/impressa no canto superior esquerdo do relatório.

Ao realizar a marcação **"Geração da Assinatura conforme signatários?"**, na última página do lado esquerdo dos relatórios, a primeira assinatura será exibida, e assim por diante. A assinatura cadastrada, deve pertencer a mesma empresa da geração do demonstrativo; assim, a data de início/fim da assinatura deverá estar no período da data que está sendo gerado o demonstrativo, e a marcação Gerar Relatórios Contábeis deve ser selecionada.

**Importante:** Caso várias assinaturas sejam impressas, pode ser que o espaço não seja suficiente, por isso, elas podem ser impressas em outra página. Sendo que, a ordenação das assinaturas geradas será de acordo com o código do signatário.

Através da marcação **"Imprimir contas com saldo mês a mês acumulado?"**, você escolhe se na impressão do Balancete Comparativo será exibido o saldo da conta contábil mês a mês acumulado ou não, ou seja, com a marcação habilitada, será gerado o Balancete Comparativo sem acumular o saldo do mês anterior com o movimento do mês seguinte e assim sucessivamente.

Quando você efetuar a marcação **"Desprezar zeramento das contas de resultado?"**, fará com que o sistema desconsidere o zeramento das contas de resultado e gere o Balancete Comparativo apresentando as contas de resultado do mês em que ocorreu o zeramento.

Defina no campo **"Grau do Balancete"** em qual grau o relatório deverá ser gerado; considere o exemplo:

Uma conta **"1.1.2.03.0004"**, que possua Grau do Balancete igual a **"3"**, será ficará como: **"1.1.2"**.

No campo **"Quebra p/ Relatório"**, determine qual o tipo de quebra que o balancete sofrerá. Nele, você pode escolher dentre as seguintes opções:

- Somente Contas;
- Quebrar por CR;
- Combinar hierarquia do CR com a da conta;
- Hierarquia do CR sem as contas;
- Quebrar por Projeto;
- Combinar hierarquia do Projeto com a da Conta;
- Hierarquia do Projeto sem as contas;
- Quebrar por CR/Projeto;
- Quebrar por Projeto/CR;
- Quebrar por CR e combinar Projeto com Conta;
- Quebrar por Projeto e combinar CR com Conta.

Por meio do campo **"Formato da impressão"**, determine qual a extensão será utilizada para impressão do relatório, sendo que elas podem ser em **"PDF"** ou **"Excel (.xlsx)"**.

**Nota:** Se você selecionar o formato Excel, ao solicitar sua visualização, será realizado o download do relatório no referido formato contendo as informações condizentes com sua configuração.

Através do campo **"Opções de visualização"** será possível definir a forma de visualizar os relatórios de acordo com as opções abaixo: 

- Imprimir linhas zebradas;
- Imprimir com altura 10;
- Imprimir padrão.

**Nota:** Com a opção **"Imprimir padrão"** selecionada, as contas sintéticas serão apresentadas no Balancete Comparativo destacadas na cor amarela.

---

**Parâmetros que influenciam a rotina**

Quando o parâmetro **"Forçar o download de relatórios internos? - FORCEDOWNLOAD"** for habilitado, fará com que a visualização do relatório seja aberta pelo visualizador nativo do sistema operacional.

---
id: "360044607714"
titulo: "Demonstrativos Contábeis"
url: "https://ajuda.sankhya.com.br/hc/pt-br/articles/360044607714-Demonstrativos-Cont%C3%A1beis"
trilha: "Manual do Produto > Fiscal e Contábil > Contábil > Contabilidade"
atualizado_em: "2026-07-29T16:01:52Z"
rotulos: ["AJUDA DO SKW", "manual", "Configuração", "Relatórios", "ECD", "Demonstrativos Contábeis", "br.com.sankhya.mgecontab.rel.demonstrativocontabilecd", "Demonstrativos Contábeis manual", "Contabilidade", "Financeiro", "Eficiência na Análise: Demonstrativos Contábeis"]
---

# Demonstrativos Contábeis

```
![módulo](https://ajuda.sankhya.com.br/hc/article_attachments/42314964456471) Módulo: Contabilidade> Consultas> Demonstrativos Contábeis 
```

---

Por meio desta tela realiza-se a geração/visualização do relatório de Demonstrativos Contábeis. Dessa forma, teremos:

| [Campos da tela](https://ajuda.sankhya.com.br/hc/pt-br/articles/360044607714-Demonstrativos-Cont%C3%A1beis#camposdatela) | [Geração de relatórios](https://ajuda.sankhya.com.br/hc/pt-br/articles/360044607714-Demonstrativos-Cont%C3%A1beis#gera%C3%A7%C3%A3oderelat%C3%B3rios) |
| --- | --- |
| [Premissa para geração dos demonstrativos](https://ajuda.sankhya.com.br/hc/pt-br/articles/360044607714-Demonstrativos-Cont%C3%A1beis#premissaparagera%C3%A7%C3%A3odosdemonstrativos) |  |

![Imagem 2: Premissa para geração dos demonstrativos](https://ajuda.sankhya.com.br/hc/article_attachments/360087859413)

## Campos da tela

Determine inicialmente o **"Período"** a ser considerado para geração do relatório. O sistema buscará o período cadastrado nas [Preferências de Contabilidade da Empresa](https://ajuda.sankhya.com.br/hc/pt-br/articles/360044607994-Empresa), aba [Exercício](https://ajuda.sankhya.com.br/hc/pt-br/articles/360044607994-Empresa#abaexerccio), seção Período Contábil para Demonstrativos e para Planejamento Orçamentário Contábil.

Pode-se definir o **"Tipo de Período"** dentre duas opções:

- **Período Comparativo:** Nessa opção serão apresentadas as demonstrações contábeis de forma comparativa do período selecionado menos um ano. Deve-se configurar previamente os períodos contábeis.
- **Período:** Por meio dessa opção, serão exibidas as demonstrações contábeis do período selecionado.

**Observação:** Quando o campo Tipo de período estiver com a opção **"Período comparativo"** selecionada, será disponibilizado o campo **"Período anterior"** para se informar o período anterior a ser analisado.

**Nota:** O filtro da pesquisa do campo Período anterior trará apenas os períodos menores que o período principal selecionado.

Informe a **"Data período"** que os Demonstrativos Contábeis deverão abranger.

No campo **"Apresentação da empresa"** defina qual nomenclatura pertinente a empresa que está gerando o demonstrativo deverá ser exibida, tendo-se as seguintes opções:

- Razão Social;
- Nome Fantasia.

Por meio do campo **"Demonstração de valores"** determine como serão exibidos os valores no demonstrativo. Tem-se as seguintes possibilidades:

- Em Reais;
- Centenas de Reais;
- Milhares de Reais;
- Centenas de Milhares Reais;
- Milhões de Reais;
- Centenas de Milhões de Reais;
- Bilhões de Reais.

**Observação:** Quando a opção **"Em Reais"** estiver selecionada, será possível gerar os demonstrativos contábeis sem a divisão dos saldos, esta será a opção padrão do campo Demonstração de valores.

Por meio do campo **"Símbolos para valores negativos"** defina a forma como os valores negativos serão apresentados. Tem-se as seguintes opções:

- 100,00-
- 100,00D
- -100,00
- (100,00)
- ( 100,00)

No campo **"Formato data p/ impressão"** deve-se determinar qual o formato a ser utilizado para impressão das datas no demonstrativo; as alternativas são:

- DD/MM/AAAA
- MM/AAAA
- AAAA

Determine no campo **"Formato de Impressão"** o tipo de arquivo utilizado na visualização do demonstrativo, podendo ser:

- PDF;
- Excel (.xlsx).

Caso a marcação **"Imprimir logo da empresa"** esteja efetuada, será impressa a logo da empresa no lado direito superior do demonstrativo conforme layout estabelecido.

Quando a marcação **"Gerar Demonstrações somente para contas saldo?"** estiver realizada, o sistema gerará as demonstrações somente para as contas contábeis em que o saldo seja diferente de 0 no período da geração.

**Nota:** Quando estiver sendo gerado o Período comparativo, deve-se excluir apenas as contas em que nos 2 períodos o saldo é zero (Referência atual e Referência anterior).

Em relação à marcação **"Exibir Receitas positivas e Custos/Despesas negativos para DRE"** tem-se que, quando esta estiver habilitada, serão exibidos no DRE o sinal negativo para as Despesas e o sinal positivo para as Receitas.

**Observação:** Ao final, o resultado será demonstrado de acordo com o somatório das receitas e despesas, ou seja, caso haja lucro durante o período, o saldo deste deverá ser exibido com o sinal positivo, havendo prejuízo, será demonstrado o sinal negativo.

Quando a marcação **"Gerar DRE no layout do PGE da ECD?"** for realizada e for solicitada a geração do relatório DRE, este será impresso e deixará de seguir a hierarquia do campo **"Cód. Tipo Demonstrativo"** e passará a seguir o campo **"Número da Ordem"** existente na aba [DRE/DRA](https://ajuda.sankhya.com.br/hc/pt-br/articles/360045115913-Demonstrativos-ECD#abadredra) da tela [Demonstrativo ECD](https://ajuda.sankhya.com.br/hc/pt-br/articles/360045115913-Demonstrativos-ECD).

**Nota:** Caso a marcação esteja habilitada durante a geração do relatório, mas nenhuma das contas tenha Número da Ordem informado, a hierarquia seguirá como se a marcação estivesse desabilitada.

**Observação:** Se a marcação estiver habilitada durante a geração do relatório e alguma das contas possuir o Número da Ordem, as que não tiverem, ficarão em último no relatório.

Na seção Demonstrativos, tem-se as marcações que irão determinar os dados a serem gerados nos Demonstrativos Contábeis. Tem-se as seguintes opções:

- Todos Demonstrativos;
- Gerar capa;
- Gerar índice;
- Balanço Patrimonial - BP;
- Demonstrativos do resultado do exercício - DRE;
- Demonstrativos do resultado abrangente - DRA;
- Demonstrativo das mutações do patrimônio líquido - DMPL;
- Demonstrativos de lucros ou prejuízos acumulados - DPLA;
- Demonstrativos do fluxo de caixa - DFC;
- Nota explicativa - NE.

[[voltar ao topo]](https://ajuda.sankhya.com.br/hc/pt-br/articles/360044607714-Demonstrativos-Cont%C3%A1beis#top)

## Geração de Relatórios

Alguns campos e informações existentes nos Demonstrativos serão os mesmos para todos os relatórios, de modo que as definições sobre onde serão coletados estes dados serão os mesmos para todos os relatórios, conforme descrição abaixo:

#### Conta Contábil e o Cálculo do Saldo:

- Para buscar a conta contábil, saldo e valor dos lançamentos, a empresa da geração poderá utilizar o plano de contas de outra empresa;
- Você realizará a definição das contas, grau e ordenação das contas a serem apresentadas no demonstrativo na configuração da estrutura na tela [Demonstrativos ECD](https://ajuda.sankhya.com.br/hc/pt-br/articles/360045115913) para cada respectivo demonstrativo;
- A coluna Notas explicativas, também será apresentada conforme configuração realizada nesta tela;
- Os valores a serem apresentados serão dos saldos das contas contábeis, para a empresa e período selecionado;
- Para as contas que possuem quebra por Centro de Resultado e Projeto no saldo das contas, o sistema agrupa os valores, pois nos demonstrativos não é utilizado nenhum tipo de quebra por Centro de Resultado e/ou Projeto;
- Quando utilizada a data Anual com Comparativa, para a data Ano 0, o sistema irá buscar o saldo das contas para aquele período retroativo (Exemplo: 31/12/15);
- Na visualização do relatório, serão apresentados os valores no seguinte formato, 99.500;

[[voltar ao topo]](https://ajuda.sankhya.com.br/hc/pt-br/articles/360044607714-Demonstrativos-Cont%C3%A1beis#top)

## Premissa para geração dos demonstrativos

Antes da geração do Relatório, realizar a configuração de toda a estrutura de classificação dos grupos de contas contábeis, que deverá ser apresentada no relatório, por meio da rotina Demonstrativos ECD.

Teremos abaixo alguns modelos de impressão de Demonstrativos:

![Imagem 3: Teremos abaixo alguns modelos de impressão de Demonstrativos :](https://ajuda.sankhya.com.br/hc/article_attachments/5317730651031)

![Imagem 4: Teremos abaixo alguns modelos de impressão de Demonstrativos :](https://ajuda.sankhya.com.br/hc/article_attachments/5317737205271)

![Imagem 5: Teremos abaixo alguns modelos de impressão de Demonstrativos :](https://ajuda.sankhya.com.br/hc/article_attachments/5317785219735)

![acesse](https://ajuda.sankhya.com.br/hc/article_attachments/16023466299799) Acesse também:

[Conceitos - Demonstrativos Contábeis](https://ajuda.sankhya.com.br/hc/pt-br/articles/360044599114)

[[voltar ao topo]](https://ajuda.sankhya.com.br/hc/pt-br/articles/360044607714-Demonstrativos-Cont%C3%A1beis#top)

---
id: "42336754749335"
titulo: "Processo Seleção de Alíquota de IBS/CBS"
url: "https://ajuda.sankhya.com.br/hc/pt-br/articles/42336754749335-Processo-Sele%C3%A7%C3%A3o-de-Al%C3%ADquota-de-IBS-CBS"
trilha: "Manual do Produto > Fiscal e Contábil > Reforma Tributária > Configurações gerais"
atualizado_em: "2026-07-30T11:54:51Z"
---

# Processo Seleção de Alíquota de IBS/CBS

**Módulo:** Fiscal

---

**Você encontra neste artigo:**

| [O que é e para que serve](https://ajuda.sankhya.com.br/hc/pt-br/articles/42336754749335-Processo-Sele%C3%A7%C3%A3o-de-Al%C3%ADquota-de-IBS-CBS#oque) [Etapa 1 — Elegibilidade (filtro)](https://ajuda.sankhya.com.br/hc/pt-br/articles/42336754749335-Processo-Sele%C3%A7%C3%A3o-de-Al%C3%ADquota-de-IBS-CBS#etapa1) [Etapa 2 — Pontuação (hierarquia por peso)](https://ajuda.sankhya.com.br/hc/pt-br/articles/42336754749335-Processo-Sele%C3%A7%C3%A3o-de-Al%C3%ADquota-de-IBS-CBS#etapa2)    ↳ [Tabela de pesos](https://ajuda.sankhya.com.br/hc/pt-br/articles/42336754749335-Processo-Sele%C3%A7%C3%A3o-de-Al%C3%ADquota-de-IBS-CBS#tabela-pesos) | [Exemplos de aplicação](https://ajuda.sankhya.com.br/hc/pt-br/articles/42336754749335-Processo-Sele%C3%A7%C3%A3o-de-Al%C3%ADquota-de-IBS-CBS#exemplos)    ↳ [Finalidade da Operação restringindo uma alíquota](https://ajuda.sankhya.com.br/hc/pt-br/articles/42336754749335-Processo-Sele%C3%A7%C3%A3o-de-Al%C3%ADquota-de-IBS-CBS#exemplo-finalidade)    ↳ [Grupo IBS/CBS redirecionando a seleção](https://ajuda.sankhya.com.br/hc/pt-br/articles/42336754749335-Processo-Sele%C3%A7%C3%A3o-de-Al%C3%ADquota-de-IBS-CBS#exemplo-grupo) [Pontos de atenção](https://ajuda.sankhya.com.br/hc/pt-br/articles/42336754749335-Processo-Sele%C3%A7%C3%A3o-de-Al%C3%ADquota-de-IBS-CBS#pontos) [Perguntas frequentes](https://ajuda.sankhya.com.br/hc/pt-br/articles/42336754749335-Processo-Sele%C3%A7%C3%A3o-de-Al%C3%ADquota-de-IBS-CBS#faq) |
| --- | --- |

## O que é e para que serve

O **Processo Seleção de Alíquota de IBS/CBS** é a lógica que o Sankhya Om aplica para decidir, entre as alíquotas de IBS e CBS cadastradas, qual delas será efetivamente usada no cálculo de um documento fiscal. Ele entra em ação sempre que mais de uma alíquota cadastrada é compatível com o mesmo documento, definindo qual regra prevalece a partir de dois critérios: elegibilidade e pontuação. Este processo não cadastra alíquotas nem calcula os valores de IBS e CBS — ele apenas decide qual alíquota, entre as já cadastradas, entra no cálculo.

## Etapa 1 — Elegibilidade (filtro)

Cada campo preenchido no cadastro da alíquota funciona como uma condição obrigatória. Para a alíquota ser candidata, todo campo preenchido nela precisa coincidir com o valor do documento — campos deixados em branco funcionam como curinga e valem para qualquer documento.

Em outras palavras, para cada campo, a alíquota só permanece na disputa se o campo cadastrado nela for igual ao valor do documento, ou se estiver vazio.

**⚠️ Atenção**

Se uma alíquota tem um campo preenchido e o documento não traz aquele valor, essa alíquota é descartada logo na filtragem — ela nem chega a disputar pontuação com as demais.

[↑ Voltar ao início](https://ajuda.sankhya.com.br/hc/pt-br/articles/42336754749335-Processo-Sele%C3%A7%C3%A3o-de-Al%C3%ADquota-de-IBS-CBS#sumario)

## Etapa 2 — Pontuação (hierarquia por peso)

Entre as alíquotas que passaram pela filtragem da Etapa 1, o sistema soma um placar conforme os campos preenchidos e aplica a alíquota de maior pontuação total. Quanto mais específico o campo, maior o peso que ele carrega.

Em caso de empate na pontuação total, o sistema aplica a alíquota com a vigência (data de início) mais recente.

### Tabela de pesos

A ordem abaixo é a mesma apresentada nas telas de **Cadastro de Alíquotas IBS e CBS**, do maior para o menor peso.

| **Ordem** | **Campo** | **Peso** |
| --- | --- | --- |
| 1 | **Cidade** | 8192 |
| 2 | **UF** | 4096 |
| 3 | **Produto** | 2048 |
| 4 | **Grupo IBS/CBS** | 1024 |
| 5 | **NBS** | até 512 |
| 6 | **NCM** | até 256 |
| 7 | **Parceiro** | 128 |
| 8 | **Grupo de Parceiro** | 64 |
| 9 | **Empresa** | 32 |
| 10 | **Regime Tributário** | 16 |
| 11 | **CNAE** | até 8 |
| 12 | **Tipo de Operação (TOP)** | 4 |
| 13 | **Finalidade da Operação** | 2 |

**ℹ️ Nota**

Os campos **NBS**, **NCM** e **CNAE** pontuam por correspondência de prefixo: quanto mais dígitos do código baterem com o documento, maior a fração do peso obtida. Um código completo pontua mais do que um código parcial, como apenas a seção.

Repare que o campo **Finalidade da Operação** tem o menor peso da tabela. Isso significa que ele raramente decide um empate sozinho — sua função é refinar a seleção, não vencer a disputa por conta própria. Quem decide a seleção, na prática, são os campos do topo da tabela: **Cidade**, **UF**, **Produto** e **Grupo IBS/CBS**.

[↑ Voltar ao início](https://ajuda.sankhya.com.br/hc/pt-br/articles/42336754749335-Processo-Sele%C3%A7%C3%A3o-de-Al%C3%ADquota-de-IBS-CBS#sumario)

## Exemplos de aplicação

Os dois cenários abaixo mostram como a combinação de elegibilidade e pontuação se traduz na prática.

### Finalidade da Operação restringindo uma alíquota

Duas alíquotas cadastradas para o mesmo cenário, diferindo apenas no **CST** e na **Finalidade da Operação**:

- Alíquota A — **CST** específico, com o campo **Finalidade da Operação** preenchido
- Alíquota B — **CST** diferente, com **Finalidade da Operação** em branco

Pela Etapa 1, o preenchimento da finalidade na Alíquota A vira uma exigência: o documento precisa trazer exatamente aquela finalidade para que ela seja elegível.

Se o documento não informar a finalidade, a Alíquota A é descartada na filtragem, porque tem um campo preenchido que o documento não atende — a Alíquota B, com a finalidade em branco, continua elegível e é a selecionada.

Se o documento informar a mesma finalidade da Alíquota A, ela passa a ser elegível e, por ter um campo a mais correspondendo, ganha pontuação extra — tornando-se a selecionada.

Não há erro de cálculo nesse comportamento: a alíquota estava se autolimitando à finalidade configurada nela. Se uma alíquota deve valer para qualquer finalidade, deixe o campo **Finalidade da Operação** em branco no cadastro dela.

### Grupo IBS/CBS redirecionando a seleção

O campo **Grupo IBS/CBS** tem peso alto — 1024, o quarto maior da tabela. Quando você configura um **Grupo IBS/CBS** no cadastro do produto e preenche esse mesmo grupo em uma alíquota, essa alíquota passa a ser elegível para todos os produtos daquele grupo e, por causa do peso elevado, tende a ser preferida em relação a alíquotas mais genéricas que também sejam elegíveis para o mesmo documento.

**💡 Dica**

Esse mecanismo é útil para tratar um conjunto de produtos de uma vez, sem precisar cadastrar uma alíquota produto a produto. Configure o **Grupo IBS/CBS** em **Produtos › Impostos › Reforma Tributária**.

[↑ Voltar ao início](https://ajuda.sankhya.com.br/hc/pt-br/articles/42336754749335-Processo-Sele%C3%A7%C3%A3o-de-Al%C3%ADquota-de-IBS-CBS#sumario)

## Pontos de atenção

- Cadastre as alíquotas da mais específica para a mais geral: reduz a chance de uma alíquota genérica vencer por engano uma regra mais restrita.
- Só preencha um campo se ele for realmente uma exigência: cada campo preenchido funciona como um filtro. Se a alíquota deve valer para qualquer finalidade, parceiro ou cidade, deixe o campo correspondente em branco.
- Revise alíquotas com **Finalidade da Operação** preenchida: por ser o campo de menor peso, ela serve para refinar comportamentos específicos — se o documento não trouxer a finalidade, a alíquota some da disputa.
- Use o **Grupo IBS/CBS** com cautela: é uma ferramenta poderosa para tratar famílias de produtos de uma vez, mas seu peso alto pode se sobrepor a alíquotas mais genéricas cadastradas para os mesmos casos.

**💡 Dica**

Em caso de dúvida sobre qual alíquota será aplicada, simule o cenário com uma alíquota de vigência futura em ambiente de testes antes de publicar a mudança em produção.

[↑ Voltar ao início](https://ajuda.sankhya.com.br/hc/pt-br/articles/42336754749335-Processo-Sele%C3%A7%C3%A3o-de-Al%C3%ADquota-de-IBS-CBS#sumario)

## Perguntas frequentes

### Por que o sistema aplicou uma alíquota diferente da que eu esperava?

Provavelmente outra alíquota elegível teve pontuação maior, ou a que você esperava foi descartada na Etapa 1 por ter um campo preenchido que o documento não atendeu. Revise os campos preenchidos em cada alíquota candidata à luz da tabela de pesos.

### Deixar um campo em branco é a mesma coisa que preenchê-lo para valer em qualquer situação?

Sim. Um campo vazio funciona como curinga: a alíquota fica elegível independentemente do valor daquele campo no documento. Preencher o campo, por outro lado, transforma-o em uma exigência.

### Um campo de peso baixo, como Finalidade da Operação, pode decidir sozinho qual alíquota é aplicada?

Só se as demais alíquotas concorrentes estiverem empatadas nos campos de maior peso. Como a **Finalidade da Operação** vale apenas 2 pontos, ela normalmente atua como critério de refinamento — mas continua sendo uma exigência de elegibilidade quando preenchida.

### Se eu preencher o Grupo IBS/CBS na alíquota e no produto, essa alíquota sempre vai vencer as demais?

Ela passa a ser elegível para os produtos daquele grupo e tende a ser preferida por causa do peso alto (1024), mas ainda pode perder para uma alíquota que some mais pontos combinando outros campos, como **Cidade**, **UF** ou **Produto** preenchidos ao mesmo tempo.

### O que acontece em caso de empate na pontuação?

O sistema aplica a alíquota com a vigência (data de início) mais recente — o mesmo critério de desempate usado nas telas de **Cadastro de Alíquotas IBS e CBS**.

### Como os campos NBS, NCM e CNAE pontuam?

Por correspondência de prefixo: quanto mais dígitos do código do documento coincidirem com o código cadastrado na alíquota, maior a fração do peso obtida. Um código completo pontua mais do que um código parcial, como apenas a seção.

---
id: "10135864060183"
titulo: "Tela Painel de Auditoria de PIS/COFINS"
url: "https://ajuda.sankhya.com.br/hc/pt-br/articles/10135864060183-Tela-Painel-de-Auditoria-de-PIS-COFINS"
trilha: "Manual do Produto > Fiscal e Contábil > Fiscal > Escriturações e Declarações   > EFD Contribuições"
atualizado_em: "2026-09-30T11:14:49Z"
rotulos: ["Configuração", "Relatórios", "Movimentação Financeira", "Livros Fiscais", "Impostos", "br.com.sankhya.mgeliv.conferenciapiscofins", "Dashboard PIS/COFINS", "Consulta Detalhada", "Configurações Necessárias", "PIS/COFINS"]
---

# Tela Painel de Auditoria de PIS/COFINS

**Caminho de acesso:** Livros Fiscais › Relatórios

---

## O que é e para que serve

A **Tela Painel de Auditoria de PIS/COFINS** é um dashboard que apresenta todas as notas contidas nos Livros de ICMS e de ISS de cada cliente, para confirmar se estão com a tributação de PIS e COFINS correta.

O dashboard contém seis opções de consulta, que trazem todas as movimentações de **Entradas** e **Saídas** escrituradas nos Livros de ICMS/IPI e ISS, bem como as **Depreciações** e as **Aquisições de Ativos Imobilizados**.

![Imagem 1: O dashboard contém seis opções de consulta, que trazem todas as movimentações de Entradas e Saídas escrituradas nos…](https://ajuda.sankhya.com.br/hc/article_attachments/28587162785943)

## Botões da tela

A tela apresenta seis botões de consulta, descritos a seguir.

### Botões Entradas e Saídas

Os botões **Entradas** e **Saídas** apresentam todas as entradas e saídas escrituradas no Livro ICMS/IPI e no Livro de ISS, independentemente do **Código Fiscal de Operações e Prestações (CFOP)** e de operações com ou sem tributação de PIS/COFINS, permitindo conferir todos os documentos antes da apuração desses impostos.

**ℹ️ Nota**

Nesta tela não são exibidos os registros quando a Nota de Devolução possuir uma das seguintes características:

- a operação for de **Emissão Própria - Pessoa física**;
- o **Código de Situação Tributária (CST)** não estiver entre 60 e 66 e for igual ou maior que 50; ou
- o campo **Cód. Natureza (PIS/COFINS M410/M810)** da tela [Tipo de Operação - TOP](https://ajuda.sankhya.com.br/hc/pt-br/articles/360044603114-Tipos-de-Opera%C3%A7%C3%A3o-TOP), aba [Livro Fiscal](https://ajuda.sankhya.com.br/hc/pt-br/articles/360044603114-Tipos-de-Opera%C3%A7%C3%A3o-TOP#abalivrofiscal), estiver diferente de **12 - Devolução de Vendas Sujeitas à Incidência Não-Cumulativa**.

#### Botão Entradas

Exibe duas grades:

- Grade superior — Notas e Conhecimentos de Frete lançados pela **Central de Notas**.
- Grade inferior — Conhecimentos de Frete lançados pela **Movimentação Financeira**.

#### Botão Saídas

Apresenta apenas uma grade, com Notas e Conhecimentos de Frete lançados pela **Central de Notas**.

### Botão Depreciações

Apresenta as depreciações efetuadas, agrupadas pela descrição do bem, independentemente de estarem configuradas para cálculo dos impostos PIS e COFINS na depreciação.

### Botão Aquisições Imobilizados

Apresenta as aquisições efetuadas de bens que não estejam configuradas para cálculo dos impostos PIS e COFINS na depreciação.

### Botão Despesas Financeiras

Apresenta uma grade com as movimentações financeiras do tipo **Despesa** vinculadas às **Naturezas de Receitas e Despesas** configuradas com as informações para os cálculos dos impostos PIS e COFINS, permitindo conferir os documentos financeiros e os valores calculados.

### Botão Receitas Financeiras

Apresenta uma grade com as movimentações do tipo **Receita** vinculadas às **Naturezas de Receitas e Despesas** configuradas com informações para os cálculos dos impostos PIS e COFINS, permitindo conferir os documentos financeiros e os valores calculados.

**💡 Dica**

Todas as consultas deste painel podem ser obtidas a partir do [Monitor de Consultas](https://ajuda.sankhya.com.br/hc/pt-br/articles/360045108733-Monitor-de-Consultas). Com elas, você identifica todas as regras e restrições que determinam os resultados apresentados nas grades do dashboard.

## Regras para Receitas e Despesas Financeiras

É necessário possuir uma **Natureza de Receita e Despesa** vinculada aos financeiros, configurada para o cálculo do PIS/COFINS com CST menor que 50 e não nulo no caso de **Receitas**, e com CST maior que 50 e não nulo no caso de **Despesas** vinculadas aos financeiros.

Na **TOP Financeira**, a marcação **Usar Alíq. da Nat. do Rateio p/registro F100 do SPED PIS/COFINS?** não pode estar marcada.

Na **TOP**, mantenha a seguinte configuração:

- **Atualização de Livro ICMS** = **Não atualiza**
- **Atualização Livros de ISS** = **Não atualiza**
- **Tem PIS** = **marcada**
- **Tem COFINS** = **marcada**

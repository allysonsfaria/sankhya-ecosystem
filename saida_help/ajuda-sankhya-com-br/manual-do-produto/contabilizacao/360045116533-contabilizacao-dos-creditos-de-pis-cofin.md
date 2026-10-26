---
id: "360045116533"
titulo: "Contabilização dos Créditos de PIS/COFINS do Ativo Imobilizado"
url: "https://ajuda.sankhya.com.br/hc/pt-br/articles/360045116533-Contabiliza%C3%A7%C3%A3o-dos-Cr%C3%A9ditos-de-PIS-COFINS-do-Ativo-Imobilizado"
trilha: "Manual do Produto > Fiscal e Contábil > Contábil > Contabilização"
atualizado_em: "2026-07-29T16:01:35Z"
rotulos: ["AJUDA DO SKW", "manual", "Ativo", "COFINS", "PIS", "Imobilizado", "Créditos", "Crédito", "Impostos", "Contabilização", "Financeiro", "br.com.sankhya.ctbz.ctbzcredpiscofinsativoimob", "Contabilização dos Créditos de PIS/COFINS do Ativo Imobilizado manual", "Contabilização de Créditos de PIS/COFINS do Ativo Imobilizado", "PIS/COFINS", "Ativo Imobilizado"]
---

# Contabilização dos Créditos de PIS/COFINS do Ativo Imobilizado

```
![Módulo](https://ajuda.sankhya.com.br/hc/article_attachments/42314976019479) Módulo: Contabilização> Rotinas
```

---

Esta rotina é utilizada para realizar a contabilização dos créditos de PIS/COFINS referentes ao Ativo Imobilizado.

A tela principal é composta por duas abas: **Depreciação** e **Aquisição**.

### Aba Depreciação

![Imagem 2: Aba Depreciação](https://ajuda.sankhya.com.br/hc/article_attachments/5165238835735)

Sendo assim, para utilização desta rotina, deve-se obrigatoriamente preencher:

**Empresa movimento:** Informe a empresa da qual deseja contabilizar as movimentações de crédito de PIS/COFINS.

**Referência:** Determine o período que será utilizado como parâmetro para geração das movimentações de crédito.

**Empresa Contabilidade:** Preencha a empresa de contabilidade que o sistema irá utilizar para busca dos devidos dados contábeis.

**Número do lote:** Informe a numeração do lote correspondente a contabilização. O número aqui informado, deve estar compreendido entre os intervalos definidos nas [Preferências da Empresa de Contabilidade](https://ajuda.sankhya.com.br/hc/pt-br/articles/360044608114-Empresa), aba [Lançamentos](https://ajuda.sankhya.com.br/hc/pt-br/articles/360044608114-Empresa#abalanamentos), campos Início do número do lote manual e Fim do número do lote manual.

Determine por fim, através da marcação **"Usar Centro de Resultado?"** pela utilização desse aspecto na contabilização dos créditos. Esta marcação estará habilitada para uso, caso a marcação de mesma nomenclatura presente nas Preferências da Empresa de Contabilidade, aba Lançamentos, esteja realizada.

Quando o botão **"Contabilizar"** for acionado, irá executar a rotina de contabilização dos créditos de PIS/COFINS do ativo imobilizado e gerar o lote.

### Aba Aquisição

Esta aba é destinada à visualização, geração e acompanhamento das parcelas mensais de crédito de PIS/COFINS referentes à **aquisição dos bens** do Ativo Imobilizado.

**Funcionalidades e Exibição:**

- **Grade de Lançamentos:** Exibe a lista de todos os lançamentos a serem realizados no mês, incluindo:
  - Novas aquisições de bens.
  - Aquisições antigas ainda vigentes (parcelas mensais).
  - Estornos de bens baixados (se houver).
- **Discriminação na Grade:** Apresenta a discriminação individualizada de cada imposto (**PIS** e **COFINS**), com os respectivos **valores a contabilizar** e os **totais do mês**.

**Botão de Ação:**

- **Botão "Gerar Parcelas":**
  - Ao clicar, o sistema executa as seguintes ações:
    - Cria as contabilizações mensais para bens com status **Ativo**.
    - Gera os estornos necessários para bens com status **A Estornar**.
    - Atualiza as tabelas de controle com as parcelas do mês (crédito\_pis-cofins).

![Imagem 3: Atualiza as tabelas de controle com as parcelas do mês ( crédito_pis-cofins ).](https://ajuda.sankhya.com.br/hc/article_attachments/36061493657111)

---
id: "39281992629015"
titulo: "Como o sistema Sankhya processa descontos em vendas e orçamentos?"
url: "https://ajuda.sankhya.com.br/hc/pt-br/articles/39281992629015-Como-o-sistema-Sankhya-processa-descontos-em-vendas-e-or%C3%A7amentos"
trilha: "Melhores Práticas > Vendas"
atualizado_em: "2026-08-31T03:08:20Z"
rotulos: ["Produtos", "Configuração", "Descontos", "TOP", "Vendas", "Financeiro", "Artigo criado KCS", "CVE - KCS", "Orçamentos"]
---

# Como o sistema Sankhya processa descontos em vendas e orçamentos?

O sistema Sankhya possui **regras específicas** para o processamento de descontos em vendas e orçamentos. Compreender esses comportamentos é fundamental para evitar inconsistências nos valores e garantir a **correta aplicação de descontos promocionais**, descontos manuais e validações de limite.

Este artigo esclarece os principais comportamentos do sistema relacionados a descontos, incluindo **desconto duplo**, **recálculo automático de percentuais**, **alterações em devoluções** e **validações de limite**.

### Desconto duplo em produtos com promoção

O sistema **permite a aplicação de descontos adicionais** sobre produtos que já possuem desconto promocional cadastrado. Esse comportamento pode resultar em um **desconto duplo**, impactando o financeiro da empresa.

Para controlar essa situação e **disparar eventos de liberação** quando houver desconto acima do valor promocional, configure o parâmetro **"Validação de Desconto Máximo"** (VALDESCMAX) como **"Valida e Não Aceita"**.

Com essa configuração:

- Ao informar um desconto **superior ao valor promocional**, seja nos campos **"% Desconto"** ou **"Vlr. Desconto"** dos itens, ou no campo **"Percentual de Desconto"** do rodapé, o sistema realizará a validação.
- O sistema **disparará os eventos de liberação correspondentes** (evento 2 para desconto no rodapé, evento 25 para desconto nos itens).

**Observações importantes:**

- Para produtos **com desconto promocional**: qualquer desconto acima do valor promocional dispara o evento 25.
- Para produtos **sem desconto promocional**: o sistema valida o campo **"% Desconto Máximo"** no cadastro do produto:

  - Campo vazio ou zero: qualquer desconto dispara o evento 25.
  - Campo com 100: nenhum evento é disparado.
  - Campo com outro valor: dispara evento 25 quando exceder o percentual definido.

### Alteração de valor unitário e solicitação de liberação

Ao **reduzir o valor unitário** de um produto e aplicar um desconto adicional, o sistema **soma o desconto ao valor reduzido**, podendo solicitar liberação de limite (evento 25).

Esse comportamento é esperado quando o vendedor não possui permissão para informar valores menores.

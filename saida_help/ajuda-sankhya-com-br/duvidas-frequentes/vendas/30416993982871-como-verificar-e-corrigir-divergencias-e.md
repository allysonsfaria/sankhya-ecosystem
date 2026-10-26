---
id: "30416993982871"
titulo: "Como verificar e corrigir divergências entre movimentações de estoque e o saldo registrado no Sistema?"
url: "https://ajuda.sankhya.com.br/hc/pt-br/articles/30416993982871-Como-verificar-e-corrigir-diverg%C3%AAncias-entre-movimenta%C3%A7%C3%B5es-de-estoque-e-o-saldo-registrado-no-Sistema"
trilha: "Dúvidas Frequentes > Vendas"
atualizado_em: "2026-07-22T14:35:53Z"
rotulos: ["Produtos", "Configuração", "Relatórios", "WMS", "Estoque", "Passos para resolver", "Razão do erro", "Detalhe do erro", "corrigir divergências", "movimentações de estoque e o saldo registrado"]
---

# Como verificar e corrigir divergências entre movimentações de estoque e o saldo registrado no Sistema?

Manter a precisão do saldo de estoque é essencial para uma boa gestão logística e financeira. Entretanto, podem ocorrer divergências entre o saldo registrado no sistema e as movimentações de entrada e saída de produtos. Este artigo apresenta o procedimento adequado para identificar e corrigir essas inconsistências.

**![Imagem 1: SOLUÇÃO:](https://ajuda.sankhya.com.br/hc/article_attachments/30416993981463)SOLUÇÃO:**

Para ajustar possíveis divergências entre o saldo de estoque e as movimentações realizadas, siga os passos abaixo:

**![Imagem 2: Acesse a rotina de verificação de saldo de estoque (Configurações » Avançado » Verificação de Saldo de Estoque)](https://ajuda.sankhya.com.br/hc/article_attachments/30485524393367) Acesse a rotina de verificação de saldo de estoque** (Configurações » Avançado » Verificação de Saldo de Estoque)

**![Imagem 3: Configuração dos filtros](https://ajuda.sankhya.com.br/hc/article_attachments/30485548583447) Configuração dos filtros**

- - Selecione os filtros necessários, como empresa e produto;
  - O sistema comparará o saldo atual do estoque com as movimentações registradas.

**![Imagem 4: Verificação e ajuste das divergências](https://ajuda.sankhya.com.br/hc/article_attachments/30485524401431) Verificação e ajuste das divergências**

O sistema permite a análise e correção de divergências nos seguintes controles:

- Estoque
- Estoque de Terceiros
- Estoque sem Lançamento na Central
- Estoque de Terceiros sem Lançamento na Central
- Reserva

#### **(1)** Opções da Rotina

A rotina de verificação apresenta duas opções:

- **Verificar:** exibe uma prévia das diferenças encontradas entre as movimentações e o saldo de estoque dos produtos;
- **Corrigir:** ajusta as informações com base nas movimentações de entrada e saída do produto.

#### **(1)** Atenção: Processo Irreversível

**O processo de correção de saldo é irreversível.** Uma vez executado, o sistema ajusta permanentemente as informações na tabela **TGFEST**. Dessa forma, **recomenda-se utilizar a opção** **Corrigir** **apenas após uma análise cuidadosa das possíveis causas da divergência.**

###

#### **(1)** Conclusão

Manter a consistência do saldo de estoque é fundamental para evitar problemas na gestão empresarial. A verificação periódica utilizando a ferramenta indicada permite identificar e corrigir inconsistências, garantindo maior confiabilidade dos dados do sistema.

**![Imagem 5: CAUSA:](https://ajuda.sankhya.com.br/hc/article_attachments/30416993981591)CAUSA:**

As divergências encontradas podem ocorrer por diversos motivos, tais como:

- Intervenção direta na base de dados
- Desabilitação de objetos do sistema (triggers)
- Uso de objetos personalizados
- Falhas em integrações com outros sistemas
- Outros fatores técnicos e operacionais

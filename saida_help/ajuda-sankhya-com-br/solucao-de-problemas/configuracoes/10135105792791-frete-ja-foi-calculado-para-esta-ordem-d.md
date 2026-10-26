---
id: "10135105792791"
titulo: "Frete já foi calculado para esta ordem de carga"
url: "https://ajuda.sankhya.com.br/hc/pt-br/articles/10135105792791-Frete-j%C3%A1-foi-calculado-para-esta-ordem-de-carga"
trilha: "Solução de Problemas > Configurações"
atualizado_em: "2026-07-22T15:04:27Z"
rotulos: ["Ordem de Carga", "Configuração", "Usuário", "Transporte", "CORE_E04570", "Permissão Necessária para Recálculo de Frete", "Erro"]
---

# Frete já foi calculado para esta ordem de carga

**![Imagem 1: MENSAGEM:](https://ajuda.sankhya.com.br/hc/article_attachments/19067161096471) MENSAGEM:**

[CORE\_E04570] Frete já foi calculado para esta ordem de carga.

**![Imagem 2: SITUAÇÃO:](https://ajuda.sankhya.com.br/hc/article_attachments/19067161104535) SITUAÇÃO:**

Ao tentar salvar o lançamento a mensagem é apresentada.

**![Imagem 3: CAUSA:](https://ajuda.sankhya.com.br/hc/article_attachments/19067144848663) CAUSA:**

Ocorre quando usuário tenta recalcular o frete, mas o usuário não tem permissão para recalcular o frete.

**![Imagem 4: SOLUÇÃO:](https://ajuda.sankhya.com.br/hc/article_attachments/19067144853783) SOLUÇÃO:**

Caso deseje realizar o recálculo do frete, acesse o cadastro do **usuário** (Caminho de acesso à tela: Configurações » Controle de Acesso » Usuários) e marque o campo "Efetua recálculo de fretes".

![Imagem 5: Caso deseje realizar o recálculo do frete, acesse o cadastro do usuário (Caminho de acesso à tela: Configurações »…](https://ajuda.sankhya.com.br/hc/article_attachments/19067161121687)

**Esta marcação impacta em:**

- Efetuar recálculo do frete: se marcado permitirá ao usuário
- Recalcular frete pela tela **Cálculo de Frete** (Caminho de acesso à tela: Comercial » Rotinas » Ordem de Carga » Cálculo de Frete).
- Alterar "Ordem de Carga" ou recalcular frete pela tela de **Formação de Carga** (Caminho de acesso à tela: Comercial » Rotinas » Ordem de Carga » Formação de Carga).
- Alterar valor do frete ou "Ordem de Carga" na Central.
- Incluir ou retirar notas de uma "Ordem de Carga" quando o frete já tenha sido calculado e efetuar o recálculo novamente.
- Calcular Frete pelo histórico, quando frete por "Rota".

---
id: "37367431050903"
titulo: "Não foi possível resolver os metadados da entidade 'TipoTabela-pt_BR'"
url: "https://ajuda.sankhya.com.br/hc/pt-br/articles/37367431050903-N%C3%A3o-foi-poss%C3%ADvel-resolver-os-metadados-da-entidade-TipoTabela-pt-BR"
trilha: "Solução de Problemas > Pessoal+"
atualizado_em: "2026-07-29T13:22:23Z"
rotulos: ["Configuração", "Eventos", "Atualização", "Folha", "Plano de saúde", "confirmar a folha de pagamento", "Erro", "Tabelas de Faixas", "Metadados da entidade", "Erro ao confirmar Folha", "Somente informações númericas", "Código do evento"]
---

# Não foi possível resolver os metadados da entidade 'TipoTabela-pt_BR'

##### MENSAGEM:

Erro interno

Não foi possível resolver os metadados da entidade 'TipoTabela-pt\_BR'.

Erro ao carregar os metadados da entidade TipoTabela:

Erro interno: Metadados do campo 'TFPEVE->DTATUALIZACAO' não inicializados.

![Imagem 1: Erro interno: Metadados do campo 'TFPEVE->DTATUALIZACAO' não inicializados.](https://ajuda.sankhya.com.br/hc/article_attachments/37367461032471)

#####

##### SOLUÇÃO:

Para corrigir o problema, siga os passos abaixo:

**(1)** Acesse a tela [**''Plano de Saúde''**](https://ajuda.sankhya.com.br/hc/pt-br/articles/14865357667223-Plano-de-Sa%C3%BAde) (Pessoal+ » Cadastros » Plano de Saúde).

**(2)** Pesquise a **tabela de faixas** utilizada no cálculo da folha.

**(3)** Localize o campo onde é informado o ''**Código do evento''**.

**(4)** Verifique se o campo possui apenas **números**.

- Remova letras, espaços ou descrições do evento.

**(5)** Ajuste o campo para conter **somente o código numérico**:

##### Exemplo correto:

```
1005
```

#####

##### Exemplo incorreto:

```
1005 PLANO DE SAÚDE
```

**(5)** Salve as alterações.

**(6)** Volte para a folha de pagamento e tente **confirmar novamente**.

**CAUSA:**

O erro ocorre quando, na **tabela de faixas**, o campo que referencia o código do evento é **preenchido com informações que não são numéricas**, como letras, espaços ou descrições do evento (por exemplo: “1005 PLANO DE SAÚDE”).

![Imagem 2: O erro ocorre quando, na tabela de faixas , o campo que referencia o código do evento é preenchido com informações que…](https://ajuda.sankhya.com.br/hc/article_attachments/37479189137431)

Como o sistema aceita apenas valores numéricos nesse campo, a inclusão de qualquer caractere adicional gera falhas de validação, impedindo a confirmação da folha de pagamento ou a execução correta dos cálculos.

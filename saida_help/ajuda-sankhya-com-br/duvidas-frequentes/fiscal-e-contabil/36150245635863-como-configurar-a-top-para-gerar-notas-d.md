---
id: "36150245635863"
titulo: "Como configurar a TOP para Gerar Notas de Transferência no Livro Fiscal"
url: "https://ajuda.sankhya.com.br/hc/pt-br/articles/36150245635863-Como-configurar-a-TOP-para-Gerar-Notas-de-Transfer%C3%AAncia-no-Livro-Fiscal"
trilha: "Dúvidas Frequentes > Fiscal e Contábil"
atualizado_em: "2026-08-27T17:37:15Z"
rotulos: ["Configuração", "Fiscal", "Tipo de Operação", "Saída", "Nota Fiscal", "TOP", "Livro Fiscal", "Entrada", "Transferência", "Portal de Movimentação Interna", "Gerar Notas de Transferência"]
---

# Como configurar a TOP para Gerar Notas de Transferência no Livro Fiscal

No Sankhya, as movimentações de **transferência entre empresas** são compostas por **duas operações automáticas**:

- **Saída** da empresa de origem;
- **Entrada** automática na empresa de destino.

Para que essas notas sejam corretamente consideradas nos **livros fiscais**, é essencial que a **TOP utilizada esteja configurada para atualizar tanto o Livro de Saídas quanto o Livro de Entradas.**

## Como Configurar a TOP

**(1)** Acesse o [**''Portal de Movimentações Internas''**](https://ajuda.sankhya.com.br/hc/pt-br/articles/360045109593-Portal-de-Mov-Internas#oqueumatransferncia) (Comercial » Rotinas » Central de Mov. Internas) e identifique a TOP utilizada no processo de transferência.

![Imagem 1: (1) Acesse o ''Portal de Movimentações Internas'' (Comercial » Rotinas » Central de Mov. Internas) e identifique a TOP…](https://ajuda.sankhya.com.br/hc/article_attachments/36412780140695)![Imagem 2: (1) Acesse o ''Portal de Movimentações Internas'' (Comercial » Rotinas » Central de Mov. Internas) e identifique a TOP…](https://ajuda.sankhya.com.br/hc/article_attachments/36412785859863)

**(2)** Em seguida, acesse a tela [**''Tipos de Operação''**](https://ajuda.sankhya.com.br/hc/pt-br/articles/360044603114-Tipos-de-Opera%C3%A7%C3%A3o-TOP) (Comercial » Arquivos » Cadastros » Tipos de Operação (TOP)) localize e selecione aTOP utilizada no campo **''Cód. Tipo Operação''**.

**(3)** Posteriormente, na aba **''Livro Fiscal''**, configure o campo **''Atualização de Livro ICMS''**.

Essa configuração garante que o sistema registre automaticamente **tanto a saída quanto a entrada** da transferência no Livro Fiscal, sem necessidade de lançamentos manuais.

##### Exemplo – Nota de Transferência entre Empresas

##### Ao gerar uma transferência:

- A **saída** será registrada no livro fiscal da **Empresa 1**.
- A **entrada automática** será registrada no livro fiscal da **Empresa 2**.

No Livro Fiscal, uma das operações será apresentada com sinal negativo (–) para diferenciá-las, já que o campo de sequência é uma PK e não permite duplicidade.

![Imagem 3: No Livro Fiscal, uma das operações será apresentada com sinal negativo (–) para diferenciá-las, já que o campo de…](https://ajuda.sankhya.com.br/hc/article_attachments/36411812386071)

## Resultado

Ao realizar uma **movimentação de transferência** pelo [**''Portal de Movimentações Internas''**](https://ajuda.sankhya.com.br/hc/pt-br/articles/360045109593-Portal-de-Mov-Internas), o sistema:

- Gera automaticamente a **nota de saída** na empresa origem;
- Cria a **nota de entrada** na empresa destino;
- Atualiza ambas no **Livro Fiscal ICMS**, conforme a configuração da TOP.

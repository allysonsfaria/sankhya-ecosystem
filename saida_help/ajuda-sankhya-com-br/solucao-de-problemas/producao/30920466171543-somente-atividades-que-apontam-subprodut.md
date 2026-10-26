---
id: "30920466171543"
titulo: "Somente atividades que apontam subprodutos podem receber subprodutos definidos como 'Exige Apontamento'"
url: "https://ajuda.sankhya.com.br/hc/pt-br/articles/30920466171543-Somente-atividades-que-apontam-subprodutos-podem-receber-subprodutos-definidos-como-Exige-Apontamento"
trilha: "Solução de Problemas > Produção"
atualizado_em: "2026-07-22T14:34:21Z"
rotulos: ["Configuração", "Roteiro", "Processo Produtivo", "Produção", "Passos para resolver", "Razão do erro", "Detalhe do erro", "'Exige Apontamento'", "PROD_E00545", "Somente atividades que apontam subprodutos", "podem receber subprodutos", "Subproduto"]
---

# Somente atividades que apontam subprodutos podem receber subprodutos definidos como 'Exige Apontamento'

![Imagem 1: MENSAGEM:](https://ajuda.sankhya.com.br/hc/article_attachments/30920493237911) **MENSAGEM:**

[PROD\_E00545] Somente atividades que apontam subprodutos podem receber subprodutos definidos como 'Exige Apontamento'.

**![Imagem 2: SOLUÇÃO:](https://ajuda.sankhya.com.br/hc/article_attachments/30920493238935)SOLUÇÃO:**

Acesse a tela **"Processo produtivo - Nova"** (Produção » Cadastros » Processo Produtivo - Nova), pesquise pelo código do processo vinculado a composição do PA. Neste processo, clique no botão **"Roteiro"**, depois na aba **"Apontamento"**, em seguida, defina na marcação **"Aponta Subproduto"** uma opção para apontar o subproduto de acordo com o processo definido.

Pode-se escolher dentre as seguintes opções:

(1)** Aponta os Subprodutos da atividade:** poderão ser apontados os subprodutos produzidos na própria atividade. Conforme configuração, é possível ou não adicionar outros subprodutos.

(1)**Aponta os Subprodutos da OP:** aponta todos os subprodutos listados em todas as atividades ditas do caminho padrão. O sistema irá iniciar o apontamento com todos os subprodutos da Ordem de Produção, no entanto, conforme configuração, poderá ou não adicionar ou remover subprodutos.

**![Imagem 3: CAUSA:](https://ajuda.sankhya.com.br/hc/article_attachments/30920493240215)CAUSA:**

Ocorre quando tentamos incluir um Sub-Produto dentro da composição do produto, porém não foi definido dentro do roteiro na Tela Processo Produtivo que o processo aponta subproduto.

---
id: "360056267614"
titulo: "Não existe estoque para subtrair"
url: "https://ajuda.sankhya.com.br/hc/pt-br/articles/360056267614-N%C3%A3o-existe-estoque-para-subtrair"
trilha: "Solução de Problemas > Configurações"
atualizado_em: "2026-07-22T15:27:17Z"
rotulos: ["Configuração", "Nota Fiscal", "TOP", "Estoque", "#formatadoroger", "Não há estoque para subtrair", "Erro"]
---

# Não existe estoque para subtrair

**![Imagem 1: MENSAGEM :](https://ajuda.sankhya.com.br/hc/article_attachments/17269541738519) MENSAGEM**:

Não existe estoque para subtrair.

**![Imagem 2: SOLUÇÃO:](https://ajuda.sankhya.com.br/hc/article_attachments/17269541739799) SOLUÇÃO:**

Para correção, siga os passos abaixo:

**(1)** Para incidentes envolvendo **notas fiscais** nas Centrais de Nota:

![Imagem 3: Acesse o cadastro da TOP em: Comercial » Arquivo » Cadastros » Tipos de Operação - TOP Aba: "Estoque de Terceiros"…](https://ajuda.sankhya.com.br/hc/article_attachments/17269547844247) Acesse o cadastro da TOP em: Comercial » Arquivo » Cadastros » Tipos de Operação - TOP
Aba: **"Estoque de Terceiros"**
Campo: **"Estoque com/de Terceiros"**

**(1)** Veja as situações para a correta configuração:

- De acordo com a configuração desta deve utilizar uma TOP que realiza o processo 'inverso' da opção configurada.
- 1.1 - Se na TOP constar "Somar ao estoque próprio em poder de terceiros" a **Devolução** deve possuir a configuração "Subtrair do estoque próprio em poder de terceiros"
- 1.2 - Se na TOP constar "Somar ao estoque de terceiros em poder da empresa" a **Devolução** deve possuir a configuração "Subtrair do estoque de terceiros em poder da empresa"

**![Imagem 4: OBSERVAÇÃO:](https://ajuda.sankhya.com.br/hc/article_attachments/17269541747351) OBSERVAÇÃO:**

Os ajustes neste campo são históricos. Então, caso haja o documento (nota) deverá ser lançado novamente.

**(1)** Para incidentes envolvendo **nota de ajuste** de Inventário:

![Imagem 5: (1) Para incidentes envolvendo nota de ajuste de Inventário: Acesse as preferências da empresa em: Comercial »…](https://ajuda.sankhya.com.br/hc/article_attachments/17269547844247) Acesse as preferências da empresa em: Comercial » Preferências » Empresa
Aba: **"Estoque/Preço"**
Campo [**"Local específico para estoque de terceiros"**](https://ajuda.sankhya.com.br/hc/pt-br/articles/360045114893-Prefer%C3%AAncias-da-Empresa#abaestoquepreo): verifique o local especificado se está válido, se possui estoque e se é o correto, caso não seja considere efetuar o ajuste necessário.

**![Imagem 6: CAUSA:](https://ajuda.sankhya.com.br/hc/article_attachments/17269541747863) CAUSA:**

Ocorre quando a TOP de devolução consta para "Subtrair" **Estoque com/de Terceiros** 'diferente' da configuração da TOP do lançamento de origem.

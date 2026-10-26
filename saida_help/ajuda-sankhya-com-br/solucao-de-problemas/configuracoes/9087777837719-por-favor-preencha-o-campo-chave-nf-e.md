---
id: "9087777837719"
titulo: "\"Por favor preencha o campo \"Chave nf-e\""
url: "https://ajuda.sankhya.com.br/hc/pt-br/articles/9087777837719--Por-favor-preencha-o-campo-Chave-nf-e"
trilha: "Solução de Problemas > Configurações"
atualizado_em: "2026-07-31T03:49:10Z"
rotulos: ["Configuração", "Fiscal", "NF-e", "Configurador de layout da nota", "Chave NF-e", "não apagar", "Confirmação de Lançamento", "Erro", "Artigo atualizado KCS", "CVE - KCS"]
---

# "Por favor preencha o campo "Chave nf-e"

**MENSAGEM**:

"Por favor preencha o campo 'Chave NF-e'"

**SITUAÇÃO:**

Ao tentar salvar o cabeçalho de um documento na Central de Compra a mensagem é apresentada.

**SOLUÇÃO:**

Verifique na tela "Configurador de layout da nota" (Caminho de acesso: Comercial » Configuração » Configurador de Layout da Nota) se o campo "Chave NF-e" está flegado como obrigatório. Caso sim, é necessário o preenchimento do mesmo na central. Já, caso realmente não tenha necessidade de preenchimento do campo, a flag de "Obrigatório?" pode ser desmarcada.

![Por](https://ajuda.sankhya.com.br/hc/article_attachments/15790451762455)

**CAUSA:**

Ocorre quando o campo Chave NF-e está definido como obrigatório e não foi devidamente preenchido.

**OBSERVAÇÃO:** Para documentos fiscais de entrada, recomenda-se preencher a Chave NF-e conforme a nota do fornecedor. Além disso, se a TOP utilizada estiver configurada como NF-e de Terceiros e o modelo do documento for 55, 57, 65 ou 66 (NF-e/NFC-e), o preenchimento da Chave NF-e é obrigatório pelo sistema mesmo que a flag "Obrigatório?" esteja desmarcada no Configurador de Layout da Nota.

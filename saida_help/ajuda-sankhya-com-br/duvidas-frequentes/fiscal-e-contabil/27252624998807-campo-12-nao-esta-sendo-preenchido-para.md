---
id: "27252624998807"
titulo: "Campo 12 não está sendo preenchido para todos os itens no registro 0200, o que fazer?"
url: "https://ajuda.sankhya.com.br/hc/pt-br/articles/27252624998807-Campo-12-n%C3%A3o-est%C3%A1-sendo-preenchido-para-todos-os-itens-no-registro-0200-o-que-fazer"
trilha: "Dúvidas Frequentes > Fiscal e Contábil"
atualizado_em: "2026-07-22T14:39:52Z"
rotulos: ["Produtos", "Alíquotas", "Configuração", "Impostos", "EFD", "Estoque", "Passos para resolver", "Razão do erro", "Detalhe do erro", "Campo 12 não está sendo preenchido", "todos os itens no registro 0200", "Alíquota de ICMS", "registro 0200"]
---

# Campo 12 não está sendo preenchido para todos os itens no registro 0200, o que fazer?

No processo de geração do 0200, o sistema só puxa alíquota para os produtos que tiveram movimentação interna no mês em questão. 
Para os produtos que estão compondo a cópia de estoque, o campo código de alíquota não é preenchido.
Lembrando que o 0200 é registro de movimento de estoque não e tem a obrigatoriedade de informar a alíquota.

**Importante:** de acordo com o guia prático do EFD ICMS/IPI,  **o campo 12 se refere a Alíquota de ICMS.**

**Confira abaixo as regras do sistema para a geração do campo código de alíquota do registro 0200:**
 

![Imagem 1: Confira abaixo as regras do sistema para a geração do campo código de alíquota do registro 0200: A primeira verificação…](https://ajuda.sankhya.com.br/hc/article_attachments/29471652149399) A primeira verificação acontecerá da seguinte maneira:

- Valida no cadastro de produto, se na aba **"Alíquota interna de destino"** tem alguma informação;
- Caso não tenha, verificará na aba **"Impostos por empresa";**
- Se não tiver olhará para a aba **"0200 do EFD".**

![Imagem 2: Se nesse primeiro tópico o sistema não encontrar nenhuma alíquota informada, validará se existe uma alíquota de ICMS…](https://ajuda.sankhya.com.br/hc/article_attachments/29471652150679)  Se nesse primeiro tópico o sistema não encontrar nenhuma alíquota informada, validará se existe uma alíquota de ICMS criada cuja a exceção seja consumidor final;

![Imagem 3: Se nesse primeiro tópico o sistema não encontrar nenhuma alíquota informada, validará se existe uma alíquota de ICMS…](https://ajuda.sankhya.com.br/hc/article_attachments/29471652151447) Se não tiver, o sistema olhará para o estado da empresa que está gerando o sped e pegará o cadastro de alíquota de ICMS sem exceção, aquela que estiver informada no campo **"Alíquota interna"**

Então, a validação final para puxar a alíquota é a regra de ICMS sem exceção para o estado da empresa.
**No 0200, o campo alíquota só ficará branco caso em nenhum dos cadastros acima tenha a informação da alíquota e não tenha uma alíquota sem exceção configurada.**

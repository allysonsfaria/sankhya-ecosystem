---
id: "30922144640151"
titulo: "Erro: Token e Appkey não associados - Gateway"
url: "https://ajuda.sankhya.com.br/hc/pt-br/articles/30922144640151-Erro-Token-e-Appkey-n%C3%A3o-associados-Gateway"
trilha: "Solução de Problemas > Configurações"
atualizado_em: "2026-07-22T14:34:20Z"
rotulos: ["Configuração", "Segurança", "Parceiro", "API", "Login API", "Erro: Token e Appkey não associados - Gateway", "Erro"]
---

# Erro: Token e Appkey não associados - Gateway

**![Imagem 1: MENSAGEM:](https://ajuda.sankhya.com.br/hc/article_attachments/30922148172951) MENSAGEM:**

Token e Appkey não associados - Gateway

![Imagem 2: Token e Appkey não associados - Gateway](https://ajuda.sankhya.com.br/hc/article_attachments/30922144632215)

**![Imagem 3: SITUAÇÃO:](https://ajuda.sankhya.com.br/hc/article_attachments/31282928554775) SITUAÇÃO:**

O erro ocorre ao realizar o login na API.

**![Imagem 4: SOLUÇÃO:](https://ajuda.sankhya.com.br/hc/article_attachments/30922144633367) SOLUÇÃO:**

Ao realizar o login na API, é fundamental garantir que a Appkey e o Token utilizados estejam devidamente associados à mesma aplicação. Quando esses dados pertencem a aplicações diferentes, como uma Appkey vinculada à aplicação X e um Token correspondente à aplicação Y, ocorre falha na autenticação.

Assim, verifique se as credenciais fornecidas são consistentes e correspondem à aplicação correta

**Appkey:** chave que identifica o Parceiro Integrador. Essa chave é obtida na [Area do Desenvolvedor](https://login.sankhya.com.br/?redirect_to=https://areadev.sankhya.com.br/&application_id=23) em Gerenciar Soluções, onde pode-se obter a "Appkey" (para ambiente de Produção) e "Appkey para Sandbox" (Exclusiva para ambiente de Testes)

**Token:** chave que identifica o ambiente Sankhya. Deve ser observado que o Token de um ambiente de Produção é diferente de um Token para ambiente de Teste. O Token é gerado na tela [Configurações Gateway](https://ajuda.sankhya.com.br/hc/pt-br/articles/10007620733463-Configura%C3%A7%C3%B5es-Gateway)

**![Imagem 5: CAUSA:](https://ajuda.sankhya.com.br/hc/article_attachments/30922144635287) CAUSA:**

O erro ocorre quando há a utilização de um AppKey e um Token pertencentes a aplicações diferentes.

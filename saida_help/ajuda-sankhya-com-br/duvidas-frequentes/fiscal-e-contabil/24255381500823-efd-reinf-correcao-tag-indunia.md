---
id: "24255381500823"
titulo: "EFD REINF - Correção tag indUnia"
url: "https://ajuda.sankhya.com.br/hc/pt-br/articles/24255381500823-EFD-REINF-Corre%C3%A7%C3%A3o-tag-indUnia"
trilha: "Dúvidas Frequentes > Fiscal e Contábil"
atualizado_em: "2026-07-22T14:47:19Z"
rotulos: ["Configuração", "Empresa", "XML", "Impostos", "EFD", "EFD REINF - Correção tag indUnia"]
---

# EFD REINF - Correção tag indUnia

![Imagem 1: MENSAGEM:](https://ajuda.sankhya.com.br/hc/article_attachments/24255381488919) **MENSAGEM:**

A informação do indicativo de entidade vinculada a União (tag indUniao) é obrigatória e exclusiva se a natureza jurídica do declarante for igual a: [101-5,104-0,107-4,110-4, 113-9, 116-3, 121-0, 122-8, 125-2, 126-0, 128-7, 131-7, 201-1, 203-8]

**![Imagem 2: SOLUÇÃO:](https://ajuda.sankhya.com.br/hc/article_attachments/24255428682263)SOLUÇÃO:**

Na tela **"Empresa"** (Caminho de acesso: Comercial>Preferências) o campo **"Entidade Vinculada a União"** está com uma das opções abaixo

- **0 -** Não aplicável
- **1 -** Órgão da administração pública federal direta, autarquias e fundações da administração pública federal, empresas públicas, sociedades de economia mista, ou demais entidades em que a União detenha maioria do capital social sujeito a voto, recebe recursos do Tesouro Nacional e está obrigada a registrar a execução orçamentária no Siafi."

A tag indUniao é construída no xml de envio do evento R1000 da EFD-Reinf.
 
 
Assim, configure o campo Entidade Vinculada a União quando a Natureza Jurídica do declarante for igual a 101-5,104-0,107-4,110-4, 113-9, 116-3, 121-0, 122-8, 125-2, 126-0, 128-7, 201-1 ou 203-8. Caso contrário use a opção **"Não utiliza entidade vinculada a união",** com essa opção a tag indUniao não será construída no XML de envio da EFD-Reinf.
 
Para solução do erro retornado pelo ECAC "A informação do indicativo de entidade vinculada a União (tag indUniao) é obrigatória e exclusiva se a natureza jurídica do declarante for igual a: [101-5,104-0,107-4,110-4, 113-9, 116-3, 121-0, 122-8, 125-2, 126-0, 128-7, 131-7, 201-1, 203-8]", corrija a informação contida no campo **Entidade Vinculada a União**que se encontra na tela Empresa (Comercial>Preferências) aba EFD - Reinf

**![Imagem 3: CAUSA:](https://ajuda.sankhya.com.br/hc/article_attachments/24255428685335)CAUSA:**

Quando marcamos nas preferências da empresa, uma das opções 0 ou 1, o sistema cria a tag, onde há validação sobre a natureza. E, caso a natureza da empresa não aceite a referida tag, o erro será apresentado, sendo necessário usar a opção não utiliza entidade vinculada a união.

![Imagem 4: Quando marcamos nas preferências da empresa, uma das opções 0 ou 1, o sistema cria a tag, onde há validação sobre a…](https://ajuda.sankhya.com.br/hc/article_attachments/27714500023191)

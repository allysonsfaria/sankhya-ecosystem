---
id: "360044109974"
titulo: "CNPJ/CPF já existente para o parceiro: 'X'"
url: "https://ajuda.sankhya.com.br/hc/pt-br/articles/360044109974-CNPJ-CPF-j%C3%A1-existente-para-o-parceiro-X"
trilha: "Solução de Problemas > Configurações"
atualizado_em: "2026-08-12T12:17:19Z"
rotulos: ["Configuração", "Parceiro", "Preferências", "CORE_E05372", "Cadastro", "Problema de CNPJ/CPF Já Existente"]
---

# CNPJ/CPF já existente para o parceiro: 'X'

**![Imagem 1: MENSAGEM:](https://ajuda.sankhya.com.br/hc/article_attachments/16589217393815) MENSAGEM:**

[CORE\_E05372]: CNPJ/CPF já existente para o parceiro: 'X'.

**![Imagem 2: SOLUÇÃO:](https://ajuda.sankhya.com.br/hc/article_attachments/16589252888599) SOLUÇÃO:**

![Imagem 3: Na mensagem apresentada será descrito o código parceiro que já possui o CPF/CNPJ que está tentando vincular a esse novo…](https://ajuda.sankhya.com.br/hc/article_attachments/16589217404311) Na mensagem apresentada será descrito o código parceiro que já possui o CPF/CNPJ que está tentando vincular a esse novo cadastro. Caso seja válida a não permissão dessa informação repetida, verifique ambos os cadastros e ajuste o CNPJ/CPF do parceiro que encontra-se com a informação indevida.

![Imagem 4: Caso em seu processo cadastral, possa permitir o cadastro de mais de um parceiro com mesmo CNPJ/CPF, ative o parâmetro:](https://ajuda.sankhya.com.br/hc/article_attachments/16589252895639) Caso em seu processo cadastral, possa permitir o cadastro de mais de um parceiro com mesmo CNPJ/CPF, ative o parâmetro:

**(2)**Chave: **"ACEITACGCREPET"**: ligado, em: Configurações » Avançado » Preferências:

![Imagem 5: (2) Chave: "ACEITACGCREPET" : ligado, em: Configurações » Avançado » Preferências :](https://ajuda.sankhya.com.br/hc/article_attachments/15327885404567)

- Se estiver "Ligado", permitirá que o usuário cadastre mais de um parceiro com mesmo CNPJ/CPF. Se estiver "Desligado", só será permitido um parceiro por CNPJ/ CPF.
- Uma das regras do parâmetro **"ACEITACGCREPET**" é que, caso esteja desligado, será permitido cadastro de apenas um parceiro por CNPJ/ CPF, porém, mesmo que ele esteja desligado e o parceiro for cadastrado com uma cidade ou unidade federativa do exterior o sistema permitirá. Só não permite o cadastro de mais de um parceiro por CNPJ quando for do Brasil.

(2)** Chave 'ACEITAPRREPET' (Produtor Rural)**

- Validar repetição de CPF com classificação distinta para "Produtor rural" e "Consumidor Final. O comportamento do parâmetro valida a inclusão de vários produtores rurais com o mesmo CPF e IE distinto, não afetando a inclusão de um consumidor final com CPF já cadastrado. Sendo assim, no sistema poderemos ter 1 consumidor final e N produtores rurais.

**![Imagem 6: CAUSA:](https://ajuda.sankhya.com.br/hc/article_attachments/16589217411607) CAUSA:**

Ocorre quando se tenta efetuar um novo parceiro, no qual ja possui CPF/CNPJ e este é o mesmo de um parceiro já cadastrado no sistema, porem o parâmetro para aceitar CPF/CNPJ repetido esta desligado.

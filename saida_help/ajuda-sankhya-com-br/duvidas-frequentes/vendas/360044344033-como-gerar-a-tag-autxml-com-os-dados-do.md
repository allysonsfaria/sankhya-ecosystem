---
id: "360044344033"
titulo: "Como gerar a tag <autXML> com os dados do Contador no XML?"
url: "https://ajuda.sankhya.com.br/hc/pt-br/articles/360044344033-Como-gerar-a-tag-autXML-com-os-dados-do-Contador-no-XML"
trilha: "Dúvidas Frequentes > Vendas"
atualizado_em: "2026-07-22T15:58:21Z"
rotulos: ["Configuração", "Parceiro", "NF-e", "Contador", "XML", "Gerar a tag <autXML>", "Cadastro do contador", "Configurar Empresa"]
---

# Como gerar a tag <autXML> com os dados do Contador no XML?

![Imagem 1: Realize o cadastro do Contador na tela " Parceiros" (Caminho de acesso: Configurações » Cadastros » Parceiros).](https://ajuda.sankhya.com.br/hc/article_attachments/16975173685143) Realize o cadastro do Contador na tela **"Parceiros"** (Caminho de acesso: Configurações » Cadastros » Parceiros).

![Imagem 2: Realize o cadastro do Contador na tela " Parceiros" (Caminho de acesso: Configurações » Cadastros » Parceiros).](https://ajuda.sankhya.com.br/hc/article_attachments/13641234978199)

![Imagem 3: Acesse a tela " Empresa" (Caminho de acesso: Comercial » Preferências » Empresa) , selecione a empresa emitente e…](https://ajuda.sankhya.com.br/hc/article_attachments/16975173686935) Acesse a tela **"Empresa"** (Caminho de acesso: Comercial » Preferências » Empresa), selecione a empresa emitente e proceda com as configurações abaixo:

- **Aba 'Contador':**

![Imagem 4: Aba 'Contador':](https://ajuda.sankhya.com.br/hc/article_attachments/13641141297943)

- Informa-se no campo **"Cód. Parceiro"** o código criado para o "Contador" no cadastro de parceiros.
- Informe no campo **"Nome do Contador",** o nome do Contador.
- Indique o CPF do Contador no campo **"CPF"**.
- A marcação "**Enviar responsável contábil na NFe**" quando efetuada, desde que o CPF do contador esteja informado ou o parceiro informado possua CNPJ/CPF informado, será gerada no XML da nota, a tag <autXML>, contendo a tag filha <CNPJ> ou a tag <CPF>.

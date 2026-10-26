---
id: "39311437302423"
titulo: "Como referenciar a nota fiscal de origem em devoluções no Sankhya?"
url: "https://ajuda.sankhya.com.br/hc/pt-br/articles/39311437302423-Como-referenciar-a-nota-fiscal-de-origem-em-devolu%C3%A7%C3%B5es-no-Sankhya"
trilha: "Melhores Práticas > Configurações"
atualizado_em: "2026-08-24T18:40:28Z"
rotulos: ["Configuração", "NF-e", "XML", "TOP", "Devolução", "Artigo criado KCS", "Docs Eletrônicos - KCS"]
---

# Como referenciar a nota fiscal de origem em devoluções no Sankhya?

O Sankhya gera automaticamente o grupo **DFeReferenciado** no XML da NF-e de devolução quando todas as condições descritas abaixo são atendidas.

Para que o referenciamento seja realizado, é necessário que:

- A nota fiscal tenha a finalidade **Devolução de mercadoria** (**finNFe = 4**);
- O documento de origem seja uma **NF-e Modelo 55;**
- A TOP utilizada na devolução esteja configurada para buscar automaticamente a nota de origem;
- Não exista um documento fiscal informado manualmente no grupo **NFref** da nota.

### **(1)** Como configurar a TOP

Acesse **Comercial > Arquivo > Cadastros > Tipos de Operação (TOP)**.

Selecione a TOP utilizada para devolução.

Na aba **Validações**, marque a opção **Buscar NF de origem p/ referenciar na NF-e**.

Na aba **Livro Fiscal**, verifique as configurações:

- **Modelo de Documento:** **55 - Nota Fiscal Eletrônica**.
- **NF-e:** **Devolução**.

Salve as alterações.

### **(1)** Passo a passo para realizar a devolução:

**(1)** Acesse os **Portais (Vendas/Compras/Mov.Interna)**.

**(2)**  Selecione a nota que deseja devolver e clique no botão **"Devolv./Estor".**

**(3)**  Escolha a TOP de devolução (venda ou compra, conforme o caso).

**(4)** Clique em **Concluir**. O sistema direcionará você para a **Central de Notas**, onde será possível concluir a emissão da nota de devolução.

### **(1)** Quando o referenciamento não é gerado

O grupo **DFeReferenciado** não será incluído automaticamente no XML quando:

- A TOP não estiver configurada para buscar a nota de origem.
- O documento de origem não for uma **NF-e Modelo 55**.
- Existir um documento informado manualmente no grupo **NFref**.
- A nota não possuir finalidade **Devolução de mercadoria (finNFe = 4)**.

Nesses casos, será necessário corrigir a configuração ou informar o documento referenciado manualmente.

### **(1)** Informações incluídas no XML

Quando todas as condições forem atendidas, o sistema incluirá automaticamente no grupo **DFeReferenciado** do XML:

- A chave de acesso da nota fiscal de origem;
- O número do item correspondente na nota fiscal de origem.

Essas informações garantem o vínculo entre a nota de devolução e o documento fiscal original, conforme as regras da NF-e.

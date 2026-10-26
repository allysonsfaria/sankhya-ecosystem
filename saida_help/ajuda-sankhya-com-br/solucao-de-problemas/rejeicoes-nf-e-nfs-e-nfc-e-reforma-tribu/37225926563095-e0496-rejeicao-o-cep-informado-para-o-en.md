---
id: "37225926563095"
titulo: "E0496 Rejeição: O CEP informado para o endereço nacional do fornecedor não existe ou não pertence ao município do endereço do fornecedor."
url: "https://ajuda.sankhya.com.br/hc/pt-br/articles/37225926563095-E0496-Rejei%C3%A7%C3%A3o-O-CEP-informado-para-o-endere%C3%A7o-nacional-do-fornecedor-n%C3%A3o-existe-ou-n%C3%A3o-pertence-ao-munic%C3%ADpio-do-endere%C3%A7o-do-fornecedor"
trilha: "Solução de Problemas > Rejeições: NF-e / NFS-e / NFC-e - Reforma tributária "
atualizado_em: "2026-07-22T14:15:28Z"
rotulos: ["Configuração", "Empresa", "NF-e", "Cidades", "SEFAZ", "Erro", "CEP cadastrado para o fornecedor", "CEP incorreto ou não corresponde ao município", "CEP para endereço nacional do fornecedor não existe ao município", "Município cadastrado no sistema"]
---

# E0496 Rejeição: O CEP informado para o endereço nacional do fornecedor não existe ou não pertence ao município do endereço do fornecedor.

**MENSAGEM**

E0496 Rejeição: O CEP informado para o endereço nacional do fornecedor não existe ou não pertence ao município do endereço do fornecedor.

**SITUAÇÃO**

Ao emitir uma NF-e ou NFC-e, o documento foi **rejeitado pela SEFAZ** com a mensagem E0496, indicando que o **CEP cadastrado para o fornecedor** (emitente) está **incorreto ou não corresponde ao município** informado no endereço do cadastro.

**SOLUÇÃO**

**(1)** Acesse a tela [**"Empresas"**](https://ajuda.sankhya.com.br/hc/pt-br/articles/360045118293-Empresas) (Configurações » Cadastros » Empresas).

**(2)** Localize a **empresa emitente** da nota fiscal rejeitada.

**(3)** Na aba **"Endereço"**, verifique o conteúdo do campo **"CEP"**.

**(4)** Confira se o **CEP informado está correto** e se **corresponde ao município cadastrado** no sistema. Para isso:

- Acesse o site dos [**''Correios''**](https://buscacepinter.correios.com.br/app/endereco/index.php).
- Consulte o **CEP correto** usando o endereço completo da empresa.
- Verifique se o **município retornado** pela consulta corresponde ao **município cadastrado no sistema**.

**(5)** Caso o CEP esteja incorreto ou não corresponda ao município cadastrado, atualize o campo **“CEP”** com a informação válida obtida na consulta.

**(6)** Se necessário, clique no **ícone dos Correios** ao lado do campo ''**CEP''** para preencher automaticamente os campos de endereço.

**(7)** Após realizar as alterações, **salve** as informações no cadastro da empresa.

**(8)** Acesse a tela [**"Central de Vendas"**](https://ajuda.sankhya.com.br/hc/pt-br/articles/360044612414-Central-de-Vendas) (Comercial » Rotinas » Central de Vendas).

**(9)** Localize a nota fiscal rejeitada, redigite os dados do cabeçalho e gere um novo lote para transmissão.

**(10)** Se a nota continuar sendo rejeitada, **inutilize ou exclua a NF-e** rejeitada e refaça o **lançamento do documento fiscal**.

**CAUSA**

A rejeição ocorre quando o **CEP informado no cadastro do fornecedor** (emitente) **não existe na base dos Correios** ou **não pertence ao município** que foi cadastrado no endereço da empresa. A SEFAZ valida se o CEP corresponde ao município informado, e qualquer **divergência entre essas informações** resulta na rejeição do documento fiscal.

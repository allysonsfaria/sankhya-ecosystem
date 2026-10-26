---
id: "37224408355991"
titulo: "E0316 Rejeição: Código da lista NBS informado inexistente tabela de NBS do sistema."
url: "https://ajuda.sankhya.com.br/hc/pt-br/articles/37224408355991-E0316-Rejei%C3%A7%C3%A3o-C%C3%B3digo-da-lista-NBS-informado-inexistente-tabela-de-NBS-do-sistema"
trilha: "Solução de Problemas > Rejeições: NF-e / NFS-e / NFC-e - Reforma tributária "
atualizado_em: "2026-07-22T14:16:39Z"
rotulos: ["Configuração", "Fiscal", "Cidades", "Impostos", "NFS-e", "Erro", "Código NBS no JSON", "Código da lista NBS", "Código da lista NBS informado inexistente", "Código NBS informado", "Tabela oficial TLFNBS"]
---

# E0316 Rejeição: Código da lista NBS informado inexistente tabela de NBS do sistema.

**MENSAGEM**

E0316 Rejeição: Código da lista NBS informado inexistente tabela de NBS do sistema.

**SITUAÇÃO**

Ao gerar o lote de uma NFS-e, o sistema apresenta a mensagem de rejeição informando que o **código NBS** (Nomenclatura Brasileira de Serviços) cadastrado **não existe na tabela oficial** de NBS do sistema.

**SOLUÇÃO**

**(1)** Acesse a tela **"Serviço"** (Configurações » Cadastros » Produtos » Serviço).

**(2)** Localize o serviço que está sendo utilizado na NFS-e rejeitada.

**(3)** Na aba **"Impostos"**, verifique o campo **"Código NBS"**. Confirme se o código informado está correto e se **existe na tabela oficial TLFNBS**.

**(4)** Caso o código esteja incorreto ou inexistente:

- Consulte a **tabela oficial de NBS** para identificar o código correto correspondente ao serviço prestado.
- Atualize o campo **"Código NBS"** com o código válido.

**(5)** Verifique se a cidade está configurada para **enviar o Código NBS** no JSON.

**(6)** Acesse a tela [**"Cidades"**](https://ajuda.sankhya.com.br/hc/pt-br/articles/360045110913-Cidades) (Configurações » Cadastros » Endereços » Cidades).

**(7)** Confirme se o campo **"Enviar o Código NBS no JSON"** está ativado.

**(8)** Caso a cidade possua uma **máscara NBS** configurada, certifique-se de que o código NBS cadastrado está no formato correto exigido pela máscara.

**(9)** Salve as alterações realizadas no cadastro do serviço.

**(10)** Acesse a tela [**''Portal de Vendas''**](https://ajuda.sankhya.com.br/hc/pt-br/articles/360044612654-Portal-de-Vendas) (Comercial » Consulta » Portal de Vendas) e gere um novo lote de envio para a NFS-e.

**CAUSA**

A rejeição ocorre porque o **código NBS informado** no cadastro do serviço **não existe na tabela oficial TLFNBS** do sistema. Isso pode acontecer quando:

- O código foi digitado incorretamente.
- O código está desatualizado ou foi descontinuado.
- O código não corresponde à hierarquia válida da tabela NBS (por exemplo: 1, 1.1, 1.1.11).
- A cidade exige o envio do código NBS e o campo não foi preenchido ou está com valor inválido.

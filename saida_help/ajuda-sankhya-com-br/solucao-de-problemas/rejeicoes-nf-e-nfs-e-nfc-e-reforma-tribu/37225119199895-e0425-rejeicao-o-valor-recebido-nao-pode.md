---
id: "37225119199895"
titulo: "E0425 Rejeição: O valor recebido não pode ser menor que o valor do serviço informado na DPS."
url: "https://ajuda.sankhya.com.br/hc/pt-br/articles/37225119199895-E0425-Rejei%C3%A7%C3%A3o-O-valor-recebido-n%C3%A3o-pode-ser-menor-que-o-valor-do-servi%C3%A7o-informado-na-DPS"
trilha: "Solução de Problemas > Rejeições: NF-e / NFS-e / NFC-e - Reforma tributária "
atualizado_em: "2026-07-22T14:16:10Z"
rotulos: ["Central de Vendas", "Portal de Vendas", "SEFAZ", "Financeiro", "Passos para resolver", "Erro", "DPS (Declaração de Prestação de Serviços)", "Valor recebido não pode ser menor que o valor do serviço", "Valor recebido inferior ao valor total do serviço"]
---

# E0425 Rejeição: O valor recebido não pode ser menor que o valor do serviço informado na DPS.

**MENSAGEM**

E0425 Rejeição: O valor recebido não pode ser menor que o valor do serviço informado na DPS.

**SITUAÇÃO**

Ao emitir um **Documento de Prestação de Serviços (DPS)**, o usuário informou um **valor recebido inferior ao valor total do serviço** prestado. Esta inconsistência entre os valores fez com que o documento fosse **rejeitado pela Sefaz** com a mensagem de erro E0425.

**SOLUÇÃO**

**(1)** Acesse a tela **''Portal de Vendas''** (Comercial » Consulta » Portal de Vendas) e localize o documento que foi rejeitado.

- Ao selecionar e abrir o documento, o sistema direciona automaticamente para a tela **''Central de Vendas''** (Comercial » Rotinas » Central de Vendas).

**(2)** Na grade **''Rodapé''** verifique o campo **''Valor do Serviço''** informando o **valor total do serviço** no documento.

**(3)** Na aba **''Financeiro''**, verifique o campo **''Vlr. do Desdobramento''** e confira o **valor recebido** informado.

**(4)** Ajuste o **valor recebido** para que seja **igual ou maior** que o valor total do serviço prestado, considerando:

- Se o pagamento foi realizado integralmente, informe o **valor total do serviço**;
- Se houver **troco**, certifique-se de que o valor recebido seja maior que o valor do serviço e informe corretamente o valor do troco;
- Se o pagamento for **parcial**, verifique se este tipo de operação está permitido para DPS.

**(5)** Salve as alterações.

**(6)** Realize novamente a **transmissão do documento** para a Sefaz.

**CAUSA**

A rejeição ocorre porque a **Sefaz valida** que o valor recebido pelo serviço prestado **não pode ser inferior** ao valor total do serviço informado no Documento de Prestação de Serviços. Esta validação garante a **consistência fiscal** e evita que sejam emitidos documentos com valores de recebimento incompatíveis com o valor da prestação do serviço, o que poderia caracterizar **inconsistência tributária**.

---
id: "38436176135703"
titulo: "Credenciais fornecidas não são válidas para autenticar o provedor financeiro"
url: "https://ajuda.sankhya.com.br/hc/pt-br/articles/38436176135703-Credenciais-fornecidas-n%C3%A3o-s%C3%A3o-v%C3%A1lidas-para-autenticar-o-provedor-financeiro"
trilha: "Solução de Problemas > Financeiro"
atualizado_em: "2026-07-22T14:01:32Z"
rotulos: ["Configuração", "Parceiro", "Financeiro", "Passos para resolver", "Razão do erro", "Detalhe do erro", "Erro", "Ambiente de Produção", "Provedor financeiro", "Credenciais"]
---

# Credenciais fornecidas não são válidas para autenticar o provedor financeiro

![Imagem 1: MENSAGEM:](https://ajuda.sankhya.com.br/hc/article_attachments/38436176132631) **MENSAGEM:**

Credenciais fornecidas não são válidas para autenticar o provedor financeiro.

**![Imagem 2: SOLUÇÃO:](https://ajuda.sankhya.com.br/hc/article_attachments/38436152228503)SOLUÇÃO:**

**(1)** Verifique se as credenciais foram geradas no **ambiente de produção** do banco.

**(2)** Confirme se as credenciais estão **ativas e válidas**.

**(3)** Certifique-se de que:

- Foram geradas para a **mesma conta bancária** cadastrada no Sankhya;
- Estão vinculadas ao **mesmo CNPJ** informado no processo de credenciamento.

**(4)** Revise se não há erro de digitação ou inserção de espaços indevidos no cadastro das credenciais.

**![Imagem 3: CAUSA:](https://ajuda.sankhya.com.br/hc/article_attachments/38436152229015)CAUSA:**

Durante o processo de credenciamento, o sistema realiza uma validação automática das credenciais por meio de chamada via API diretamente na instituição bancária. Essa validação tem como objetivo assegurar que as credenciais existem na base do banco, estão ativas, encontram-se vinculadas à conta bancária informada e correspondem ao CNPJ cadastrado no processo.

O erro é apresentado quando uma ou mais das seguintes condições não são atendidas:

- Credenciais geradas em **ambiente de homologação**, e não em produção;
- **Client ID, Client Secret, Token ou Chave de API** inválidos;
- Credenciais expiradas ou inativas;
- Credenciais vinculadas a **outra conta bancária**;
- Credenciais associadas a **CNPJ diferente** do informado no credenciamento;
- Inserção incorreta das informações (espaços adicionais ou caracteres inválidos).

Para garantir a correta geração das credenciais, siga as orientações previstas nos **manuais específicos de cada instituição bancária**:

- [''Como obter as credenciais do **Banco do Brasil**''](https://ajuda.sankhya.com.br/hc/pt-br/articles/21042285386391-Como-obter-as-credenciais-do-Banco-do-Brasil)
- [''Como obter as credenciais do boleto híbrido do banco **Itaú**''](https://ajuda.sankhya.com.br/hc/pt-br/articles/21043102851223-Como-obter-as-credenciais-do-boleto-h%C3%ADbrido-do-banco-Ita%C3%BA)
- [''Como obter as credenciais do banco **Santander**''](https://ajuda.sankhya.com.br/hc/pt-br/articles/21069541531927-Como-obter-as-credenciais-do-banco-Santander)
- [''Como obter as credenciais do banco **Sicredi**''](https://ajuda.sankhya.com.br/hc/pt-br/articles/30801000122519-Como-obter-as-credenciais-do-banco-Sicredi)
- [''Como obter as credenciais do banco **Sicoob**''](https://ajuda.sankhya.com.br/hc/pt-br/articles/30820232298007-Como-obter-as-credenciais-do-banco-Sicoob)

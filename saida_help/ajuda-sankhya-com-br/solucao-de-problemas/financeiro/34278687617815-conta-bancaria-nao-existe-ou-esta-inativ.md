---
id: "34278687617815"
titulo: "Conta Bancária não existe ou está inativo ou não pode ser usado aqui"
url: "https://ajuda.sankhya.com.br/hc/pt-br/articles/34278687617815-Conta-Banc%C3%A1ria-n%C3%A3o-existe-ou-est%C3%A1-inativo-ou-n%C3%A3o-pode-ser-usado-aqui"
trilha: "Solução de Problemas > Financeiro"
atualizado_em: "2026-07-22T14:27:22Z"
rotulos: ["Configuração", "Contas", "Movimentação Financeira", "Financeiro", "CORE_E01315", "Passos para resolver", "Razão do erro", "Detalhe do erro", "não pode ser usada aqui", "Campo \"Ativa\"", "Conta bancária não existe", "está inativa", "Campo \"Exclusiva da Empresa\""]
---

# Conta Bancária não existe ou está inativo ou não pode ser usado aqui

**MENSAGEM**

[CORE\_E01315] Conta bancária não existe ou está inativa ou não pode ser usada aqui.

**SOLUÇÃO**

Antes de utilizar uma conta bancária, é necessário realizar algumas validações importantes para garantir que a conta esteja ativa, disponível para uso e corretamente configurada no sistema.:

**(1)**  Acesse a tela **"Contas"** (Configurações » Cadastros » Bancários » Contas).

    **O que verificar:**

- Campo **"Ativa"**: certifique-se de que a conta está marcada como ativa.
- Campo **"Exclusiva da Empresa"**: verifique se está marcada como exclusiva e, se necessário, ajuste conforme o contexto de uso.

![Imagem 1: Acesse a tela "Central de Certificações" (Comercial » Avançado » Certificações » Central de Certificações). O que…](https://ajuda.sankhya.com.br/hc/article_attachments/34278722141463) 
**(2)**  Acesse a tela **"Central de Certificações"** (Comercial » Avançado » Certificações » Central de Certificações).

    **O que verificar:**

- Se existe alguma **limitação de uso** da conta.
- Caso haja limitação, verifique se a regra está **vinculada ao usuário** que está tentando utilizar a conta.

![Imagem 2: Durante o processo de baixa, observe a sequência prioritária para sugestão de conta bancária pelo sistema:](https://ajuda.sankhya.com.br/hc/article_attachments/34278687609495) ![Imagem 3: Durante o processo de baixa, observe a sequência prioritária para sugestão de conta bancária pelo sistema:](https://ajuda.sankhya.com.br/hc/article_attachments/34278687610263) 
**(3)**  Durante o processo de baixa, observe a **sequência prioritária** para sugestão de conta bancária pelo sistema:

- **Conta informada na aba "Contas p/ Baixa"** no cadastro do usuário.
- **Conta definida no parâmetro** **CONTAPADRAO** ("Número da conta padrão na baixa").
- **Conta bancária informada no título** na movimentação financeira.
- **Conta marcada como "Exclusiva da Empresa"** no cadastro de contas bancárias.

**CAUSA**

A mensagem ocorre quando a conta bancária utilizada está inativa, não cadastrada ou possui restrições que impedem seu uso no processo.

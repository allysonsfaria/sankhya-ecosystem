---
id: "42427495738647"
titulo: "Como utilizar a integração com a Receita Federal?"
url: "https://ajuda.sankhya.com.br/hc/pt-br/articles/42427495738647-Como-utilizar-a-integra%C3%A7%C3%A3o-com-a-Receita-Federal"
trilha: "PLOOMES: Automação de propostas  > Clientes"
atualizado_em: "2026-08-10T18:04:39Z"
rotulos: ["sync_hc", "ploomes", "ploomes_5452388", "sync_hash_68a8de9c74e6"]
---

# Como utilizar a integração com a Receita Federal?

A integração com a Receita Federal permite preencher automaticamente os dados cadastrais de um cliente a partir do CNPJ informado.

É uma consulta pontual: os dados são buscados **somente no momento do clique** e os dados não são sincronizados automaticamente após salvar o registro.

## Onde acessar a integração?

A integração com a Receita Federal está disponível nas telas de criação e edição do cliente através do símbolo da Receita Federal no campo de **CNPJ** nativo.

![integração com receita federal](https://downloads.intercomcdn.com/i/o/kg4ewnrl/2048661576/78aa6299f0830e65eb0b47764889/image.png?expires=1786536000&signature=145ada0fd7c01d6c992836af241a5c07c8374b335716a17fd2e2475b43087003&req=diAjHs94nIRYX%2FMW3nq%2BgWOGQu0fbAYtr%2F%2FvXHeI70Hw8Om2QhTQ4oLTa5Tq%0AtpR9ZnYs5w%2BeR9KAyF1LWAZHLs8%3D%0A)

⚠️ Atenção:

- Não é possível realizar essa integração massivamente: é uma ativação manual no cadastro clicando no botão.
- Essa opção aparece apenas no campo nativo de "CNPJ", campos criados (dinâmicos) não possuem essa opção.

## Como funciona a integração?

- Com o formulário de criação/edição aberto, insira um **CNPJ válido** no campo.
- Clique no ícone **"Integrar CNPJ com a Receita Federal"**.
- O Ploomes envia uma requisição à Receita Federal e preenche automaticamente alguns campos do cadastro.

## Campos preenchidos automaticamente

- Nome
- Razão social
- Descrição CNAE
- Data de nascimento
- Código CNAE
- Atividades Secundárias
- Observações (nomes dos sócios e cargos)
- Endereço
- Número (endereço)
- Complemento
- Bairro
- Cidade
- Estado
- País
- CEP

Veja o exemplo abaixo, já preenchido:

[GIF animado: exemplo de integração](https://downloads.intercomcdn.com/i/o/kg4ewnrl/2048686039/95f5488349aba4e1380447e58efa/receita.gif?expires=1786536000&signature=cf4df9ed70b293daf745b4ee433afc14f9863f2f9c1ea2f7ed8d3a7b287436b8&req=diAjHs92m4FcUPMW3nq%2BgVebMjlXbdhmiG65tlOZVMLprlAI2Y%2FP2swbbFZ0%0AhfeKigCvTjhOFA5Qh4yJx7HkBGA%3D%0A)

## O que acontece após clicar em integrar?

Depois do preenchimento automático, o ícone muda para: **"Desativar integração de CNPJ com a Receita Federal"**

- Se clicar nessa opção, **todos os dados preenchidos pela integração serão desfeitos**.
- O botão só permanece ativo **enquanto o formulário estiver aberto**.

A integração **não é contínua**. Ou seja:

- Após salvar o cadastro, a integração **não permanece ativa**.
- Se abrir o registro novamente para editar, o ícone aparecerá desativado - mesmo que você tenha integrado antes.
- Caso precise atualizar os dados conforme a Receita Federal, basta **clicar novamente no botão** ao editar o cliente.

---

**Esse artigo te ajudou?** Deixe seu retorno abaixo para continuarmos sempre melhorando nossa base de conhecimento. 😊

**Ficou com alguma dúvida?** Não hesite em chamar o Suporte pelo chat da plataforma ou pelo e-mail [suporte@ploomes.com](mailto:suporte@ploomes.com).

---
id: "14467020135703"
titulo: "Componentes 'XXXXXX' deve ser informada"
url: "https://ajuda.sankhya.com.br/hc/pt-br/articles/14467020135703-Componentes-XXXXXX-deve-ser-informada"
trilha: "Solução de Problemas > Vendas"
atualizado_em: "2026-07-22T14:58:40Z"
rotulos: ["DUVIDANF", "Produtos", "Configuração", "NF-e", "CORE_E04011", "Validação obrigatória de componentes não correspondente", "Falta informar componentes", "Verificar configurações na aba Componentes", "Erro"]
---

# Componentes 'XXXXXX' deve ser informada

**![Imagem 1: MENSAGEM:](https://ajuda.sankhya.com.br/hc/article_attachments/16859181558679) MENSAGEM:**

[CORE\_E04011]: Componentes 'XXXXXX' deve ser informada.

**![Imagem 2: SOLUÇÃO:](https://ajuda.sankhya.com.br/hc/article_attachments/16859168656407)SOLUÇÃO:**

Acesse a aba **"Componentes",** no **[cadastro de Produtos](https://ajuda.sankhya.com.br/hc/pt-br/articles/360045112113-Cadastro-de-Produtos-#abacomponentes)** (Caminho de acesso: Configurações » Cadastros » Produtos) verifique a configuração do campo abaixo:

A **"Validação de Componentes"**se dará da seguinte forma:

- **Obrigatório:** a quantidade de componentes na Nota poderá ser maior ou igual a informada nesta aba;
- **Opcional:** o sistema não fará a validação dos componentes;
- **Qtd Iguais:** a quantidade de componentes desta aba tem que ser igual a quantidade de componentes que tiver na nota. Ou seja, se aqui o componente Arroz tiver 5 kg, então na nota tem que haver para este componente (Arroz) exatamente 5 kg.

![Imagem 3: Qtd Iguais: a quantidade de componentes desta aba tem que ser igual a quantidade de componentes que tiver na nota. Ou…](https://ajuda.sankhya.com.br/hc/article_attachments/14466924522647)

**![Imagem 4: CAUSA:](https://ajuda.sankhya.com.br/hc/article_attachments/16859181562007)CAUSA:**

Ocorre quando o campo Validação de componentes está definido como obrigatório e a quantidade informada no lançamento não é igual ao definido na aba Componentes.

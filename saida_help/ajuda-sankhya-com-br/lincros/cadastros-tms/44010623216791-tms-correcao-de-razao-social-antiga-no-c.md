---
id: "44010623216791"
titulo: "[TMS] - Correção de Razão Social Antiga no Cadastro de Destinatário"
url: "https://ajuda.sankhya.com.br/hc/pt-br/articles/44010623216791--TMS-Corre%C3%A7%C3%A3o-de-Raz%C3%A3o-Social-Antiga-no-Cadastro-de-Destinat%C3%A1rio"
trilha: "Lincros > TMS > Cadastros - TMS"
atualizado_em: "2026-10-05T18:42:06Z"
rotulos: ["sync_hc", "lincros", "lincros_13432459", "sync_hash_28f03004d6c2"]
---

# [TMS] - Correção de Razão Social Antiga no Cadastro de Destinatário

## Visão Geral

Quando o TMS exibe a razão social antiga de um destinatário — diferente da que consta na nota fiscal (NF) —, o motivo é que o cadastro da **Pessoa** (destinatário) no sistema ainda não foi atualizado com os novos dados. A identidade de um destinatário no TMS é definida pelo **CNPJ completo (14 dígitos)**, e cada CNPJ possui seu próprio cadastro de razão social e nome fantasia.

## Passo a Passo

### 1. Acessar o cadastro do destinatário

- No menu, acesse **Operacional > Documentos de despacho > Notas fiscais**.
- Localize a nota fiscal desejada e clique diretamente no campo **Destinatário** dentro do documento para abrir o cadastro.

![Imagem 1: Localize a nota fiscal desejada e clique diretamente no campo Destinatário dentro do documento para abrir o cadastro.](https://ajuda.sankhya.com.br/hc/article_attachments/44010619591575)

### 2. Atualizar os dados cadastrais

- Dentro do cadastro do destinatário, localize os campos **Razão Social** e **Fantasia**.
- Atualize os campos com as informações corretas e vigentes.
- Clique em **Salvar** para confirmar a alteração.

![Imagem 2: Clique em Salvar para confirmar a alteração.](https://ajuda.sankhya.com.br/hc/article_attachments/44010631457559)

### 3. Validar a atualização

- Após salvar, as próximas notas fiscais emitidas para esse destinatário passarão a exibir a razão social atualizada.
- Caso o problema persista, é possível que existam **dois cadastros distintos** para o mesmo destinatário com CNPJs diferentes (por exemplo, filiais com CNPJs /0001, /0002 etc.). No TMS, cada CNPJ completo representa uma entidade independente — verifique se a nota fiscal está vinculada ao CNPJ correto e repita a correção no cadastro correspondente.

## ⚠️ Informações Importantes

- A alteração da razão social **não afeta notas fiscais já emitidas** anteriormente — aplica-se apenas às emissões futuras.
- O campo **Razão Social** deve corresponder exatamente ao nome registrado na Receita Federal para o CNPJ em questão, evitando inconsistências fiscais.
- Em caso de dúvida sobre qual dado utilizar, consulte o [Comprovante de Inscrição no CNPJ](https://solucoes.receita.fazenda.gov.br/Servicos/cnpjreva/Cnpjreva_Solicitacao.asp) no site da Receita Federal.
- Se o destinatário foi criado automaticamente via integração sem nome (exibindo "DESCONHECIDO"), o cadastro precisa ser completado manualmente seguindo este mesmo procedimento.

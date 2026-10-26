---
id: "44013443676567"
titulo: "[TMS] - Erro de Integração de Embarques/Ordem de Coleta com o Tracking: \"Unidade sem código do depósito do Tracking\""
url: "https://ajuda.sankhya.com.br/hc/pt-br/articles/44013443676567--TMS-Erro-de-Integra%C3%A7%C3%A3o-de-Embarques-Ordem-de-Coleta-com-o-Tracking-Unidade-sem-c%C3%B3digo-do-dep%C3%B3sito-do-Tracking"
trilha: "Lincros > TMS > Cadastros - TMS"
atualizado_em: "2026-10-05T19:57:31Z"
rotulos: ["sync_hc", "lincros", "sync_hash_973d1e09bd9e", "lincros_13432504"]
---

# [TMS] - Erro de Integração de Embarques/Ordem de Coleta com o Tracking: "Unidade sem código do depósito do Tracking"

## 1. Problema Relatado pelo Cliente:

O cliente informou que está exibindo a mensagem de erro "Unidade sem código de depósito do Tracking", mesmo com a unidade cadastrada em ambas as plataformas. O erro ocorre durante a tentativa de integração de Embarque/Ordem de Coleta do TMS ao Tracking e impede a continuidade do processo integração do embarque ao Tracking.

## 2. Passo a Passo para Resolver o Problema:

Para resolver o erro de integração mencionado, siga os seguintes passos:

## Passo 1: Verificar o Cadastro da Unidade no Tracking

- A unidade deve estar devidamente cadastrada no sistema de Tracking. Confirme se todos os dados necessários estão presentes e corretos no cadastro da Unidade de Negócio.**[Tracking] Menu > Cadastros > Unidade de Negócio**

## Passo 2: Verificar o Cadastro de Pessoa no TMS da Unidade

- Toda unidade no TMS é vinculada a um cadastro de pessoa, que deve conter dados indispensáveis para garantir a correta integração com o Tracking.

  - No cadastro da pessoas (**Menu > Cadastros Gerais > Pessoas > Cadastro > Filtrar pelo CNPJ da Unidade**), verifique se os seguintes campos estão preenchidos, caso não estejam preencher conforme:

    - Em **Informações da pessoa:**adicione o edite os dados:

      - **GE\_CODEMPRESA**: Código da Unidade no Tracking.
      - **GE\_DEPOSITO**: Nome da Unidade no Tracking.

![Imagem 1: GE_DEPOSITO : Nome da Unidade no Tracking.](https://ajuda.sankhya.com.br/hc/article_attachments/44013431008791)

## Passo 3: Confirmação e Validação

- Após os ajustes, confirme se o processo foi concluído com sucesso e sem a mensagem de erro. Caso o problema persista, revise novamente as informações de cadastro e, se necessário, entre em contato com o suporte técnico para verificar possíveis inconsistências no sistema.

---

---
id: "44012718714647"
titulo: "[TMS] - Como Alterar a Transportadora no Cadastro do Embarque Sem Desvincular Documentos e Pré-Conhecimentos"
url: "https://ajuda.sankhya.com.br/hc/pt-br/articles/44012718714647--TMS-Como-Alterar-a-Transportadora-no-Cadastro-do-Embarque-Sem-Desvincular-Documentos-e-Pr%C3%A9-Conhecimentos"
trilha: "Lincros > TMS > Operacional - TMS"
atualizado_em: "2026-10-05T19:37:39Z"
rotulos: ["sync_hc", "lincros", "lincros_13433285", "sync_hash_e10a36ba31e9"]
---

# [TMS] - Como Alterar a Transportadora no Cadastro do Embarque Sem Desvincular Documentos e Pré-Conhecimentos

## Problema Relatado pelo Cliente

O cliente informou que ao alterar a transportadora na aba de cadastro de embarque, o sistema está desvinculando os documentos e pré-conhecimentos que estavam relacionados ao embarque, o que gera um problema de integridade de dados. O cliente solicita que, ao realizar a alteração, esses documentos e pré-conhecimentos permaneçam vinculados à nova transportadora.

---

## Passo a Passo para Resolver o Problema

Para resolver essa questão, você pode seguir um dos dois procedimentos, dependendo da existência de uma tabela associada à transportadora.

- ## Caso a transportadora tenha uma tabela associada:

1. Acesse o embarque no qual deseja alterar a transportadora em Operacional > Cargas > Embarques.
2. Na aba "Tabelas", selecione a tabela da transportadora desejada.
3. Após selecionar a tabela, clique em "Salvar" para confirmar a alteração.

Com este procedimento, a transportadora será alterada sem que os documentos e pré-conhecimentos sejam desvinculados.

- ## Caso a transportadora não tenha uma tabela associada:

1. Acesse o embarque no qual deseja alterar a transportadora em Operacional > Cargas > Embarques.
2. Na aba "Cadastros", remova a transportadora e a filial, deixando ambos os campos em branco.
3. Salve o embarque sem a transportadora e sem a filial.
4. Após salvar, verifique que os pré-conhecimentos permanecem vinculados ao embarque.
5. Informe a nova transportadora e a filial desejada.
6. Clique em "Salvar" para confirmar a alteração.

Esse procedimento garante que a transportadora do embarque seja alterada sem afetar os pré-conhecimentos vinculados ao embarque.

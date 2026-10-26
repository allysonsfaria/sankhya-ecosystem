---
id: "42950723994391"
titulo: "Erro de login \"certificate_expired\" causado por ambiente cadastrado incorretamente como SANDBOX Sintoma"
url: "https://ajuda.sankhya.com.br/hc/pt-br/articles/42950723994391-Erro-de-login-certificate-expired-causado-por-ambiente-cadastrado-incorretamente-como-SANDBOX-Sintoma"
trilha: "VIDYA: Vendas externas, televendas e entregas > Central de ajuda > Configurações"
atualizado_em: "2026-08-24T17:02:07Z"
rotulos: ["sync_hc", "vidya", "sync_hash_a2003d667fc6", "vidya_599863"]
---

# Erro de login "certificate_expired" causado por ambiente cadastrado incorretamente como SANDBOX Sintoma

## Imagem 1: SintomaImagem 2: SintomaSintoma

O cliente não consegue fazer login no aplicativo e recebe a seguinte mensagem de erro:

```
Erro ao fazer login
(certificate_expired) PKIX path validation failed:
java.security.cert.CertPathValidatorException: validity check failed
```

O erro ocorre na tela de login, impedindo completamente o acesso ao sistema.

## Causa raiz

O erro de certificado é apenas o **sintoma visível**. A causa real identificada foi um **erro de configuração de ambiente na AWS**:

- O backend do cliente estava marcado (tag) como **SANDBOX**, quando na verdade se tratava de um ambiente de **produção** em uso ativo pelo cliente.
- Como o ambiente estava sinalizado como SANDBOX, ele foi tratado pelas rotinas/processos internos como um ambiente de teste.
- Em algum momento, o ambiente de SANDBOX foi derrubado (processo normal para ambientes de teste), e por estar com a tag incorreta, o backend de produção do cliente caiu junto.
- Com o backend fora do ar, o certificado associado a ele deixou de ser validado corretamente, gerando a falha de `certificate_expired` / `PKIX path validation failed` no momento do login.

Em resumo: **o ambiente nunca deveria ter sido criado com a tag SANDBOX**, pois era, na prática, um ambiente de produção.

## Impacto

- Clientes com backend afetado ficaram completamente **sem acesso ao sistema**.
- O erro aparece de forma genérica (relacionado a certificado), o que pode dificultar o diagnóstico se a causa raiz (tag incorreta) não for verificada primeiro.

## Como diagnosticar

1. Verificar se o cliente relatou o erro `certificate_expired` / `PKIX path validation failed` na tela de login.
2. Localizar o backend do cliente na AWS.
3. Conferir a **tag do ambiente** associada ao backend (SANDBOX vs. PRODUÇÃO).
4. Confirmar se o ambiente está de fato em uso como produção pelo cliente, mesmo estando marcado como SANDBOX.
5. Verificar se o ambiente de SANDBOX foi encerrado/derrubado recentemente (rotina de limpeza de ambientes de teste), o que explicaria a queda simultânea do backend do cliente.

## Solução

A correção definitiva é **recriar o ambiente com a tag correta**:

1. Excluir o ambiente atualmente configurado como SANDBOX.
2. Recriar o ambiente do zero, desta vez com a tag de **PRODUÇÃO**.
3. Reconfigurar/revalidar o acesso do cliente ao novo ambiente.
4. Validar o login do cliente após a recriação, garantindo que o certificado seja validado corretamente.

> Não é uma correção apenas de certificado — a causa raiz é a classificação incorreta do ambiente, então a tag precisa ser corrigida para evitar recorrência.

## Prevenção

Para evitar que o problema se repita em outros clientes:

- Ao provisionar um novo backend na AWS, **sempre confirmar com o time responsável** se o ambiente é de fato SANDBOX (teste) ou PRODUÇÃO antes de aplicar a tag.
- Incluir uma etapa de **checagem/validação da tag do ambiente** no processo de criação de novos backends de clientes.
- Considerar auditoria periódica dos ambientes marcados como SANDBOX na AWS, verificando se algum deles está, na prática, sendo usado como produção.
- Avaliar alertas automáticos para o caso de ambientes SANDBOX apresentarem tráfego/uso compatível com produção (indício de classificação incorreta).

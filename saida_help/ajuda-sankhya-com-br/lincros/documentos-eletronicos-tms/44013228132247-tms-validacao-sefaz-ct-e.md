---
id: "44013228132247"
titulo: "[TMS] - Validação SEFAZ: CT-e"
url: "https://ajuda.sankhya.com.br/hc/pt-br/articles/44013228132247--TMS-Valida%C3%A7%C3%A3o-SEFAZ-CT-e"
trilha: "Lincros > TMS > Documentos Eletrônicos - TMS"
atualizado_em: "2026-10-05T19:50:59Z"
rotulos: ["sync_hc", "lincros", "lincros_13432829", "sync_hash_85aa640189d6"]
---

# [TMS] - Validação SEFAZ: CT-e

**Menu**: Documentos eletrônicos > CT-es

**Objetivo**: Apresentar as regras para que haja a validação de CT-es no portal SEFAZ de forma automática.

## Considerações

- Para que a validação seja realizada de forma automática, é necessário inicialmente ter o certificado digital válido configurado no sistema;
- É necessário ter cadastrado o processo 'transpobrasil.ValidacaoCTeJob' ou  ter o parâmetro 'ValidarCte = true' nos parâmetros da empresa;
- Por padrão, a validação no portal SEFAZ é feita somente nas 24h posteriores a emissão do CT-e. Após esse tempo, não há mais essa validação no portal. Se o cliente desejar aumentar esse tempo, é necessário realizar o cadastro do parâmetro em parâmetros por empresa (periodoMaximoEmissaoCteEmHorasPorUF);

## Validar se há certificado digital

Para verificar se o certificado digital está válido, acessar o menu: Cadastros Gerais > Configurações de empresa > Gerais > Certificado Digital

## Cadastramento do JOB

Para cadastrar o job, acessar o menu: Sistema > Agendamento de processos. Se o cliente for validar por JOB, precisa cadastrar o JOB “com.transpobrasil.ValidacaoCTeJob”.

## Parâmetros da Empresa

Para cadastrar o parâmetro 'ValidarCte' acessar o menu: Cadastros gerais > Configurações da empresa > Parâmetros > Empresa. Se o cliente for validar pelo parâmetro, precisa cadastrar o parâmetro “ValidarCte = true”.

## Requisitos necessário para um CT-e ser validado

- Precisa ter XML;
- Nunca foi validado;
- Não pode estar cancelado ou anulado no sistema;
- Emitido nas últimas 24h ou última semana (de acordo com o parâmetro periodoMaximoEmissaoCteEmHorasPorUf) e não consultado nas últimas 6hrs;

Se no CT-e estiver com a seguinte informação: 'Não consultado' na situação e a empresa tiver apenas o parâmetro cadastrado, executar o script a seguir que irá verificar se o Job está cadastrado para a empresa 'Null'.

select \* from agendamento where classe = 'com.transpobrasil.job.ValidacaoCTeJob';

  "Em atenção ao cumprimento de nossas políticas de segurança da informação e privacidade, alguns dados serão ocultados e protegidos".

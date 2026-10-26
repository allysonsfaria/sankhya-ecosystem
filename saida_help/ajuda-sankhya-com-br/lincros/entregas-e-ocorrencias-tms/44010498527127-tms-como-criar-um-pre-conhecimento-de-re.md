---
id: "44010498527127"
titulo: "[TMS] - Como criar um pré-conhecimento de redespacho manualmente"
url: "https://ajuda.sankhya.com.br/hc/pt-br/articles/44010498527127--TMS-Como-criar-um-pr%C3%A9-conhecimento-de-redespacho-manualmente"
trilha: "Lincros > TMS > Entregas e Ocorrências - TMS"
atualizado_em: "2026-10-05T18:39:03Z"
rotulos: ["sync_hc", "lincros", "sync_hash_17bacf18eeb0", "lincros_15019039"]
---

# [TMS] - Como criar um pré-conhecimento de redespacho manualmente

**Menu:** Operacional > Cargas > Pré-conhecimentos

## Objetivo

Criar um pré-conhecimento do tipo **Redespacho** manualmente no TMS Lincros, a partir de um pré-conhecimento Normal já existente. Esse processo é necessário quando o redespacho não foi gerado automaticamente via importação de NF-e, ou quando é preciso criá-lo manualmente para uma nota específica.

## O que é um redespacho?

O redespacho é um pré-conhecimento utilizado quando o transporte de uma mercadoria é dividido em dois ou mais trechos, com transportadoras diferentes em cada trecho. O sistema clona o pré-conhecimento original (tipo Normal), define o tipo como REDESPACHO, vincula a origem e o destino corretos e encadeia com o conhecimento de origem.

**Exemplo:** Uma nota fiscal sai de São Paulo com a Transportadora A até um hub intermediário. A partir desse hub, a Transportadora B realiza o trecho final até o destino. O pré-conhecimento Normal cobre o primeiro trecho e o Redespacho cobre o segundo.

## Pré-requisitos

- A nota fiscal já deve estar importada no sistema;
- O pré-conhecimento Normal da nota já deve existir;
- A transportadora responsável pelo redespacho deve estar cadastrada e ser **diferente** da transportadora do pré-conhecimento Normal (regra obrigatória do sistema);
- O **CEP intermediário** (ponto de transferência entre as transportadoras, ou seja, o destino do primeiro trecho e a origem do segundo) deve ser conhecido e informado. Sem ele, o sistema bloqueia a criação.

## Passo a passo

**1. Acesse a tela de Pré-conhecimentos**

No menu principal, acesse: **Operacional > Cargas > Pré-conhecimentos**

**2. Localize e abra o pré-conhecimento Normal da nota**

Pesquise pelo número da nota fiscal ou pelo número do pré-conhecimento. Confirme que o tipo do pré-conhecimento encontrado é **Normal**. Clique no número dele para abrir o detalhamento.

**3. Abra o diálogo de redespacho**

Dentro do pré-conhecimento, localize na barra de ações a opção para criar um redespacho. O sistema abrirá um **diálogo** com os campos necessários para configurar o redespacho.

**4. Preencha os campos do diálogo**

No diálogo de redespacho, preencha:

- **CEP intermediário:** informe o CEP do ponto de transferência entre as duas transportadoras. Este campo é obrigatório, sem ele o sistema bloqueia a criação;
- **Transportadora:** selecione a transportadora responsável pelo segundo trecho. Deve ser diferente da transportadora do pré-conhecimento Normal.

**5. Clique em "Gerar" para simular**

O botão **Gerar** executa uma simulação, mostrando como o redespacho ficará configurado (origem, destino, transportadora, valores calculados). Use esta etapa para validar as informações antes de confirmar.

**6. Clique em "Salvar" para confirmar a criação**

Após verificar os dados da simulação, clique em **Salvar**. O sistema irá clonar o pré-conhecimento Normal, definir o tipo como REDESPACHO, situação "Criado", e criar o vínculo entre os dois automaticamente.

**7. Verifique o redespacho criado**

Acesse o pré-conhecimento de Redespacho gerado e confirme os dados: origem (CEP intermediário), destino final, transportadora e peso. No pré-conhecimento Normal, o redespacho deve aparecer vinculado.

## Alternativa: criação totalmente manual

Caso o diálogo não esteja disponível para o pré-conhecimento em questão (por exemplo, quando a nota possui cotação spot confirmada), é possível criar o pré-conhecimento de redespacho do zero:

1. Acesse **Operacional > Cargas > Pré-conhecimentos** e clique em **Novo**;
2. Preencha os campos obrigatórios: Remetente, Destinatário, Responsável, Origem (CEP do hub intermediário), Destino (destino final), Peso;
3. Na aba **Transporte**, selecione a transportadora do segundo trecho (diferente da do pré-conhecimento Normal);
4. Salve o pré-conhecimento;
5. Acesse a aba **Notas Fiscais** e vincule a nota fiscal correspondente;
6. Salve novamente.

## Regras de negócio importantes

- **CEP intermediário obrigatório:** sem o CEP intermediário preenchido, o sistema lança erro e não permite criar o redespacho;
- **Transportadoras obrigatoriamente diferentes:** o sistema não permite que a transportadora do Redespacho seja a mesma do pré-conhecimento Normal. Se isso ocorrer, o embarque (romaneio) não será gerado e o sistema apresentará erro de validação;
- **Redespacho sem origem bloqueado:** o sistema valida que o pré-conhecimento do tipo Redespacho obrigatoriamente possui origem definida;
- **Redespacho multinível:** se já existir um redespacho vinculado ao pré-conhecimento Normal, o sistema encadeia o novo redespacho no nível seguinte, desde que as faixas de CEP tenham interseção entre o destino do primeiro trecho e a origem do segundo;
- **Situação inicial:** ao ser gerado, o pré-conhecimento de redespacho assume a situação "Criado".

## Situações de erro mais comuns

- **"CEP intermediário não informado":** preencha o CEP do ponto de transferência entre as transportadoras antes de salvar;
- **Erro de transportadora igual:** verifique se a transportadora selecionada para o redespacho é diferente da transportadora do pré-conhecimento Normal;
- **Redespacho não aparece vinculado na nota:** confirme que o vínculo entre o redespacho e a nota fiscal foi salvo corretamente na aba Notas Fiscais;
- **Erro no embarque após redespacho:** se ao importar o JSON de embarque aparecer o erro "Conhecimento de redespacho possui a mesma transportadora", acesse os dois pré-conhecimentos, corrija a transportadora divergente na aba Transporte e reenvie o JSON.

## Artigos relacionados

- Para redespacho gerado automaticamente via NF-e (tags TF\_CNPJ\_REDESPACHO e TF\_CEP\_REDESPACHO): [Gerar conhecimento de redespacho de forma automática](https://sankhya.zendesk.com/hc/pt-br/articles/44010117758487);
- Para corrigir erro de mesma transportadora no embarque: [Erro ao importar JSON de Embarque - transportadora do redespacho igual à do pré-conhecimento normal](https://intercom.help/ajudalincros/pt-BR/articles/13432895-tms-erro-ao-importar-json-de-embarque-romaneio-no-tms-transportadora-do-redespacho-igual-a-do-pre-conhecimento-normal).

"Em atenção ao cumprimento de nossas políticas de segurança da informação e privacidade, alguns dados serão ocultados e protegidos."

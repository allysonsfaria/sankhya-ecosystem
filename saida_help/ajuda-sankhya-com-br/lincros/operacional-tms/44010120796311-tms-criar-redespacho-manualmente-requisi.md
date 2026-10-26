---
id: "44010120796311"
titulo: "[TMS] - Criar redespacho manualmente: requisitos e erros comuns"
url: "https://ajuda.sankhya.com.br/hc/pt-br/articles/44010120796311--TMS-Criar-redespacho-manualmente-requisitos-e-erros-comuns"
trilha: "Lincros > TMS > Operacional - TMS"
atualizado_em: "2026-10-05T18:30:13Z"
rotulos: ["sync_hc", "lincros", "sync_hash_fbe9bd32e38b", "lincros_17253116"]
---

# [TMS] - Criar redespacho manualmente: requisitos e erros comuns

**Menu:** Operacional > Cargas > Pré-conhecimentos

**Objetivo**: Como criar manualmente um pré-conhecimento do tipo Redespacho a partir do pré-conhecimento Normal e como resolver os erros mais comuns nesse processo

## Considerações:

- O pré-conhecimento de Redespacho representa o segundo trecho do transporte e deve estar sempre vinculado ao pré-conhecimento **Normal** que deu origem a ele;
- O redespacho é criado **a partir do pré-conhecimento Normal** da nota fiscal, e não diretamente pela tela de NF-es;
- É obrigatório informar o **CEP intermediário**, que será o destino do primeiro trecho (Normal) e a origem do segundo (Redespacho);
- A transportadora do redespacho **deve ser diferente** da transportadora do pré-conhecimento Normal de origem.

## Passo a passo

1. Acesse Operacional > Cargas > Pré-conhecimentos e localize o pré-conhecimento **Normal** da nota fiscal;
2. Abra o pré-conhecimento Normal e, na barra de ações, use a opção de criar redespacho (abre uma janela);
3. Informe o **CEP intermediário** (obrigatório);
4. Escolha a **transportadora do redespacho** (diferente da transportadora do Normal);
5. Clique em **Gerar** para simular e, em seguida, em **Salvar**.

## Erros e situações comuns

- **Mensagem 'Selecione um conhecimento de origem para o tipo Redespacho':** o pré-conhecimento de Redespacho está sem vínculo com o Normal de origem. O sistema não permite editar ou salvar um redespacho sem origem. Solução: gere o redespacho novamente a partir do pré-conhecimento Normal, conforme o passo a passo acima;
- **Não consigo criar o redespacho pela nota fiscal ou pela tela de NF-es:** se a nota já possui um pré-conhecimento Normal, o redespacho deve ser criado de dentro dele. Pesquise a NF em Operacional > Cargas > Pré-conhecimentos, abra o Normal e use a opção de redespacho;
- **Transportadora do redespacho igual à do Normal:** o Lincros não permite gerar redespacho com a mesma transportadora do trecho de origem. Escolha uma transportadora diferente;
- **CEP intermediário não informado:** o campo é obrigatório para criar o redespacho.

## Redespacho automático

Se a intenção é que o redespacho seja gerado automaticamente (via roteiro ou via tags no XML da NF-e), consulte o artigo '[[TMS] - Gerar conhecimento de redespacho de forma automática'](https://suporte.lincros.com/pt-BR/articles/13433349-tms-gerar-conhecimento-de-redespacho-de-forma-automatica).

## Alterar a transportadora depois

Para trocar a transportadora de um pré-conhecimento já vinculado a um embarque, consulte o artigo '[[TMS] - Alteração de transportador no embarque e no pré-conhecimento: cenários e restrições](https://suporte.lincros.com/pt-BR/articles/13433331-tms-alteracao-de-transportador-no-embarque-e-no-pre-conhecimento-cenarios-e-restricoes)'.

"Em atenção ao cumprimento de nossas políticas de segurança da informação e privacidade, alguns dados serão ocultados e protegidos"

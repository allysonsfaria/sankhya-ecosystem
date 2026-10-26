---
id: "44012666585239"
titulo: "[TMS] - Não é possível adicionar este documento ( Nota fiscal) dentro do embarque"
url: "https://ajuda.sankhya.com.br/hc/pt-br/articles/44012666585239--TMS-N%C3%A3o-%C3%A9-poss%C3%ADvel-adicionar-este-documento-Nota-fiscal-dentro-do-embarque"
trilha: "Lincros > TMS > Operacional - TMS"
atualizado_em: "2026-10-05T19:35:49Z"
rotulos: ["sync_hc", "lincros", "lincros_13433381", "sync_hash_ff673997f46a"]
---

# [TMS] - Não é possível adicionar este documento ( Nota fiscal) dentro do embarque

**Menu:** Operacional > Cargas > Embarques

**Objetivo**: Como resolver a questão de  'Não é possível adicionar este documento. O conhecimento normal ou o último conhecimento do tipo redespacho do documento, possui a mesma transportadora do embarque' ao lançar uma nota fiscal no embarque

**Considerações**:

- Possuir o embarque criado no sistema;
- Possuir nota fiscal importada no sistema;

 Abaixo segue os procedimentos:

1. Primeiramente consultar a nota fiscal na qual o cliente está tentando adicionar no embarque e que acusa a mensagem citada acima;
2. Verificar se a nota em questão possui dois conhecimentos do tipo 'Normal', conforme exemplo abaixo:

![Imagem 1: Verificar se a nota em questão possui dois conhecimentos do tipo 'Normal', conforme exemplo abaixo:](https://ajuda.sankhya.com.br/hc/article_attachments/44012703555863)

3. Sendo assim, deve-se alterar o  tipo' de carga do pre-conhecimento vinculado ao CT-e de menor valor, pois entende-se que este CT-e é do tipo 'Complementar' e não 'Normal';

![Imagem 2: 3. Sendo assim, deve-se alterar o tipo' de carga do pre-conhecimento vinculado ao CT-e de menor valor, pois entende-se…](https://ajuda.sankhya.com.br/hc/article_attachments/44012688539927)

4. Alterar o tipo da carga do pré-conhecimento de 'Normal' para 'Complementar';

5. Clicar em "Salvar';

5. Após, basta adicionar a nota fiscal no embarque em questão;

"Em atenção ao cumprimento de nossas políticas de segurança da informação e privacidade, alguns dados serão ocultados e protegidos"

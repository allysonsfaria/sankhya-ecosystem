---
id: "44012669215767"
titulo: "[TMS] - Como alterar Transportadora do Pré-conhecimento após importar a Carta de Correção"
url: "https://ajuda.sankhya.com.br/hc/pt-br/articles/44012669215767--TMS-Como-alterar-Transportadora-do-Pr%C3%A9-conhecimento-ap%C3%B3s-importar-a-Carta-de-Corre%C3%A7%C3%A3o"
trilha: "Lincros > TMS > Operacional - TMS"
atualizado_em: "2026-10-05T19:35:07Z"
rotulos: ["sync_hc", "lincros", "lincros_13433410", "sync_hash_d8c870a92e01"]
---

# [TMS] - Como alterar Transportadora do Pré-conhecimento após importar a Carta de Correção

**Menu**: Operacional > Cargas > Pré-conhecimento > Edição de pré-conhecimento > Aba Transporte

**Objetivo**: Instruir o usuário em como alterar a transportadora de um Pré-conhecimento

## Considerações:

- Ao realizar a importação da Carta de Correção para alterar a transportadora é criado um evento na NF-e, porém, a alteração da transportadora não é efetuada automaticamente pelo sistema;
- Cartas de correção, como por exemplo, referentes à mudança da transportadora de uma NF-e são emitidas com campo de texto livre, o que não permite que o sistema possa interpretar de forma precisa para qual transportadora está sendo atualizado o respectivo documento mencionado na mesma;

Sendo assim, a correção da transportadora deve ser realizada no pré-conhecimento manualmente, segue os passos abaixo:

1. Acessar a aba 'Edição de Pré-conhecimento';
2. Acessar a aba 'Transporte';

![Imagem 1: Acessar a aba 'Transporte';](https://ajuda.sankhya.com.br/hc/article_attachments/44012655844119)

3. Acessar a aba 'Transportadora';

4. No campo 'Transportadora' definir a Transportadora e no campo 'filial' definir a filial da Transportador;

![Imagem 2: 4. No campo 'Transportadora' definir a Transportadora e no campo 'filial' definir a filial da Transportador;](https://ajuda.sankhya.com.br/hc/article_attachments/44012669517463)

5. Após, clicar e 'Salvar';

**Obs**: Um ponto de atenção diz respeito a quando um pré-conhecimento está vinculado a um embarque. O sistema possui uma validação na transportadora do pré-conhecimento e de seu respectivo embarque, caso esteja vinculado a um. Nestes casos, pode-se remover o pré-conhecimento do embarque, uma vez que, a transportadora será alterada e entende-se que não mais compõe o frete anterior (carga fechada).

"Em atenção ao cumprimento de nossas políticas de segurança da informação e privacidade, alguns dados serão ocultados e protegidos"

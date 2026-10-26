---
id: "44013195128471"
titulo: "[TMS] - Não é possível ter mais de um CT-e ativo vinculado ao mesmo conhecimento"
url: "https://ajuda.sankhya.com.br/hc/pt-br/articles/44013195128471--TMS-N%C3%A3o-%C3%A9-poss%C3%ADvel-ter-mais-de-um-CT-e-ativo-vinculado-ao-mesmo-conhecimento"
trilha: "Lincros > TMS > Documentos Eletrônicos - TMS"
atualizado_em: "2026-10-05T19:51:06Z"
rotulos: ["sync_hc", "lincros", "lincros_13432819", "sync_hash_0590050ec455"]
---

# [TMS] - Não é possível ter mais de um CT-e ativo vinculado ao mesmo conhecimento

**Menu**: Documentos eletrônicos > CT-es

**Objetivo**: Como ajustar a situação referente a mensagem de alerta apresentada no sistema quando se tenta reabrir um CT-e que já possui vínculo com um pré-conhecimento

**Considerações**:

- Possuir no sistema um Ct-e anulado;

Ao clicar em "Reabrir" determinado CT-e o sistema pergunta se deseja realmente reabrir o CT-e, e então apresenta a seguinte mensagem: 'Não é possível ter mais de um CT-e ativo vinculado ao mesmo conhecimento'.

Importante salientar que aplicamos essa correção para um caso específico, e pode ser que tenhamos que utilizar alguma outra ação caso ocorra situação semelhante.

O mais indicado é sempre analisar o cenário como um todo e, caso seja um caso conforme exemplificado acima, então pode-se aplicar a mesma correção. Caso contrário, terá que analisar e ver qual ação a ser para ajustar este cenário.

![Imagem 1: O mais indicado é sempre analisar o cenário como um todo e, caso seja um caso conforme exemplificado acima, então…](https://ajuda.sankhya.com.br/hc/article_attachments/44013228819863)

Abaixo segue os procedimentos:

1. Acessar o conhecimento vinculado ao CT-e que estava tentando realizar a reabertura;
2. Em seguida consultar o DACTE e verificar que este CT-e pertence à uma determinada nota fiscal. Essa informação pode-se consultar no campo **SÉRIE/NRO. DOCUMENTO** do DACTE, no caso, para encontrar a nota fiscal, e no campo **NÚMERO** para encontrar o número do CT-e. Caso necessário pode-se/deve-se pegar a chave do DACTE e consultar no SEFAZ se estão autorizados;
3. Pegar o número da Nota Fiscal presente no DACTE, consultar no sistema e verificar que não à vínculo com nenhum CT-e;
4. Então movemos este CT-e para o pré-conhecimento vinculado a Nota Fiscal, e desta forma conseguimos reabrir o CT-e que antes apresentava a mensagem 'Não é possível ter mais de um CT-e ativo vinculado ao mesmo conhecimento'.

 "Em atenção ao cumprimento de nossas políticas de segurança da informação e privacidade, alguns dados serão ocultados e protegidos".

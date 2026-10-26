---
id: "360044294473"
titulo: "Como configurar o envio de NF-e em contingência?"
url: "https://ajuda.sankhya.com.br/hc/pt-br/articles/360044294473-Como-configurar-o-envio-de-NF-e-em-conting%C3%AAncia"
trilha: "Dúvidas Frequentes > Configurações Sankhya"
atualizado_em: "2026-07-22T15:58:56Z"
rotulos: ["DUVIDANF", "Configuração", "NF-e", "SEFAZ", "Preferências", "Configuração de Envio de NF-e em Contingência", "Documentos Eletrônicos"]
---

# Como configurar o envio de NF-e em contingência?

**![Imagem 1: SITUAÇÃO:](https://ajuda.sankhya.com.br/hc/article_attachments/17323073418903) SITUAÇÃO:**

Para que se possa trabalhar no sistema com envio de NF-e em modo Contingência são necessárias algumas configurações na tela de preferências da 'Empresa' (Comercial » Preferências » Empresa).

**![Imagem 2: SOLUÇÃO:](https://ajuda.sankhya.com.br/hc/article_attachments/17323098442775) SOLUÇÃO:**

Seguem abaixo alguns campos que deverão ser selecionados com orientação do setor de Contabilidade de sua empresa.

![Imagem 3: Acesse: Comercial » Preferências » Empresa, aba: "NF-/NFC", campo: "Tipo de Envio NF-e"](https://ajuda.sankhya.com.br/hc/article_attachments/17323098446615)Acesse: Comercial » Preferências » Empresa, aba: **"NF-/NFC",** campo: **"Tipo de Envio NF-e"**

Este campo serve para que o usuário possa controlar a forma de contingência que irá trabalhar caso a internet ou a SEFAZ não estejam funcionando. Por exemplo, o serviço na SEFAZ encontra-se ativo, mas o serviço de recepção não. Para isso é necessário trabalhar com a contingência adequada para comunicação eficaz das notas. Este campo possui as seguintes opções de escolha:

- **SEFAZ/Contingência:** o sistema primeiramente tentará comunicar com a Sefaz Estadual e caso falhe a comunicação, envia a nota para a contingência.
- **Preferir contingência:** tenta enviar primeiro para a contingência. Caso o envio para a contingência falhe, tenta enviar para a SEFAZ Estadual.
- **Sempre contingência:** tenta enviar para a contingência. Caso não tenha sucesso **não** tenta enviar para a SEFAZ Estadual.

O campo abaixo determina qual será o ambiente de Contingência a ser utilizado.

- Campo: **"Envio em Contingência"**

Esta opção automatizará os ambientes de contingência para envios de Nota Fiscal Eletrônica. Deve-se escolher uma das seguintes opções:

- **Não usar contingência**: escolhendo esta opção, o sistema não enviará nenhuma Nota Fiscal Eletrônica.
- **Perguntar ao usuário**: escolhendo esta opção, o sistema apresentará uma tela para selecionar a opção desejada na hora do envio da nota.
- **EPEC**: escolhendo esta opção, o programa marcará as notas como EPEC (Evento Prévio de Emissão em Contingência), numerará as notas com a série da SEFAZ e enviará como EPEC. O tempo máximo para transmissão das notas enviadas nesse método é de até 7 dias ou 168 horas.
- **SVC**: ao consultar o "Status do serviço" no webservice estadual (normal) e obter a resposta "107 - Serviço SVC em Operação", as notas deverão ser enviadas em contingência SVC.
- **SVC/EPEC**: escolhendo esta opção, se o SVC não estiver ativo, o sistema irá marcar as notas como EPEC, numerar as notas e enviar EPEC, mas se o SVC estiver ativo, ele irá numerar as notas e enviar ao SVC.

**![Imagem 4: IMPORTANTE:](https://ajuda.sankhya.com.br/hc/article_attachments/17323073438615) IMPORTANTE:**

Se configurada a empresa como tipo de envio NF-e igual a 'Sempre Contingência' e marcar o campo 'Envio em contingência' igual a 'Não usar contingência' o sistema ao gerar a nota pela Central de Vendas emitirá a mensagem: '**Não é possível determinar o tipo de emissão das notas da empresa XXX para o estado de YY.**'

---
id: "360043863934"
titulo: "Quais as configurações para impressão/envio de boleto por e-mail, via Portal de Vendas?"
url: "https://ajuda.sankhya.com.br/hc/pt-br/articles/360043863934-Quais-as-configura%C3%A7%C3%B5es-para-impress%C3%A3o-envio-de-boleto-por-e-mail-via-Portal-de-Vendas"
trilha: "Dúvidas Frequentes > Vendas"
atualizado_em: "2026-07-22T15:58:27Z"
rotulos: ["DUVIDANF", "#Revisadoclaudio", "Configuração", "Impressão", "NF-e", "Portal de Vendas", "Boleto", "Financeiro", "NFS-e", "Imprimir boleto na confirmação manual ou proibido", "Escolha entre Imprimir Enviar e-mail ou ambos", "Verifique Web Connection e condições de impressão/envio", "Geração automática boleto ao confirmar a NF de venda", "Configurações boleto"]
---

# Quais as configurações para impressão/envio de boleto por e-mail, via Portal de Vendas?

![Imagem 1: Tela "Tipos de Operação - TOP" (Caminho de acesso: Comercial » Arquivo » Cadastros):](https://ajuda.sankhya.com.br/hc/article_attachments/17128476775959) Tela **"Tipos de Operação - TOP"** (Caminho de acesso: Comercial » Arquivo » Cadastros):

Aba: **"Impressão",** **"Imprimir Boleto/Duplicata"**: para envio automático de e-mail deverá constar "**Na Confirmação**":

- **Na confirmação:** o boleto será impresso quando efetuar a confirmação da nota, clicando no botão **"Confirmar"**.
- **Manual:** se selecionada, a impressão do boleto será efetuada através do botão **"Imprimir"**, opção **"Imprimir boleto/duplicata"**.
- **Proibido:** se selecionado, o boleto não será impresso. Nos Portais se solicitar a impressão do boleto/duplicata o sistema emite o aviso: Documento (Número da Nota): TOP proíbe impressão de Boleto/Duplicata.

![Imagem 2: Proibido: se selecionado, o boleto não será impresso. Nos Portais se solicitar a impressão do boleto/duplicata o…](https://ajuda.sankhya.com.br/hc/article_attachments/1500013658082)

![Imagem 3: Tela "Parceiros" (Caminho de acesso: Configurações » Cadastros)](https://ajuda.sankhya.com.br/hc/article_attachments/17128446066711) Tela **"Parceiros"** (Caminho de acesso: Configurações » Cadastros)

Aba: **"NF-e/NFS-e/CT-e"**

- Opção **"Geração de boleto nas Centrais":** Imprimir ou Imprimir e Enviar e-mail

**Imprimir:** os boletos serão apenas impressos;

**Imprimir e Enviar e-mail:** deverá além de imprimir também enviar os boletos por e-mail;

**Enviar e-mail:**enviará apenas os boletos para o e-mail. Mesmo assim, se o usuário necessitar efetuar a impressão será possível imprimi-lo através do Portal de Vendas, botão **"Imprimir"**, opção **"Imprimir Boleto"**.

- Campo **"E-mail p/ envio NF-e/NFS-e/CT-e":** coloque os emails, separados por ponto e virgula(;)

![Imagem 4: Campo " E-mail p/ envio NF-e/NFS-e/CT-e": coloque os emails, separados por ponto e virgula(;)](https://ajuda.sankhya.com.br/hc/article_attachments/1500013939741)

**![Imagem 5: OBSERVAÇÃO:](https://ajuda.sankhya.com.br/hc/article_attachments/17128476781975) OBSERVAÇÃO:**

A configuração do campo **"Geração de boletos nas centrais"** terá validade se a TOP utilizada na nota estiver configurada para imprimir boleto/duplicata na confirmação (Cadastro de Tipos de Operação - TOP > Aba Impressão > Imprimir Boleto/Duplicata, opção "Na Confirmação").

Aba: **"Informações"**:

- Opção **"Tipo Geração Boleto" -** Imprimir ou Enviar e-mail: a configuração do campo **"Tipo geração boleto"** irá definir como serão gerados os boletos relacionados aos parceiros em questão. Esta informação está relacionada às rotinas de Nota Fiscal Eletrônica de Serviço - Prefeituras (parâmetro Gerar boleto para NFS-e - NFSEGERARBOLETO) e Faturamento de Contratos.

![Imagem 6: Tela "Tipos de Negociação" (Caminho de acesso: Comercial » Arquivo » Cadastros) Aba: "Características" Opção "…](https://ajuda.sankhya.com.br/hc/article_attachments/17128446077847) Tela **"Tipos de Negociação"** (Caminho de acesso: Comercial » Arquivo » Cadastros)
Aba: **"Características"**
Opção **"Subtipo":** A prazo ou Parcelada
Opção **"Imprimir boleto/duplicata":** para envio automático de e-mail deverá constar Na Confirmação

![Imagem 7: Tela "Contas" (Caminho de acesso: Configurações » Cadastros » Bancários) Aba: "Boleto(s)/Duplicatas" Opção " Emite" :…](https://ajuda.sankhya.com.br/hc/article_attachments/17128476785815) Tela **"Contas"** (Caminho de acesso: Configurações » Cadastros » Bancários)
Aba: **"Boleto(s)/Duplicatas"**
Opção **"Emite"**: marque
Opção **"Modelo":** preencha com o código do Modelo de Boleto (configurado na tela: Financeiro » Relatórios » Modelos de Boleto(s) e vinculado a tela: Configurações » Avançado » Modelos de Nota Fiscal/Duplicatas/Boleto(s)).

**![Imagem 8: OBSERVAÇÃO:](https://ajuda.sankhya.com.br/hc/article_attachments/17128476781975) OBSERVAÇÃO:**

Quando o tipo de negociação tiver parcela que não emite boleto, o tipo de título informado nessa parcela deve estar com a linha "**Proibir impressão boleto?**" marcada.

![Imagem 9: Quando o tipo de negociação tiver parcela que não emite boleto, o tipo de título informado nessa parcela deve estar com…](https://ajuda.sankhya.com.br/hc/article_attachments/9239654531095)

**![Imagem 10: IMPORTANTE:](https://ajuda.sankhya.com.br/hc/article_attachments/17128476788247) IMPORTANTE:**

![Imagem 11: Considerações sobre Web Connection/Navegador Sankhya](https://ajuda.sankhya.com.br/hc/article_attachments/17128476775959) Considerações sobre Web Connection/Navegador Sankhya

- Se utiliza o Web Connection **Externo**, verifique se  ele está Iniciado e atualizado, dúvidas acesse o link [Sankhya Web Connection](https://ajuda.sankhya.com.br/hc/pt-br/articles/360044596394)
- Se utiliza o Navegador Sankhya, o web connection virá embarcado, não necessitando mais do web connection **Externo,**com o Navegador Sankhya atualizado o web connection também estará.
- Poderá ocorrer conflito caso o WebConnection Externo e do Navegador estejam iniciados ao mesmo tempo, pois a porta de comunicação é a mesma (porta:9096)
- Caso necessário aumente a memória utilizada do Web Connection, acessando: Navegador Sankhya>>Configurações Gerais>>Configurações WebConnetion 2.0bXXX, aba **"Geral"**, opção **"Memoria utilizada"**  (esta configuração é por Computador, que faz uso do Web Connection e também deverá verificar se a memória do computador, será suficiente para tal ação).

[GIF animado: Imagem 12: Caso necessário aumente a memória utilizada do Web Connection, acessando: Navegador Sankhya>>Configurações…](https://ajuda.sankhya.com.br/hc/article_attachments/1500013662182)

![Imagem 13: Condições em que o sistema não realiza impressão/envio:](https://ajuda.sankhya.com.br/hc/article_attachments/17128446066711) Condições em que o sistema não realiza impressão/envio:

- Data de Vencimento igual data de negociação.
- Tipo de Negociação com subtipo = À vista
- Títulos já baixados.
- Conta utilizada não configurada para emissão de boleto.

O sistema somente irá enviar boleto por e-mail na confirmação do documento se o lançamento for de um documento fiscal, exemplo NF-e ou NFS-e. Se na TOP a marcação do campo **"NF-e ou NFS-e"** estiver como **"Convencional (Não usa NF-e)"** ou **"Convencional (Não usa NFS-e)"**, o envio automático não ocorre.

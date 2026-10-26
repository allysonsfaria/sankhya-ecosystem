---
id: "39321612658583"
titulo: "Erro: Atenção! A comunicação com a internet não está disponível no momento"
url: "https://ajuda.sankhya.com.br/hc/pt-br/articles/39321612658583-Erro-Aten%C3%A7%C3%A3o-A-comunica%C3%A7%C3%A3o-com-a-internet-n%C3%A3o-est%C3%A1-dispon%C3%ADvel-no-momento"
trilha: "Solução de Problemas > Varejo"
atualizado_em: "2026-07-22T13:55:52Z"
rotulos: ["Configuração", "SEFAZ", "Sankhya Checkout", "Erro", "Artigo criado KCS", "Varejo - KCS", "Internet"]
---

# Erro: Atenção! A comunicação com a internet não está disponível no momento

**MENSAGEM**

Atenção! A comunicação com a internet não está disponível no momento

![Imagem 1: Atenção! A comunicação com a internet não está disponível no momento](https://ajuda.sankhya.com.br/hc/article_attachments/41608193439511)

**SITUAÇÃO**

A mensagem é apresentada no Sankhya Checkout ao tentar habilitar novamente o envio de documentos para a SEFAZ, ou seja, durante o processo de retirada do caixa do modo de contingência.

**SOLUÇÃO**

Para resolver o problema de comunicação com a internet no Checkout, siga os passos abaixo:

**(1)** Verifique se a **"conexão com a internet"** está ativa e funcionando corretamente na máquina do Checkout. Teste acessando sites externos. 

**(2)** Valide se existe algum **"bloqueio na infraestrutura de rede"** que esteja impedindo a comunicação com a **"SEFAZ"**. Verifique configurações de **"firewall"**, **"proxy"** ou **"switches"** que possam estar bloqueando o tráfego.

**(3)** Entre em contato com o **"provedor de internet"** para verificar se há instabilidades ou bloqueios na conexão que possam estar afetando a comunicação.

**(4)** Caso a conexão esteja funcionando em outras máquinas mas não no Checkout, teste conectar a máquina em uma **"rede alternativa"** (como um roteador de celular) para identificar se o problema está relacionado à rede corporativa.

**CAUSA**

A mensagem é apresentada quando há falha na comunicação entre o Sankhya Checkout e os serviços externos necessários para a autorização dos documentos fiscais, especialmente os serviços da SEFAZ.

As causas mais comuns para esse comportamento são:

- Queda ou instabilidade na conexão com a internet;
- Bloqueios na infraestrutura de rede, como firewall, proxy ou equipamentos de rede corporativos;
- Problemas ou instabilidades no provedor de internet;
- Indisponibilidade temporária dos serviços da SEFAZ;
- Configurações incorretas de rede na máquina onde o Sankhya Checkout está sendo executado.
